# Automated Trend-Driven Content Calendar Generator

## Problem Statement
Marketing agencies manage multiple brands and struggle to manually balance "trending" topics with "evergreen" content. This system automates the strategy phase by merging live search data with historical performance data.

## Approach
1. **Ingestion:** Reads offline CSVs of past Instagram performance.
2. **Analysis:** Calculates the highest engagement format (Reel vs Post) per brand.
3. **Trends:** Pings Google Trends (via `pytrends`) to find rising queries in the brand's niche.
4. **Logic:** - 60% of content is Trend-based (Uses rising queries).
   - 40% is Historical (Repurposes top-performing themes).
   - Enforces format diversity (Mix of Reels, Carousels, Stories).

## Setup & Run
1. Install dependencies: `pip install -r requirements.txt`
2. Generate dummy data: `python generate_mock_data.py`
3. Run the generator: `python main.py`
4. Check `data/output/` for the CSV result.

## Limitations
- **Google Trends API:** The `pytrends` library uses an unofficial API which may be rate-limited by Google. The code includes a fallback "Mock Mode" if this happens.
- **Captioning:** Currently uses a rule-based template. For production, integrate OpenAI API.