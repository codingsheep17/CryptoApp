#crypto app using free coincap api
import requests
import sys
import time

class CryptoApp:
    def __init__(self):
        self.welcome()

    def welcome(self):
        print("Welcome To Crypto App")
        for self.x in range(4, -1,-1):
            self.seconds = self.x % 60
            print(f"{self.seconds:02} wait till app is loading...", end= '\r')
            time.sleep(1)
        self.api_working()
        
    def api_working(self):
        self.api_key = "dcc2d442641f5f38a955f647ad1bbfe2fd5dd627a8ae78ac7c86f56f30e6f681"
        self.api_url = f"https://rest.coincap.io/v3/assets?apiKey={self.api_key}"
        self.data_req = requests.get(self.api_url)
        self.data = self.data_req.json()
        self.user_menu()

    def top_10_curriencies(self):
        self.idx = 0
        self.coin_num = 1
        for self.i in range(1,11):
            self.coin_name = self.data["data"][self.idx]["name"]
            self.coin_volume_24hr = self.data["data"][self.idx]["volumeUsd24Hr"]
            self.coin_price_usd = self.data["data"][self.idx]["priceUsd"]
            self.coin_symbol = self.data["data"][self.idx]["symbol"]
            self.coin_market_cap_ud = self.data["data"][self.idx]["marketCapUsd"]
            self.coin_percent_24hr = self.data["data"][self.idx]["changePercent24Hr"]    

            # for coin_volume
            if float(self.coin_volume_24hr) >= 1_000_000_000:
                self.formatted_volume = f"${float(self.coin_volume_24hr)/ 1_000_000_000:.2f} B"
            elif float(self.coin_volume_24hr) >= 1_000_000:
                self.formatted_volume = f"${float(self.coin_volume_24hr) / 1_000_000:.2f} M"
            else:
                self.formatted_volume = f"${float(self.coin_volume_24hr):,.2f}"

            #for coin 24 hour precentage
            self.symbol = "🔼" if float(self.coin_percent_24hr) >= 0 else "🔽"

            print(f"{self.coin_num}:{self.coin_name}-{self.coin_symbol}")
            print(f"💵 Price:≈ ${float(self.coin_price_usd):,.2f}")
            print(f"🏦 Market Cap {float(self.coin_market_cap_ud):,.2f}")
            print(f"🔁 24 Hour Volume: {self.formatted_volume}")
            print(f"📈 24 Hour Change: {float(self.coin_percent_24hr):,.2f}{self.symbol}")
            print("________________________________")
            self.idx+=1
            self.coin_num+=1

    def search_coin(self):
        try:
            self.coin_name = str((input("Enter The Name of Coin --> "))).lower()
            self.single_coin_url = f"https://rest.coincap.io/v3/assets/{self.coin_name}?apiKey={self.api_key}"
            self.get_request = requests.get(self.single_coin_url)
            self.single_coin_data = self.get_request.json()

            self.coin = self.single_coin_data["data"]
            if self.coin["id"] == self.coin_name or self.coin["symbol"].lower() == self.coin_name.lower():
                self.single_coin_name = self.coin["name"]
                self.single_coin_volume_24hr = self.coin["volumeUsd24Hr"]
                self.single_coin_price_usd = self.coin["priceUsd"]
                self.single_coin_symbol = self.coin["symbol"]
                self.single_coin_market_cap_ud = self.coin["marketCapUsd"]
                self.single_coin_percent_24hr = self.coin["changePercent24Hr"] 

                if float(self.single_coin_volume_24hr) >= 1_000_000_000:
                    self.single_formatted_volume = f"${float(self.single_coin_volume_24hr)/ 1_000_000_000:.2f} B"
                elif float(self.single_coin_percent_24hr) >= 1_000_000:
                    self.single_formatted_volume = f"${float(self.single_coin_percent_24hr) / 1_000_000:.2f} M"
                else:
                    self.single_formatted_volume = f"${float(self.single_coin_percent_24hr):,.2f}"

                self.symbol_single_coin = "🔼" if float(self.single_coin_percent_24hr) >= 0 else "🔽"

                print(f"-->{self.single_coin_name}-{self.single_coin_symbol}")
                print(f" 💵 Price:≈ ${float(self.single_coin_price_usd):,.2f}")
                print(f" 🏦 Market Cap {float(self.single_coin_market_cap_ud):,.2f}")
                print(f" 🔁 24 Hour Volume: {self.single_formatted_volume}")
                print(f" 📈 24 Hour Change: {float(self.single_coin_percent_24hr):,.2f}{self.symbol_single_coin}")
            else:
                print("Coin Not Found")

        except Exception as single_coin:
            print(f"Error {single_coin}")

    def view_global_market_status(self):
        try:
            self.global_market_url = f"https://rest.coincap.io/v3/assets?apiKey={self.api_key}"
            self.global_data_fetch = requests.get(self.global_market_url)
            self.data_global_market = self.global_data_fetch.json()

            self.total_global_market_cap = 0.0
            self.total_global_24hr_volume = 0.0

            for self.global_final in self.data_global_market["data"]:
                self.total_global_market_cap += float(self.global_final["marketCapUsd"])
                self.total_global_24hr_volume += float(self.global_final["volumeUsd24Hr"])
            print(f"Total Market Cap --> {self.total_global_market_cap:,.2f}")
            print(f"Total Market 24Hr Volume --> {self.total_global_24hr_volume:,.2f}")

        except Exception as global_market:
            print(f"Error Occured in Global Market {global_market}")

    def change_currency(self):
        pass

    def user_menu(self):
        while True:
            try:     
                self.user_input = int(input("""
==== CRYPTO TRACKER ====
1. 🔟 Top 10 Cryptocurrencies
2. 🔍 Search Specific Coin
3. 📈 View Global Market Stats
4. 🌐 Change Currency (Default: USD)
5. ❌ Exit --> """))
                if self.user_input == 1:
                    self.top_10_curriencies()
                elif self.user_input == 2:
                    self.search_coin()
                elif self.user_input == 3: 
                    self.view_global_market_status()
                elif self.user_input == 4:
                    self.change_currency()
                elif self.user_input == 5:
                    print("Thanks for using my app")
                    sys.exit()
                else:
                    print("Entered Number not in range")
            except Exception as e:
                print(f"Error Occured {e}")

crypto_app = CryptoApp()