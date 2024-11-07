import nlpcloud


class API:
    def __init__(self):
        # Initialize the client with the desired model and API key
        self.client = nlpcloud.Client("distilbert-base-uncased-emotion", "22752f23182b66b8a06bdb6845a9938e6aaaa8a8",
                                      gpu=False)

    def sentiment_analysis(self, text):
        # Use the NLP Cloud client to perform sentiment analysis
        response = self.client.sentiment(text)
        return response


