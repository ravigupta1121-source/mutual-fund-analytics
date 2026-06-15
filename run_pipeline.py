"""
Master Pipeline Script
Mutual Fund Analytics Project
"""

import os

print("Starting Mutual Fund Analytics Pipeline...")

# Run project scripts
os.system("python live_nav_fetch.py")
os.system("python data_cleaning.py")
os.system("python database_loader.py")
os.system("python csv_analysis.py")

print("Pipeline Completed Successfully!")