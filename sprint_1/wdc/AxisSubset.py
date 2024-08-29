class AxisSubset:
    """
    AxisSubset class to implement WCPS axis subsets.

    Object Attributes:
        axis (str) -> Name of the axis as a string.

        start -> Starting point of the subset

        stop = None -> Stopping point of the subset; if it is None, the subset will
        consists of a single point, which is the starting point. 
    """

    def __init__(self, axis: str, start, stop = None):
        self.axis = axis
        self.start = start
        self.stop = stop

    def __str__(self):
        """
        String representation of the subset.
        """

        axis_string = f"{self.axis}("

        axis_string += f"\"{self.start}\"" if isinstance(self.start, str) else f"{self.start}"
        if self.stop != None:
            axis_string += f":\"{self.stop}\"" if isinstance(self.stop, str) else f":{self.stop}"
        
        axis_string += ")"

        return axis_string
    
    def get_wcps(self):
        """
        Returns the WCPS equivalent of the query.
        """
        return str(self)
