import pandas as pd
from pytrends.request import TrendReq
import random

class TrendsEngine:
    def __init__(self, geo='IN'):
        self.geo = geo
        self.pytrends = TrendReq(hl='en-US', tz=330)

    def fetch_trends(self, keywords):
        """
        Fetches interest over time for specific keywords.
        Falls back to mock data if API fails (common in local envs).
        """
        try:
            print(f"Fetching Google Trends for: {keywords}...")
            self.pytrends.build_payload(keywords, cat=0, timeframe='today 1-m', geo=self.geo, gprop='')
            data = self.pytrends.interest_over_time()
            if data.empty:
                raise Exception("Empty response from Google Trends")
            
            
            trend_scores = data.mean().sort_values(ascending=False).to_dict()
            return trend_scores
            
        except Exception as e:
            print(f"Warning: Google Trends API failed ({e}). Using simulated trend data.")
            return self._generate_mock_trends(keywords)

    def _generate_mock_trends(self, keywords):
        """Simulates trend scores for robustness."""
        return {k: random.randint(20, 100) for k in keywords}

    def get_related_queries(self, keyword):
        """Get rising related queries for content ideas."""
        try:
            self.pytrends.build_payload([keyword], timeframe='today 1-m', geo=self.geo)
            related = self.pytrends.related_queries()
            if related and related[keyword]['rising'] is not None:
                return related[keyword]['rising']['query'].head(3).tolist()
        except:
            pass

        return [f"Best {keyword} tips", f"{keyword} 2024 trends", f"How to {keyword}"]
