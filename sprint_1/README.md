# wdc: Python-WCPS Datacube Integration Library

## Overview
The wdc library simplifies interaction between Python and WCPS, allowing Python developers to work with geospatial datacubes hosted on [Rasdaman](http://www.rasdaman.org/). By converting Python operations into WCPS queries, developers can seamlessly process datacube operations on the server side.

## Example usage
Here is a basic example showcasing the library's functionalities:

```python
server_url = 'https://ows.rasdaman.org/rasdaman/ows?REQUEST=GetCoverage' 
db_conn = dbc(server_url) 
query = Query(["AverageChloroColorScaled"])
db_obj = dco(db_conn, query)
result = db_obj.execute_query() 
DataVisualizer.display_result(result) 
```

## Main Features
- **WCPS Query Generation:** Create WCPS queries using Python methods.
- **Database Connection Object:** Efficiently manage connections to WCPS servers.
- **Datacube Operations:** Access, subset, process, aggregate, fuse, and encode datacubes.

## Getting Started
To establish a connection to the server, use the following code snippet:

```python
self.dbc = dbc("https://ows.rasdaman.org/rasdaman/ows")
```

In case the above link fails, you can try using this alternative link: "https://ows.rasdaman.org/rasdaman/ows?REQUEST=GetCoverage"

# Query Class
## Overview
The Query class simplifies the construction of WCPS queries without requiring in-depth knowledge of the WCPS language.

## Functionality
- **Accessing Data:** Retrieve data from the specified datacube server.
- **Subsetting:** Easily subset data on the server using the AxisSubset class.
- **Aggregation:** Compute statistical summaries across dimensions of the datacube.
- **Processing:** Construct complex queries using switch-cases and coverage constructor features of WCPS.

# dco Class
## Overview
The dco class allows you to manage both queries and connections within a single object. It can be instantiated with a dbc object and a Query object, providing easy access to the Query object for further modifications.

# Documentation
The "wdc" library includes detailed documentation located in the "docs" folder. Additionally, there are example programs and a Jupyter Notebook available to help users understand and utilize the library effectively.

# Authors
- [Ana-Maria Dobrescu](https://github.com/dobreasca)
- [Solomon Njora](https://github.com/Hensei4)
- [Enes Aksay](https://github.com/Akysens)
- [Thanh Nguyen](https://github.com/iamthienthanh)
- [Salem Bisenebit](https://github.com/salemylkl)