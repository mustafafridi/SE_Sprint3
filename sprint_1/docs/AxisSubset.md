
<a id="wdc.AxisSubset"></a>

# wdc.AxisSubset

<a id="wdc.AxisSubset.AxisSubset"></a>

## AxisSubset Objects

```python
class AxisSubset()
```

AxisSubset class to implement WCPS axis subsets.

Object Attributes:
- axis (str) -> Name of the axis as a string.

- start -> Starting point of the subset

- stop = None -> Stopping point of the subset; if it is None, the subset will
consists of a single point, which is the starting point.

<a id="wdc.AxisSubset.AxisSubset.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

String representation of the subset.

<a id="wdc.AxisSubset.AxisSubset.get_wcps"></a>

#### get\_wcps

```python
def get_wcps()
```

Returns the WCPS equivalent of the query.