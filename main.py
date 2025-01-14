from models.search import *
from models.my_groq import *
from models.html_parser import *


if __name__ == "__main__":
    # iniiate classes
    search_api = GoogleSearchAPI()
    parser = HTMLTextParser()
    groq_query = GroqSearchQuery()
    user_query= input("Enter you search query: ")
    # get the best search term
    best_search_term = groq_query.get_best_search_term(user_query)
    print(f"Best search term: {best_search_term}")
    print(best_search_term)
    # get the first search result
    first_result_url = search_api.get_first_search_result(best_search_term)
    print(f"First search result URL: {first_result_url}")
    # get the text from the first search result
    try:
        text = parser.get_text_from_url(first_result_url)
        print(text)
    except Exception as e:
        text = None
        print(f"Error: {e}")
    # get the summary of the text
    if text != None:
        summary = groq_query.get_summary(text)
        print(f"{summary}, \n source: {first_result_url}")
    else:
        print("Error parssing website try again")
