# 📅 Automated Trend-Driven Content Calendar Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)

A smart, data-engineering solution that automates social media strategy by generating a **30-day content calendar** using a hybrid of **Real-Time Google Trends** and **Historical Instagram Performance**.

> **Problem Solved:**  
> Marketers struggle to balance trending topics with evergreen content.  
> This system uses Python logic to decide what to post, when to post, and which format (Reel / Carousel) to use — purely data-driven.

---

## 🚀 Key Features

### 🧠 Hybrid Logic Engine
- 60% Trend-Based: Uses Google Trends to capture real-time rising topics.
- 40% Historical Repurposing: Reuses past viral Instagram content intelligently.

### 📂 Smart Data Ingestion
- Accepts raw CSV exports from Instagram scrapers (e.g., IG Exporter).
- Auto-cleans column names, date formats, and missing values.

### 📈 Advanced Scoring Algorithm
- Calculates a Weighted Engagement Score.
- Gives higher weight to video views and comments.

### 🔗 Actionable Output
- Adds reference URLs of original viral posts.
- Suggests location tags based on historical geo-performance.

---

## 📂 Project Structure

```
content_calendar_project/
│
├── data/
│   ├── raw_instagram/
│   └── output/
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── trends_engine.py
│   ├── analytics.py
│   └── calendar_logic.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```
git clone https://github.com/yourusername/trend-driven-calendar.git
cd trend-driven-calendar
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

Or manually:
```
pip install pandas numpy pytrends openpyxl
```

### 3. Add Instagram Data
- Export posts as CSV using IG Exporter
- Place files in:
```
data/raw_instagram/
```

---

## ⚡ How to Run

```
python main.py
```

---

## 📊 Sample Output

| Date       | Brand  | Content Type | Content Idea                         | Source          |
|------------|--------|--------------|--------------------------------------|-----------------|
| 2026-01-10 | Snitch | Reel         | Trend Alert: Oversized tees          | Google Trends   |
| 2026-01-11 | Snitch | Carousel     | Repurpose Hit: Summer styling tips   | Historical Data |
| 2026-01-12 | Zomato | Reel         | Viral Food Capsule meme              | Google Trends   |

---

## 🔮 Future Improvements
- GPT-based caption generation
- Streamlit dashboard
- Hashtag volume optimizer

---

## 👨‍💻 Author
Shivangi Upadhyay
