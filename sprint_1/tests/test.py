import unittest
import threading
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

from wdc import DataVisualizer, dco, dbc, Query, AxisSubset

class testcases(unittest.TestCase):
    def setUp(self):
        self.dbc = dbc("https://ows.rasdaman.org/rasdaman/ows")

    def test_minimum(self):
        """
        Tests a query where we look for the minimum temperature of a given coordinate
        in a time period.
        """
        
        # Create a query.
        query = Query(["AvgLandTemp"])
        query.set_subset([AxisSubset("ansi", "2003-09", "2009-02"), AxisSubset("Lat", 27.09), AxisSubset("Long", 64)])
        query.set_aggregation_method(Query.AggregationMethod.min)

        # Send query to rasdaman servers
        res = self.dbc.execute_query(query)
        
        # Check if the returned value is correct.
        self.assertEqual(res, '14.409449')

    def test_maximum(self):
        """
        Tests a query where we look for the maximum temperature of a given coordinate
        in a time period.
        """

        # Create a query.
        query = Query(["AvgLandTemp"])
        query.set_subset([AxisSubset("ansi", "2003-09", "2009-02"), AxisSubset("Lat", 27.09), AxisSubset("Long", 67)])
        query.set_aggregation_method(Query.AggregationMethod.max)

        # Send query to rasdaman servers
        res = self.dbc.execute_query(query)
        
        # Check if the returned value is correct.
        self.assertEqual(res, '45.0')

    def test_average(self):
        """
        Tests a query where we look for the average temperature of a 
        certain coordinate during a time period.
        """

        # Create a query
        query = Query(["AvgLandTemp"])
        query.set_subset([AxisSubset("ansi", "2007-04", "2009-02"), AxisSubset("Lat", 43), AxisSubset("Long", 57)])
        query.set_aggregation_method(Query.AggregationMethod.avg)

        # Send a request
        res = self.dbc.execute_query(query)
        
        # Check if the returned value is correct
        self.assertEqual(res, '23.58781221120254')


    def test_count_temp_10(self):
        """
        Tests a query where we check how many times the temperature was
        less than 10 degree Celcius in a certain location within a timeframe.
        """

        query = Query(["AvgLandTemp"])

        query.set_aggregation_method(Query.AggregationMethod.count)

        query.set_subset([AxisSubset("ansi", "2008-04", "2015-02"), AxisSubset("Lat", 56), AxisSubset("Long", 89)])

        # Manually typing condition
        query.set_return_value("$c < 10")

        res = self.dbc.execute_query(query)

        self.assertEqual(res, '49')
    
    def test_basic(self):
        """
        Test a simple query that always returns 1.
        """

        query = Query(["AverageChloroColorScaled"])

        query.set_return_value(1)

        res = self.dbc.execute_query(query)

        self.assertEqual(res, '1')
        
    
        
    def test_load(self):
        num_threads=5  
        requests_per_thread=10  
        def send_queries():
            for _ in range(requests_per_thread):
                query="""
                diagram>>for $c in ({self.coverage})
                return encode( $c[Lat({lat}), Long({long}), ansi({ansi})]
                , "text/csv")
                """  
                self.dbc.execute_query(query)
        threads=[]
        for _ in range(num_threads):
            thread=threading.Thread(target=send_queries)
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
            
    def test_invalid_url(self):
        """
        Test initializing dbc with an invalid server URL.
        """

        with self.assertRaises(Exception):
            dbc("invalid_url")

    def test_empty_query(self):
        """
        Test sending an empty query.
        """

        res = self.dbc.execute_query("")
        self.assertEqual(res, 'Empty query')

    def test_nonexistent_coordinate(self):
        """
        Test querying for a coordinate that does not exist.
        """

        query = Query(["AvgLandTemp"])
        query.set_subset([AxisSubset("ansi", "2003-09", "2009-02"), AxisSubset("Lat", 100), AxisSubset("Long", 100)])
        query.set_aggregation_method(Query.AggregationMethod.min)

        res = self.dbc.execute_query(query)
        self.assertEqual(res, 'Coordinate does not exist')

    def test_invalid_aggregation_method(self):
        """
        Test setting an invalid aggregation method in the query.
        """

        query = Query(["AvgLandTemp"])
        query.set_aggregation_method("invalid_method")

        res = self.dbc.execute_query(query)
        self.assertEqual(res, 'Invalid aggregation method')

    def test_large_concurrent_requests(self):
        """
        Test sending a large number of concurrent requests.
        """

        num_threads = 10
        requests_per_thread = 5

        def send_queries():
            for _ in range(requests_per_thread):
                query = "SELECT * FROM table"
                self.dbc.execute_query(query)

        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=send_queries)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
            
            
if __name__=='__main__':
    unittest.main()