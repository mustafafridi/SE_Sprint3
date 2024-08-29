class DataVisualizer:
    """
    DataVisualizer class to display the data received after a WCPS query.

    It contains methods of data visualization.
    """

    @staticmethod
    def display_result(result):
        """
        Displays the given data.
        If it is string data, it will show the decoded text.
        If it is not, it will try to display it as an image.
        If everything fails, it will raise an error.

        Parameters:
            result (any) -> The data that we want to display.
        """

        if isinstance(result, bytes):
            try:
                # First attempt to decode assuming it's text
                decoded_text = result.decode('utf-8')
                print(decoded_text)  # If successful, print the decoded text
            except UnicodeDecodeError:
                # If decoding fails, assume it might be an image
                try:
                    image = Image.open(io.BytesIO(result))
                    image.show()
                except IOError:
                    print(
                        "Failed to display image or decode text. Data might be corrupted or non-textual.")
        elif isinstance(result, str):
            # If it's already a string, just print it
            print(result)
        elif isinstance(result, list):
            # If it's a list, assume it's CSV data and try to plot it as a graph
            try:
                import pandas as pd
                df = pd.DataFrame(result)
                df.plot()
                plt.show()
            except Exception as e:
                print("Failed to plot the data as a graph.")
        else:
            raise DataVisualizer.NondecodableBytesError(
                "Visualizer cannot decode the data")

    class NondecodableBytesError(Exception):
        """
        Raised when the visualizer cannot display the result.

        This does not mean the bytes have no meaning, but it means that
        the DataVisualizer class cannot figure out what it is.
        """
        pass
