from fastapi import FastAPI, HTTPException
import pandas as pd
import os

app = FastAPI()

# Path to CSV file (ensure it’s in the same directory or adjust accordingly)
CSV_FILE = "G:/Work/Chetu W4.52 Fast API Mini Apps/MiniAPIs/AirQuality.csv"

@app.get("/airquality/")
def get_air_quality_records():
    try:
        if not os.path.exists(CSV_FILE):
            raise HTTPException(status_code=404, detail="CSV file not found.")

        # Read CSV
        # df = pd.read_csv(CSV_FILE, sep="\t", engine="python")
        df = pd.read_csv(CSV_FILE, sep=",", engine="python", encoding="utf-8")
        print(df.head())  # Debug: print first few rows

        # Convert to JSON
        records = df.head(10).fillna("").to_dict(orient="records")
        return {"records": records}
    
    except Exception as e:
        print("ERROR:", e)  # 🔍 Debug output
        raise HTTPException(status_code=500, detail=str(e))

