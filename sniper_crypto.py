import requests

import pandas as pd

import os





def send_telegram_alert(msg):

   

    TOKEN = os.environ.get("TOKEN_TELEGRAM") #token bot telegram

   

    CHAT_ID = os.environ.get("CHAT_ID") # ID main account telegram

   

    url_bot = f"https://api.telegram.org/bot{TOKEN}/sendMessage" # url connection to sever

   

    msg_bot = f"Bottom {msg}" # message from telegram bot to main account

   

    pay_load = {"chat_id":CHAT_ID ,"text": msg_bot} #

   

    try:

        response = requests.post(url_bot , json= pay_load) # check API sever telegram

        if response.status_code == 200: #check valid status code = 200 is correct

            print("Connection succes")

        else:

            print(f"Error from to the sever {response.status_code}")

    except requests.exceptions.RequestException as e :

        #Failed connection to sever

        print(f"Cable internet of international get trouble {e}")

    return msg_bot

   

   

     

def get_price_crypto(coin_id):

    url = "https://api.coingecko.com/api/v3/simple/price" # link api web coingeko.com

    pay_load_coin = {"ids":coin_id, "vs_currencies": "usd"} # dictionary contain name and value need to find

    try:

        response_url_coin_id = requests.get(url , params= pay_load_coin)  # waiting sever response

        if response_url_coin_id.status_code == 200: # check valid code = 200

            print("connection success to the API market price coingecko.com")

            raw_data = response_url_coin_id.json() # craw raw data with json

           

            price_coin_id = raw_data[coin_id]["usd"] # filter data to find name and value of Bitcoin

           

            return price_coin_id # return the price of bitcoin

        else:

            print(f"URL get trouble can't connectional {response_url_coin_id.status_code}") # if status code != 200 print display what trouble got

            return None

    except requests.exceptions.RequestException as e : # trap internet global if have problem

        print(f"Cable Internet international have trouble can't connection {e}")

        return None

if __name__ == "__main__": # Logic command center

    print("🤖 Đang khởi động Bot Bắn Tỉa Bitcoin... (Starting Bitcoin Sniper Bot...)")

    list_coin = ["bitcoin" , "ethereum" ,"solana"] # create a list contain three coin you want to search price

    bottom_fishing = {

        "bitcoin": 65000,  # Nếu rớt dưới 65k thì báo động

        "ethereum": 2500,  # Nếu rớt dưới 2k5 thì báo động

        "solana": 80       # Nếu rớt dưới 80 thì báo động

    }

    for item in list_coin:

        price_coin = get_price_crypto(item)

       

        if price_coin :

            trap_coin = bottom_fishing[item]

            print(f"price {item} is : {price_coin} USD , Bottom {trap_coin}")

            if price_coin < trap_coin :

                warning_msg = f"🚨 {item.upper()} RỚT ĐÁY! Giá: {price_coin}. MUA NGAY"

                send_telegram_alert(warning_msg)

        else:


            print("skip it , hold ")
