import pandas as pd
import random
from datetime import timedelta

class CalendarGenerator:
    def __init__(self, start_date, days=30):
        self.start_date = pd.to_datetime(start_date)
        self.days = days

    def generate_caption(self, topic, brand_niche):
        templates = [
            f"Here is why {topic} is taking over the {brand_niche} world! 🚀",
            f"Have you tried {topic} yet? Let us know below! 👇",
            f"The ultimate guide to {topic}. Save this for later! 📌"
        ]
        return random.choice(templates)

    def create_calendar(self, brands_df, analytics, trend_engine):
        calendar_rows = []
        unique_brands = brands_df['brand_name'].unique()
        niche_map = dict(zip(brands_df['brand_name'], brands_df['niche']))

        for i in range(self.days):
            current_date = self.start_date + timedelta(days=i)
            
            for brand in unique_brands:
                niche = niche_map[brand]
                perf_metrics = analytics.get_brand_performance(brand)
                
                is_trend_day = random.random() > 0.4
                
                content_type = ""
                content_idea = ""
                source = ""
                ref_url = ""      # NEW Column
                location_tip = "" # NEW Column

                if is_trend_day:
                    # Google Trends Logic
                    related_queries = trend_engine.get_related_queries(niche)
                    trend_topic = random.choice(related_queries)
                    content_idea = f"Trend Alert: Discussing '{trend_topic}'"
                    source = "Google Trends"
                    content_type = "Reel" 
                else:
                    # Historical Data Logic (Ab URL bhi use karega)
                    # Pick a random top performer object
                    best_post = random.choice(perf_metrics['top_themes'])
                    
                    historical_caption = str(best_post['caption'])
                    short_theme = (historical_caption[:40] + '..') if len(historical_caption) > 40 else historical_caption
                    
                    content_idea = f"Repurpose Hit: {short_theme}"
                    ref_url = best_post['url']  # Link to original post
                    
                    # Agar location thi, toh suggest karo
                    if best_post['location'] and str(best_post['location']) != 'nan':
                        location_tip = f"Tag Location: {best_post['location']}"
                    
                    source = "Historical Data"
                    content_type = perf_metrics['best_format'].title()

                if i % 3 == 0 and not is_trend_day:
                     content_type = "Carousel"

                calendar_rows.append({
                    'Date': current_date.strftime('%Y-%m-%d'),
                    'Brand Name': brand,
                    'Platform': 'Instagram',
                    'Content Type': content_type,
                    'Content Idea': content_idea,
                    'Ref URL': ref_url,           # <-- User can click here
                    'Location Tip': location_tip, # <-- User knows where to tag
                    'Caption Hook': self.generate_caption(content_idea.split(': ')[-1], niche),
                    'Hashtags': f"#{niche} #{content_type} #fyp",
                    'Trend Source': source
                })

        return pd.DataFrame(calendar_rows)