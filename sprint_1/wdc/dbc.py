from wdc.Query import Query
import requests

class dbc:
    """
    dbc class for connecting to a database.

    Objects of this class are responsible for handling requests that
    are sent to the servers that are specified by the user.

    Object Attributes:
        server_url (str) -> The URL of the database we are accessing to.
    """

    def __init__(self, server_url: str):
        self.server_url = server_url

    def execute_query(self, query: Query | str):
        """
        Sends a query to the server, via requests.

        If the query is an instance of Query class, it will be converted to its WCPS equivalent.

        If it is a string, it will be sent directly

        Parameters:
            query (Query | str) -> The query to send.
        """

        # If query is an instance of Query class, convert it to WCPS string.
        if isinstance(query, Query):
            parsed_query = query.get_wcps()
        else:
            parsed_query = query

        try:
            response = requests.post(self.server_url, data={  'query': parsed_query})
            response.raise_for_status()  # Check for HTTP errors

            # Try to decode as UTF-8; if it fails, return as binary data
            try:
                # Decode as UTF-8 if the content is text
                return response.content.decode('utf-8')
            except UnicodeDecodeError:
                # Return as binary if the content is not text (e.g., images)
                return response.content

        except HTTPError as e:
            return f"HTTP error occurred - {e}"
        except Exception as e:
            return f"Unexpected error - {e}"

    def get_server_capabilities(self):
        """
        Retrieves the capabilities of the server.

        Returns:
            str: The server capabilities information.
        """
        try:
            response = requests.get(f"{self.server_url}/capabilities")
            response.raise_for_status()  # Check for HTTP errors
            return response.content.decode('utf-8')
        except HTTPError as e:
            return f"HTTP error occurred - {e}"
        except Exception as e:
            return f"Unexpected error - {e}"

    def get_coverage_metadata(self, coverage_id: str):
        """
        Retrieves metadata about a specific coverage identified by coverage_id.

        Parameters:
            coverage_id (str): The identifier for the coverage.

        Returns:
            str: Metadata information about the specified coverage.
        """
        try:
            response = requests.get(
                f"{self.server_url}/coverages/{coverage_id}/metadata")
            response.raise_for_status()  # Check for HTTP errors
            return response.content.decode('utf-8')
        except HTTPError as e:
            return f"HTTP error occurred - {e}"
        except Exception as e:
            return f"Unexpected error - {e}"
