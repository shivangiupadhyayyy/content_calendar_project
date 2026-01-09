# src/__init__.py

from .data_loader import DataLoader
from .trends_engine import TrendsEngine
from .analytics import AnalyticsEngine
from .calendar_logic import CalendarGenerator

# This allows you to import everything in main.py like this:
# from src import DataLoader, TrendsEngine, AnalyticsEngine, CalendarGenerator