import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string


class SentimentAnalyzer:
    """
    Perform sentiment analysis on a string
    """

    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()

    def getScore(self, text: str) -> dict:
        """
        Returns 
        ```
        {
            'neg' : <score>,
            'pos' : <score>
        }
        ```
        """
        text = text.translate(str.maketrans('', '', string.punctuation))
        score = self.sid.polarity_scores(text)
        score.pop("compound")
        score.pop("neu")
        sentiment = max(score, key=score.get)
        return score


# tests
if __name__ == "__main__":
    text = 'We purchased new office furniture from this location  We were advised the shipment would arrive in 3 business days  The shipment was delivered the same day as promised  We received excellent service from the first step into their showroom at their location on Dean Martin all thru the delivery  Very positive experience and great pricing for the quality items we purchased  Very pleased and will be purchasing more furniture from this store'
    sa = SentimentAnalyzer()
    print(sa.getScore(text))
