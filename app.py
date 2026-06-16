from fastapi import FastAPI
import json

app = FastAPI()

def load_json(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/")
def home():
    return {"status": "API Running"}

@app.get("/property-inquiries")
def property_inquiries(page: int = 1, page_size: int = 100):

    data = load_json("property_inquiries.json")

    start = (page - 1) * page_size
    end = start + page_size

    return {
        "page": page,
        "page_size": page_size,
        "total_records": len(data),
        "data": data[start:end]
    }

@app.get("/property-visits")
def property_visits(page: int = 1, page_size: int = 100):

    data = load_json("property_visits.json")

    start = (page - 1) * page_size
    end = start + page_size

    return {
        "page": page,
        "page_size": page_size,
        "total_records": len(data),
        "data": data[start:end]
    }

@app.get("/weather-data")
def weather_data():

    return load_json("weather_data.json")

@app.get("/market-trends")
def market_trends():

    return load_json("market_trends.json")
