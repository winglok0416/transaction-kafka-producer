from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import json


def convert_rows_to_records(rows: [WebElement]):
    result = []
    for row in rows:
        elements = row.find_elements(By.CLASS_NAME, "latest-real-time-trades__cell")
        time = elements[0].text
        price = float(elements[1].text.replace("$ ", ""))
        volume = int(elements[2].text.replace(",", ""))
        result.append(convert_record_to_json(time, price, volume))
    return result


def convert_record_to_json(time: str, price: str, volume: str):
    return json.dumps({
        "time": time,
        "price": float(price),
        "volume": int(volume)
    })

def read_records_from_txt(path: str):
    with open(path) as f:
        return [line for line in f]