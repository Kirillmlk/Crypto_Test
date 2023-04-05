# import requests
#
#
# def get_info():
#     response = requests.get(url="http://yobit.net/api/3/info")
#
#     with open("info.txt", "w") as file:
#         file.write(response.text)
#
#     return response.text
#
#
# def get_ticker(coin1="btc", coin2="usd"):
#     # response = requests.get(url="http://yobit.net/api/3/ticker/eth_btc-xrp_btc")
#     response = requests.get(url=f"http://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1")
#
#     with open("ticker.txt", "w") as file:
#         file.write(response.text)
#
#     return response.text
#
#
# def get_depth(coin1="btc", coin2="usd", limit=150):
#     response = requests.get(url=f"http://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")
#
#     with open("depth.txt", "w") as file:
#         file.write(response.text)
#
#     bids = response.json()[f"{coin1}_usd"]["bids"]
#
#     total_bids_amount = 0
#     for item in bids:
#         price = item[0]
#         coin_amount = item[1]
#
#         total_bids_amount += price * coin_amount
#
#     return f"Total bids: {total_bids_amount} $"
#
#
# def get_trades(coin1="btc", coin2="usd", limit=150):
#     response = requests.get(url=f"http://yobit.net/api/3/trades/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")
#
#     with open("trades.txt", "w") as file:
#         file.write(response.text)
#
#     total_trade_ask = 0
#     total_trade_bid = 0
#
#     for item in response.json()[f"{coin1}_{coin2}"]:
#         if item["type"] == "ask":
#             total_trade_ask += item["price"] * item["amount"]
#         else:
#             total_trade_bid += item["price"] * item["amount"]
#
#     info = f"[-] TOTAL {coin1} SELL: {round(total_trade_ask, 2)} $\n[+] TOTAL {coin1} BUY: {round(total_trade_bid, 2)} $"
#
#     return info
#
#
# def main():
#     # print(get_info())
#     # print(get_ticker())
#      #print(get_depth(coin1="eth"))
#     # print(get_depth())
#     print(get_trades(coin1="btc"))
#
#
# if __name__ == '__main__':
#     main()

import requests
import time
from datetime import datetime, timedelta

url = "https://api.binance.com/api/v3/ticker/price"
params = {'symbol': 'ETHUSDT'}   # Параметр Eth

response = requests.get(url, params=params)   # Запрос с параметрами


if response.status_code == 200:
    answer = response.json()
    eth_price = float(answer['price'])
    first_price = float(eth_price)     # Сохранение цены с начала запуска
    print(f"Цена с начала запуска: {first_price} USDT")
    start_time = datetime.now()   # Переменная хранит время старта
else:
    print("error")

while True:
    response = requests.get(url, params=params)

    if response.status_code == 200:
        answer = response.json()
        eth_price = float(answer['price'])
        print(f"Текущая цена эфира: {eth_price} USDT")
        current_time = datetime.now()        # Сохранение текущего времени в переменную
        time_diff = current_time - start_time       # Количество прошедших минут
        if eth_price > first_price * 1.01 or eth_price < first_price * 0.99 or time_diff >= timedelta(minutes=60):        # Задаем время
            if eth_price > first_price * 1.01:
                print("Цена Eth выросла на 1% с начала запуска")
            elif eth_price < first_price * 0.99:
                print("Цена Eth опустилась на 1 % с начала запуска")
            else:
                print("Цена Eth не изменилась ")
            start_time = datetime.now()   # Сохраниние текущего времени
            first_price = eth_price
        else:
            pass
    else:
        print("error")

    time.sleep(0.001)
    """Время выполнения функции"""
