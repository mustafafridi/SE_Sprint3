from wdc.dbc import dbc
from wdc.Query import Query

class dco:
    """
    dco (Datacube Operator) class for managing datacubes.

    This class allows users to handle both connections and queries in the same object.

    Object Parameters:
        connector (dbc) -> A dbc object that handles connections to data.
        query (Query) -> A Query object that handles query generation.
    """

    def __init__(self, connector: dbc, query: Query):
        self.connector = connector
        self.query = query
    
    def execute_query(self):
        """
        Executes the query via the dbc inside the dco object.

        Return:
            data (str | bytes) -> The data that server sends. Might contain an error message.
        """
        data = dbc.execute_query(self.query)
        return data

    class Examples:
        """
        This class contains some functions that return some example queries,
        also giving the user the availability to change some of the parameters
        such as Latitude and Longitude.
        """
        @staticmethod
        def get_color_map(coverage, lat, long, ansi):
            """
            A query that displays the WCPS switch cases.
            It will return a color map from the coverage specified

            Parameters:
                coverage -> The coverage to apply the query to

                lat -> The subset of latitute

                long -> The subset of longitute

                ansi -> The subset (should be a point) of ansi
            """
            
            return f"""
            image>>for $c in ({coverage}) 
            return encode(
                switch 
                        case $c[ansi({ansi[:7]}), Lat({lat}), Long({long})] = 99999 
                            return {{red: 255; green: 255; blue: 255}} 
                        case 18 > $c[ansi({ansi[:7]}), Lat({lat}), Long({long})] 
                            return {{red: 0; green: 0; blue: 255}} 
                        case 23 > $c[ansi({ansi[:7]}), Lat({lat}), Long({long})] 
                            return {{red: 255; green: 255; blue: 0}} 
                        case 30 > $c[ansi({ansi[:7]}), Lat({lat}), Long({long})]  
                            return {{red: 255; green: 140; blue: 0}} 
                        default return {{red: 255; green: 0; blue: 0}}
                    , "image/png")
            """

        # Constructs a gradient-looking image to represent the coverage
        @staticmethod
        def construct_gradient_image(coverage):
            return f"""
            image>>for $c in ({coverage}) 
            return encode(
                            coverage myCoverage
                            over $p x(0:200),
                                $q y(0:200)
                            values $p + $q
                , "image/png")
            """

        # Transforms the 3D data into 1-dimensional data
        @staticmethod
        def transform_to_1d(coverage, lat, long, ansi):
            return f"""
            diagram>>for $c in ({coverage})
            return encode(
                        $c[Lat({lat}), Long({long}), ansi({ansi})]
                    , "text/csv")
            """

        # Transforms the 3D data into 2-dimensional data
        @staticmethod
        def transform_to_2d(coverage, ansi):
            return f"""
            image>>for $c in ({coverage})
            return encode(
                        $c[ansi({ansi[:7]})]
                    , "image/png")
            """

        # Converts Celsius data to Kelvin
        @staticmethod
        def celsius_to_kelvin(coverage, lat, long, ansi):
            return f"""
            diagram>>for $c in ({coverage}) 
            return encode(
                            $c[Lat({lat}), Long({long}), ansi({ansi})] 
                            + 273.15
                    , "text/csv")
            """

        # Gets the minimum value from the data
        @staticmethod
        def get_minimum(coverage, lat, long, ansi):
            return f"""
            for $c in ({coverage}) 
            return 
                min($c[Lat({lat}), Long({long}), ansi({ansi})])
            """

        # Gets the maximum value from the data
        @staticmethod
        def get_maximum(coverage, lat, long, ansi):
            return f"""
            for $c in ({coverage}) 
            return 
                max($c[Lat({lat}), Long({long}), ansi({ansi})])
            """

        # Gets the average value from the data
        @staticmethod
        def get_average(coverage, lat, long, ansi):
            return f"""
            for $c in ({coverage}) 
            return 
                avg($c[Lat({lat}), Long({long}), ansi({ansi})])
            """

        # Finds out when the temperature is less than 10
        @staticmethod
        def temperature_less_10(coverage, lat, long, ansi):
            return f"""
            for $c in ({coverage})
            return count(
                    $c[Lat({lat}), Long({long}), ansi({ansi})]
                < 10)
            """
        
        # Finds out when the temperature is bigger than 20
        @staticmethod
        def temperature_greater_20(coverage, lat, long, ansi):
            return f"""
            for $c in ({coverage})
            return count(
                    $c[Lat({lat}), Long({long}), ansi({ansi})]
                >20)
            """
        # The most basic query - simply returns 1 for each pixel in coverage
        @staticmethod
        def basic_query(coverage):
            return f"""
            for $c in ({coverage}) return 1
            """
        
        # Returns a single value at a specific point
        @staticmethod
        def get_single_value(coverage, lat, long, ansi):
            return f"""
            for $c in ({coverage}) 
            return $c[Lat({lat}), Long({long}), ansi({ansi[:7]})]
            """  