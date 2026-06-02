import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print(data)

nav_df = pd.DataFrame(data["data"])

nav_df.to_csv("data/raw/hdfc_nav.csv", index=False)

print("CSV file saved successfully!")