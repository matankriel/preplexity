import http.client
import json
import ssl

class GoogleSearchAPI:
    API_URL = "google.serper.dev"
    API_KEY = "55cdfa9aa167717f2f32769c65e9cc5e194f6606"

    def __init__(self):
        """
        Initialize the GoogleSearchAPI class with a custom SSL context.
        """
        self.conn = http.client.HTTPSConnection(
            self.API_URL, context=ssl._create_unverified_context()
        )

    def get_first_search_result(self, query):
        """
        Get the URL of the first organic search result for a given query.

        :param query: The search query string.
        :return: The URL of the first organic search result, or None if no results are found.
        """
        #print("Query:", query)
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': self.API_KEY,
            'Content-Type': 'application/json',
        }

        # Send the POST request to the search endpoint
        self.conn.request("POST", "/search", payload, headers)
        response = self.conn.getresponse()
        data = response.read()
        
        # Decode and parse the JSON response
        response_json = json.loads(data.decode("utf-8"))
        #print("Response JSON:", json.dumps(response_json, indent=2))

        # Extract the first organic search result
        organic_results = response_json.get("organic", [])
        #print("Organic search results:", organic_results)
        if organic_results:
            print(organic_results[0].get("link"))
            return organic_results[0].get("link")  # Return the "link" of the first organic result
        else:
            print("No organic search results found in the response.")
            return None

# Example usage

if __name__ == "__main__":
    search_api = GoogleSearchAPI()
    query = "border collie breed information characteristics temperament"
    first_result_url = search_api.get_first_search_result(query)
    print(f"First search result URL: {first_result_url}")