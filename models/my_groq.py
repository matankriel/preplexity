from groq import Groq

class GroqSearchQuery:
    API_KEY = "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"
    MODELS = ["llama-3.3-70b-versatile", "llama3-8b-8192"]

    def __init__(self):
        """
        Initialize the GroqSearchQuery class with static API key and models.
        """
        self.client = Groq(api_key=self.API_KEY)
        self.current_model_index = 0

    def get_best_search_term(self, query):
        """
        Queries the Groq API for the best search term.

        :param query: The search query string.
        :return: The best search term suggested by the API.
        """
        while self.current_model_index < len(self.MODELS):
            model = self.MODELS[self.current_model_index]
            try:
                chat_completion = self.client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"Create the best google-search-term for this query: {query}.\n answer only with query. no yapping.",
                        }
                    ],
                    model=model,
                )
                return chat_completion.choices[0].message.content
            except Exception as e:
                # Check if the error is related to rate limiting and switch model
                if "rate limit" in str(e).lower():
                    self.current_model_index += 1
                else:
                    raise e

        raise Exception("All models have reached their request limits or failed.")
    
    def get_summary(self, text):
        """
        Queries the Groq API for text summary.

        :param text: The text string to summary.
        :return: The summary by the API.
        """
        while self.current_model_index < len(self.MODELS):
            model = self.MODELS[self.current_model_index]
            try:
                chat_completion = self.client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"Create a short summary for this text that was taken from an html page its a mix of all the text in that page: {text}.\n answer only with the summary. no yapping.",
                        }
                    ],
                    model=model,
                )
                return chat_completion.choices[0].message.content
            except Exception as e:
                # Check if the error is related to rate limiting and switch model
                if "rate limit" in str(e).lower():
                    self.current_model_index += 1
                else:
                    raise e

        raise Exception("All models have reached their request limits or failed.")
