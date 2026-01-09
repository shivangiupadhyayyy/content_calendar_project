import os
from src.data_loader import DataLoader
from src.trends_engine import TrendsEngine
from src.analytics import AnalyticsEngine
from src.calendar_logic import CalendarGenerator
from datetime import datetime

def main():
    print("=== Automated Content Calendar Generator ===")
    
    # 1. Setup paths
    input_path = 'data/raw_instagram'
    output_path = 'data/output'
    os.makedirs(output_path, exist_ok=True)

    # 2. Load Data
    print("[1/5] Loading Brand Data...")
    try:
        loader = DataLoader(input_path)
        full_data = loader.load_all_brands()
        print(f"      Loaded {len(full_data)} posts from {full_data['brand_name'].nunique()} brands.")
    except Exception as e:
        print(f"Error: {e}")
        return

    # 3. Initialize Engines
    print("[2/5] Initializing Analytics & Trends Engines...")
    analytics = AnalyticsEngine(full_data)
    trends = TrendsEngine(geo='IN') # Setting region to India

    # 4. Generate Calendar
    print("[3/5] Generating Content Logic (This may take a moment)...")
    generator = CalendarGenerator(start_date=datetime.now(), days=30)
    
    calendar_df = generator.create_calendar(full_data, analytics, trends)

    # 5. Export
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    output_file = f"{output_path}/Generated_Content_Calendar_{timestamp}.csv"
    
    print(f"[4/5] Exporting to {output_file}...")
    calendar_df.to_csv(output_file, index=False)
    
    print("[5/5] Done! Process Completed Successfully.")
    print("\nSample Output:")
    print(calendar_df[['Date', 'Brand Name', 'Content Idea']].head())

if __name__ == "__main__":
    main()