import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os


BRANDS = {
    'TechNova': 'Technology',
    'FitLife_India': 'Fitness',
    'CurryCraze': 'Food',
    'VogueVibes': 'Fashion',
    'TravelDiaries_IN': 'Travel',
    'EduSpark': 'Education',
    'FinSmart': 'Finance',
    'HomeDecor_Hub': 'Interior Design',
    'PetPals': 'Pets',
    'GamerZone': 'Gaming'
}

POST_TYPES = ['reel', 'post', 'story', 'carousel']
THEMES = ['Tips', 'Behind the Scenes', 'Product Launch', 'Meme', 'Tutorial', 'Motivation']

def generate_mock_csvs():
    os.makedirs('data/raw_instagram', exist_ok=True)
    
    for brand, niche in BRANDS.items():
        data = []
        
        for i in range(50):
            date_posted = datetime.now() - timedelta(days=random.randint(1, 180))
            p_type = random.choice(POST_TYPES)
            
            
            base_likes = random.randint(50, 500)
            if p_type == 'reel':
                base_likes *= 2.5
            
            entry = {
                'post_id': f"{brand}_{i+100}",
                'brand_name': brand,
                'niche': niche,
                'post_type': p_type,
                'caption': f"Loving this new {niche} update! #{niche} #trending",
                'hashtags': f"#{niche} #{random.choice(THEMES).lower().replace(' ', '')}",
                'likes': int(base_likes),
                'comments': int(base_likes * 0.05),
                'date_posted': date_posted.strftime('%Y-%m-%d')
            }
            data.append(entry)
        
        df = pd.DataFrame(data)
        df.to_csv(f'data/raw_instagram/{brand}_history.csv', index=False)
        print(f"Generated data for {brand}")

if __name__ == "__main__":

    generate_mock_csvs()
