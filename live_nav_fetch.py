import pandas as pd
import requests

funds = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for name, code in funds.items():
    url = f"https://api.mfapi.in/mf/{code}"
    data = requests.get(url).json()

    df = pd.DataFrame(data["data"])
    df.to_csv(f"data/raw/{name}_nav.csv", index=False)

    print(f"{name} saved")