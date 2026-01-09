import pandas as pd
import glob
import os

class DataLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.niche_map = {
            'snitch.co.in': 'Fashion',
            'zomato': 'Food',
            'lenskart': 'Eyewear'
        }

    def load_all_brands(self):
        if not os.path.exists(self.folder_path):
            raise FileNotFoundError(f"Folder nahi mila: {self.folder_path}")

        all_files = glob.glob(os.path.join(self.folder_path, "*.csv"))
        
        if not all_files:
            raise FileNotFoundError("Folder mein koi CSV file nahi mili.")

        df_list = []
        print(f"      Found {len(all_files)} CSV files. Processing FULL Data...")

        for filename in all_files:
            try:
                df = pd.read_csv(filename)
                
                # --- AUTO-DETECT & EXTRACT ALL COLUMNS ---
                if 'User Name' in df.columns:
                    clean_df = pd.DataFrame()
                    
                    # 1. Basic Info
                    clean_df['brand_name'] = df['User Name']
                    clean_df['caption'] = df['Caption']
                    clean_df['hashtags'] = df['Hashtags']
                    clean_df['date_posted'] = pd.to_datetime(df['Date(GMT)'], errors='coerce')
                    
                    # 2. Engagement Metrics (Ab Views bhi use honge)
                    clean_df['likes'] = df['Likes'].fillna(0)
                    clean_df['comments'] = df['Comments'].fillna(0)
                    clean_df['video_views'] = df.get('Video View Count', 0).fillna(0)  # NEW
                    
                    # 3. Reference Links (Reference ke liye)
                    clean_df['post_url'] = df['Post URL']  # NEW
                    clean_df['thumbnail'] = df.get('Thumbnail URL', '') # NEW
                    
                    # 4. Context (Location)
                    clean_df['location'] = df.get('Location Name', '') # NEW

                    # 5. Post Type Logic
                    def get_type(row):
                        is_vid = str(row.get('Is Video', '')).upper()
                        is_car = str(row.get('Is Carousel', '')).upper()
                        if is_vid == 'YES' or is_vid == 'TRUE': return 'reel'
                        elif is_car == 'YES' or is_car == 'TRUE': return 'carousel'
                        else: return 'post'

                    clean_df['post_type'] = df.apply(get_type, axis=1)

                    # 6. Niche Logic
                    brand = str(df['User Name'].iloc[0]).lower() if not df.empty else 'unknown'
                    found_niche = 'General'
                    for key, val in self.niche_map.items():
                        if key in brand:
                            found_niche = val
                            break
                    clean_df['niche'] = found_niche

                    # 7. Advanced Engagement Score Calculation
                    # Logic: 1 Comment = 5 Likes, 100 Views = 1 Like
                    clean_df['engagement_score'] = (clean_df['likes'] * 1) + \
                                                   (clean_df['comments'] * 5) + \
                                                   (clean_df['video_views'] * 0.05)

                    df_list.append(clean_df)
                    print(f"      -> Loaded & Enriched: {filename}")

                elif 'brand_name' in df.columns:
                    # Mock data support
                    df['engagement_score'] = df['likes'] + df['comments']
                    df['post_url'] = '' # Mock data has no URL
                    df_list.append(df)

            except Exception as e:
                print(f"      -> Error reading {filename}: {e}")
            
        if not df_list:
            raise ValueError("No valid data loaded.")

        return pd.concat(df_list, ignore_index=True)