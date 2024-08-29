
<a id="wdc.Query"></a>

# wdc.Query

<a id="wdc.Query.Query"></a>

## Query Objects

```python
class Query()
```

Query class for WCPS query generation via Python.

Includes general attributes of a Query. These attributes are then converted to
WCPS query language. Converting an Query object to str will return its WCPS equivalent.

Inner Classes:
- Types -> An enum class that includes encoding types that the library supports.

- AggregationMethod -> An enum class that has aggregation methods of WCPS.

- CoverageConstructor -> A class that implements the complex WCPS feature of constructing
coverages inside a query.

Object Attributes:
- coverages (List[str]) -> List of coverages the query is applied to

- subset (List[AxisSubset]) -> List of axis subsets to apply to the coverage

- return_type (Query.Types) -> The type to encode the data

- return_value (any) -> The return value of the query

- aggregate (Query.AggregationMethod) = None -> The aggregation method that will be applied
to the coverage

- cases (List) = None -> The list of cases that will be converted to a WCPS switch-case.

<a id="wdc.Query.Query.Types"></a>

## Types Objects

```python
class Types()
```

Query.Types enum class that includes encoding types that is supported by rasdaman.
Currently only png, jpeg, tiff, gif and csv is included.

<a id="wdc.Query.Query.AggregationMethod"></a>

## AggregationMethod Objects

```python
class AggregationMethod()
```

Query.AggregationMethods enum class that has the aggregation operations that users
can implement in their queries. These include:
- avg()
- add() or sum()
- min()
- max()
- count()

<a id="wdc.Query.Query.CoverageConstructor"></a>

## CoverageConstructor Objects

```python
class CoverageConstructor()
```

Query.CoverageConstructor class that implements the coverage constructors of
WCPS language.

Coverage constructors allows users to generate a new coverage from other coverages
on the fly. Even though they can be used in any part of the WCPS query, the library
currently only supports them in the return statement

Object Attributes:
- name (str) -> The name of the constructed coverage

- over (List[AxisSubset]) = None -> List of axes the new coverage will have.
Iterator variables that go through the axis have the name "\$p<Axis Name>". For example
for an axis with the name "x", the corresponding iterator variable would be "$px".

- values (str) -> The expression that computes the constructed coverage's cell values.

<a id="wdc.Query.Query.CoverageConstructor.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

String representation (i.e WCPS) representation of the constructor.

<a id="wdc.Query.Query.CoverageConstructor.get_wcps"></a>

#### get\_wcps

```python
def get_wcps()
```

Returns the WCPS equivalent of the coverage constructor.

<a id="wdc.Query.Query.set_coverages"></a>

#### set\_coverages

```python
def set_coverages(new_coverages: List[str])
```

Set the coverages to query.

**Arguments**:

  new_coverages (List[str]) -> List of coverage names.

<a id="wdc.Query.Query.set_subset"></a>

#### set\_subset

```python
def set_subset(new_subset: List[AxisSubset])
```

Subset of each axis.

**Arguments**:

  new_subset (List[AxisSubset]) -> The new subset.

<a id="wdc.Query.Query.encode"></a>

#### encode

```python
def encode(new_return_type: Type[Types])
```

Set the return type of the query.
This will add the encode() function to the WCPS query,
which will in turn get the response in that format.

Users should use the types that are included in the Query.Types
enum class.

**Arguments**:

  new_return_type (Query.Types) -> The encoding type.

<a id="wdc.Query.Query.set_return_value"></a>

#### set\_return\_value

```python
def set_return_value(new_return_value)
```

Sets the new return value of the query.

<a id="wdc.Query.Query.set_aggregation_method"></a>

#### set\_aggregation\_method

```python
def set_aggregation_method(new_aggregation: AggregationMethod | None)
```

Sets the aggregation method of the query.
These are WCPS fucntions such as avg(), count() etc. that condense coverages into
a single data point.

Users can use the Query.AggregationMethod enums to include an aggregation method in
their queries.

This will make the query ignore the encoding type.

**Arguments**:

  new_aggregation (Query.AggregationMethod or None) -> New aggregation method to apply.

<a id="wdc.Query.Query.reset_aggregation_method"></a>

#### reset\_aggregation\_method

```python
def reset_aggregation_method()
```

Resets the aggregation method. Deletes any aggregation methods from the query
and makes encoding usable again.

<a id="wdc.Query.Query.add_switch_case"></a>

#### add\_switch\_case

```python
def add_switch_case(boolean_expression: str,
                    coverage_expression: str,
                    default: bool = False)
```

Creates a switch statement and adds a case to it.
This will make the Query ignore the return_value attribute.

**Arguments**:

  boolean_expression (str) -> A condition that will trigger a case when it is true
  
  coverage_expression (str) -> If the condition holds, this statement will be returned.
  
  default (bool) = False -> Whether this case is the default case (i.e the case that will
  hold if all other cases fail). It is false by default.

<a id="wdc.Query.Query.reset_cases"></a>

#### reset\_cases

```python
def reset_cases()
```

Resets the cases. This will delete any case specified, and the query
will use the return_value instead of switch.

<a id="wdc.Query.Query.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

String representation of the query.

<a id="wdc.Query.Query.get_wcps"></a>

#### get\_wcps

```python
def get_wcps()
```

Returns string representation (i.e WCPS equivalent) of the query
