
<a id="wdc.DataVisualizer"></a>

# wdc.DataVisualizer

<a id="wdc.DataVisualizer.DataVisualizer"></a>

## DataVisualizer Objects

```python
class DataVisualizer()
```

DataVisualizer class to display the data received after a WCPS query.

It contains methods of data visualization.

<a id="wdc.DataVisualizer.DataVisualizer.display_result"></a>

#### display\_result

```python
@staticmethod
def display_result(result)
```

Displays the given data.
If it is string data, it will show the decoded text.
If it is not, it will try to display it as an image.
If everything fails, it will raise an error.

**Arguments**:

  result (any) -> The data that we want to display.

<a id="wdc.DataVisualizer.DataVisualizer.NondecodableBytesError"></a>

## NondecodableBytesError Objects

```python
class NondecodableBytesError(Exception)
```

Raised when the visualizer cannot display the result.

This does not mean the bytes have no meaning, but it means that
the DataVisualizer class cannot figure out what it is.
