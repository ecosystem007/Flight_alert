import yaml
from flight_scraper import get_flight_price
from alert_engine import send_alert

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

dep = config["from"]
arr = config["to"]
date = config["date"]
threshold = config["price_limit"]

print(f"📡 正在查询 {dep} → {arr} 日期：{date}")

price = get_flight_price(dep, arr, date)
if price:
    print(f"🎯 最低价为：¥{price}")
    if price < threshold:
        send_alert(f"{dep} → {arr}，{date}，当前最低价 ¥{price}", config)
    else:
        print("😴 未低于阈值，无需提醒")
else:
    print("⚠️ 抓取失败或无航班")
