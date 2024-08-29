from wdc import Query, AxisSubset, dbc, dco, DataVisualizer
from PIL import Image
import io

# Some example queries

d = dbc("https://ows.rasdaman.org/rasdaman/ows?&SERVICE=WCS&ACCEPTVERSIONS=2.1.0&REQUEST=GetCapabilities")
q =  Query(["AvgLandTemp"])

datacube = dco(d, q)

print("First query:\n")
print(datacube.query)

datacube.query.set_subset([AxisSubset("ansi", "2014-07"),
                           AxisSubset("Lat", -20, 30),
                           AxisSubset("Long", 10, 30)])

print()
print("Second query (subsetting):\n")
print(datacube.query)

datacube.query.encode(Query.Types.png)

print()
print("Third query (encode to png):\n")
print(datacube.query)

datacube.query.set_aggregation_method(Query.AggregationMethod.max)

print()
print("Fourth query (maximum temperature of the day):\n")
print(datacube.query)

datacube.query.reset_aggregation_method()
datacube.query.add_switch_case("$c = 99999", "{red: 255, green: 255, blue: 255}")
datacube.query.add_switch_case("18 > $c", "{red: 0, green: 0, blue: 255}")
datacube.query.add_switch_case("23 > $c", "{red: 255, green: 255, blue: 0}")
datacube.query.add_switch_case("30 > $c", "{red: 255, green: 140, blue: 0}")   
datacube.query.add_switch_case("", "{red: 255, green: 0, blue: 0}", default=True)

print()
print("Fifth query (switch case):\n")
print(datacube.query)
