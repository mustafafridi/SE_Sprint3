
<a id="wdc.dbc"></a>

# wdc.dbc

<a id="wdc.dbc.dbc"></a>

## dbc Objects

```python
class dbc()
```

dbc class for connecting to a database.

Objects of this class are responsible for handling requests that
are sent to the servers that are specified by the user.

Object Attributes:
- server_url (str) -> The URL of the database we are accessing to.

<a id="wdc.dbc.dbc.execute_query"></a>

#### execute\_query

```python
def execute_query(query: Query | str)
```

Sends a query to the server, via requests.

If the query is an instance of Query class, it will be converted to its WCPS equivalent.

If it is a string, it will be sent directly

**Arguments**:

  query (Query | str) -> The query to send.
