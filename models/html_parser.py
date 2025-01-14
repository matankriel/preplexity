

import requests
from bs4 import BeautifulSoup

class HTMLTextParser:
    def __init__(self):
        """
        Initialize the HTMLTextParser class.
        """
        pass

    def get_text_from_url(self, url):
        """
        Retrieve all text content from the HTML page of a given URL.

        :param url: The URL of the web page to parse.
        :return: A string containing all the text from the page.
        """
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text(strip=True)
        else:
            raise Exception(f"Failed to retrieve URL. Status code: {response.status_code}")

# Example usage:
if __name__ == "__main__":
    parser = HTMLTextParser()
    url = "https://google.com"
    try:
        text = parser.get_text_from_url(url)
        print(text)
    except Exception as e:
        print(f"Error: {e}")