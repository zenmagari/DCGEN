import requests, os, ctypes; ctypes.windll.kernel32.SetConsoleTitleW(f"DCGEN")

url = "https://api.discord.gx.games/v1/direct-fulfillment"
billurl = "https://discord.com/billing/partner-promotions/1180231712274387115/"

payload = {"partnerUserId": "21b3bb0e1c0612e6d59b71212e463f2b0c1585120e9431fae57554ddc834148c"}
headers = {
    "authority": "api.discord.gx.games",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.opera.com",
    "referer": "https://www.opera.com/",
    "sec-ch-ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
}

def cbanner():
    banner = '''


  \033[95m  ▄▀▀█▄▄   ▄▀▄▄▄▄   ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄ 
  \033[85m █ ▄▀   █ █ █    ▌ █        ▐  ▄▀   ▐ █  █ █ █ 
  \033[75m ▐ █    █ ▐ █      █    ▀▄▄   █▄▄▄▄▄  ▐  █  ▀█ 
  \033[65m   █    █   █      █     █ █  █    ▌    █   █  
  \033[66m  ▄▀▄▄▄▄▀  ▄▀▄▄▄▄▀ ▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄   ▄▀   █   
  \033[67m █     ▐  █     ▐  ▐         █    ▐   █    ▐   
  \033[68m ▐        ▐                  ▐        ▐       
  '''
    print(banner)

def main():
    cbanner()
    value = int(input("   VALUE: "))
    for i in range(1, value + 1):
        response = requests.request("POST", url, json=payload, headers=headers)
        try:
            api = response.json()
            token = api.get("token")

            if token:
                billtoken = f"{billurl}/{token}"
                print(f"   GENERATED: {i}\r", end="", flush=True)
                with open("token.txt", "a") as ftoken:
                    ftoken.write(f"{billtoken}\n\n")

        except (KeyboardInterrupt, Exception) as e:
            print(f"Error occurred: {str(e)}")

    input()

if __name__ == "__main__":
    main()
