from typing import List, Type
from wdc.AxisSubset import AxisSubset
from enum import Enum

class Query:
    """
    Query class for WCPS query generation via Python.

    Includes general attributes of a Query. These attributes are then converted to 
    WCPS query language. Converting an Query object to str will return its WCPS equivalent.

    Inner Classes:
        Types -> An enum class that includes encoding types that the library supports.

        AggregationMethod -> An enum class that has aggregation methods of WCPS.

        CoverageConstructor -> A class that implements the complex WCPS feature of constructing
        coverages inside a query.

    Object Attributes:
        coverages (List[str]) -> List of coverages the query is applied to

        subset (List[AxisSubset]) -> List of axis subsets to apply to the coverage

        return_type (Query.Types) -> The type to encode the data

        return_value (any) -> The return value of the query
        
        aggregate (Query.AggregationMethod) = None -> The aggregation method that will be applied
        to the coverage

        cases (List) = None -> The list of cases that will be converted to a WCPS switch-case.
    """

    class Types:
        """
        Query.Types enum class that includes encoding types that is supported by rasdaman.
        Currently only png, jpeg, tiff, gif and csv is included.
        """
        png = "image/png"
        jpeg = "image/jpeg"
        tiff = "image/tiff"
        gif = "image/gif"
        csv = "text/csv"

    class AggregationMethod:
        """
        Query.AggregationMethods enum class that has the aggregation operations that users
        can implement in their queries. These include:
        - avg()
        - add() or sum()
        - min()
        - max()
        - count()
        """
        avg = "avg"
        add = "sum"
        sum = "sum"
        min = "min"
        max = "max"
        count = "count"

    class CoverageConstructor:
        """
        Query.CoverageConstructor class that implements the coverage constructors of
        WCPS language.

        Coverage constructors allows users to generate a new coverage from other coverages
        on the fly. Even though they can be used in any part of the WCPS query, the library
        currently only supports them in the return statement

        Object Attributes:
            name (str) -> The name of the constructed coverage

            over (List[AxisSubset]) = None -> List of axes the new coverage will have.
            Iterator variables that go through the axis have the name "$p<Axis Name>". For example
            for an axis with the name "x", the corresponding iterator variable would be "$px".

            values (str) -> The expression that computes the constructed coverage's cell values.
        """
        
        def __init__(self, name: str, over: List[AxisSubset], values: str):
            self.name = name
            self.over = over
            self.values = values

        def __str__(self):
            """
            String representation (i.e WCPS) representation of the constructor.
            """
            
            constructor_wcps = []
            constructor_wcps.append(f"coverage {self.name}")

            over_text = [f"$p{ax.axis} {ax}" for ax in self.over]
            over_text = ", ".join(over_text)

            constructor_wcps.append(f"over {over_text}")

            constructor_wcps.append(f"values {self.values}")

            return "\n".join(constructor_wcps)
        
        def get_wcps(self):
            """
            Returns the WCPS equivalent of the coverage constructor.
            """
            return str(self)
            

    def __init__(self, coverages: List[str], return_value = "$c", 
                 subset: List[AxisSubset] = None, return_type = None):
        self.coverages = coverages
        self.subset = subset
        self.return_type = return_type
        self.return_value = return_value
        self.aggregate = None
        self.cases = None

    def set_coverages(self, new_coverages: List[str]):
        """
        Set the coverages to query.

        Parameters:
        new_coverages (List[str]) -> List of coverage names.
        """
        self.coverages = new_coverages

    def set_subset(self, new_subset: List[AxisSubset]):
        """
        Subset of each axis.
        
        Parameters:
        new_subset (List[AxisSubset]) -> The new subset.
        """
        self.subset = new_subset

    def encode(self, new_return_type: Type[Types]):
        """
        Set the return type of the query.
        This will add the encode() function to the WCPS query,
        which will in turn get the response in that format.

        Users should use the types that are included in the Query.Types
        enum class.

        Parameters:
            new_return_type (Query.Types) -> The encoding type. 
        """
        self.return_type = new_return_type

    def set_return_value(self, new_return_value):
        """
        Sets the new return value of the query.
        """
        self.return_value = new_return_value
    
    def set_aggregation_method(self, new_aggregation: AggregationMethod | None):
        """
        Sets the aggregation method of the query.
        These are WCPS fucntions such as avg(), count() etc. that condense coverages into
        a single data point.
        
        Users can use the Query.AggregationMethod enums to include an aggregation method in
        their queries.

        This will make the query ignore the encoding type.

        Parameters:
            new_aggregation (Query.AggregationMethod or None) -> New aggregation method to apply. 
        """
        self.aggregate = new_aggregation

    def reset_aggregation_method(self):
        """
        Resets the aggregation method. Deletes any aggregation methods from the query
        and makes encoding usable again.
        """
        self.aggregate = None

    def add_switch_case(self, boolean_expression: str, coverage_expression: str, 
                        default: bool = False):
        """
        Creates a switch statement and adds a case to it.
        This will make the Query ignore the return_value attribute.

        Parameters:
            boolean_expression (str) -> A condition that will trigger a case when it is true
            
            coverage_expression (str) -> If the condition holds, this statement will be returned.
            
            default (bool) = False -> Whether this case is the default case (i.e the case that will
            hold if all other cases fail). It is false by default.
        """

        # Create a list of cases if it does not exist.
        if self.cases == None:
            self.cases = []
        
        # Add the case as a dictionary to the list of cases.
        self.cases.append({"default": default, 
                           "bool_exp": boolean_expression, 
                           "cov_exp": coverage_expression})

    def reset_cases(self):
        """
        Resets the cases. This will delete any case specified, and the query
        will use the return_value instead of switch.
        """
        self.cases = None

    def __str__(self):
        """
        String representation of the query.
        """

        # Start with empty list of query texts
        query_string = []

        if len(self.coverages) > 1:
            # If we have more than one coverage
            # Include all in the for statement of the query
            query_string.append("for $c in (" + ",".join(self.coverages) + ")")
        elif len(self.coverages) == 1:
            # If there is only one coverage
            # Include just that in the for statement
            query_string.append("for $c in ( " + self.coverages[0] + " )")
        else:
            # If there is no coverage in the list,
            # query is illegal, raise NoCoverageException
            raise Query.Exceptions.NoCoverageException()
        
        if self.subset != None and len(self.subset) > 0:
            # If there is a subset, include them as a variable in the query

            subset_string = ", ".join(map(AxisSubset.get_wcps, self.subset))
            query_string.append(f"let $subset := [{subset_string}]")
        
        return_text = "return"

        # If there is an aggregation method specified
        if self.aggregate != None:
            return_text += f" {self.aggregate} ("
        elif self.return_type != None:
            # And there is no aggregate method
            # and if there is a return type
            return_text += f" encode ("

        # Switch cases
        if self.cases != None:
            # If we have cases, create a switch case text
            switch_text = [" ( ", "switch"]
            
            for case in self.cases:
                if case["default"] == True:
                    switch_text.append(f"default return {case['cov_exp']}")
                else:
                    switch_text.append(f"case {case['bool_exp']} return {case['cov_exp']}")
            
            switch_text.append(" )")

            return_text += "\n".join(switch_text)
        else:
            # No switch case, manual return_value
            # Add the returnValue to the return part of the query
            if self.return_value == "$c":
                return_text += f" ( {self.return_value} "
            else:
                return_text += f" ( ( {self.return_value} ) "

        # Apply subset to the result, if it exists
        if self.subset != None and len(self.subset) > 0:
            return_text += " [ $subset ]"
        
        if self.cases == None:
            return_text += f" )"

        # If there is an aggregation method
        if self.aggregate != None:
            return_text += f" )"
        # If there is a return type and no aggregation method
        elif self.return_type != None:
            return_text += f" , \"{self.return_type}\" )"

        query_string.append(return_text)

        return "\n".join(query_string)

    def get_wcps(self):
        """
        Returns string representation (i.e WCPS equivalent) of the query
        """
        return str(self)