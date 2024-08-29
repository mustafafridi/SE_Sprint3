
<a id="wdc.dco"></a>

# wdc.dco

<a id="wdc.dco.dco"></a>

## dco Objects

```python
class dco()
```

dco (Datacube Operator) class for managing datacubes.

This class allows users to handle both connections and queries in the same object.

Object Parameters:
- connector (dbc) -> A dbc object that handles connections to data.
- query (Query) -> A Query object that handles query generation.

<a id="wdc.dco.dco.execute_query"></a>

#### execute\_query

```python
def execute_query()
```

Executes the query via the dbc inside the dco object.

**Returns**:

  data (str | bytes) -> The data that server sends. Might contain an error message.

<a id="wdc.dco.dco.Examples"></a>

## Examples Objects

```python
class Examples()
```

This class contains some functions that return some example queries,
also giving the user the availability to change some of the parameters
such as Latitude and Longitude.

<a id="wdc.dco.dco.Examples.get_color_map"></a>

#### get\_color\_map

```python
@staticmethod
def get_color_map(coverage, lat, long, ansi)
```

A query that displays the WCPS switch cases.
It will return a color map from the coverage specified

**Arguments**:

  coverage -> The coverage to apply the query to
  
  lat -> The subset of latitute
  
  long -> The subset of longitute
  
  ansi -> The subset (should be a point) of ansi
