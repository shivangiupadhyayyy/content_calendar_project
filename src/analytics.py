import pandas as pd

class AnalyticsEngine:
    def __init__(self, df):
        self.df = df

    def get_brand_performance(self, brand_name):
        brand_data = self.df[self.df['brand_name'] == brand_name]
        
        if brand_data.empty:
            return None

        
        avg_engagement = brand_data.groupby('post_type')['engagement_score'].mean()
        best_format = avg_engagement.idxmax()

        
        top_posts = brand_data.sort_values(by='engagement_score', ascending=False).head(3)
        
        
        top_themes = []
        for _, row in top_posts.iterrows():
            top_themes.append({
                'caption': row['caption'],
                'url': row.get('post_url', ''),
                'location': row.get('location', '')
            })

        return {
            'best_format': best_format,
            'top_themes': top_themes, 
            'avg_engagement': brand_data['engagement_score'].mean()

        }
