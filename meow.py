import requests
import json
import urllib.parse
import re
import time

# Fungsi untuk mengekstrak username dari auth_data
def extract_username(auth_data):
    decoded_data = urllib.parse.unquote(auth_data)
    match = re.search(r'"username\\?":\\?"([^"]+)"', decoded_data)
    if match:
        return match.group(1)
    return "Unknown"

# Fungsi untuk mengekstrak nilai dari bonus
def extract_bonus(bonus_list, bonus_type):
    for bonus in bonus_list:
        if bonus.get("type") == bonus_type:
            return bonus.get("value", "N/A")
    return "N/A"

# Fungsi utama untuk menjalankan script dengan delay dan countdown
def main():
    print("=========SUPERMEOW BOT BY KUTUJAYA=============")
    delay = float(input("Masukan delay (dalam detik): "))
    print("===============================================")

    while True:
        # Membaca data dari file data.json
        with open('data.json', 'r') as file:
            data_list = json.load(file)

        # Mengatur header untuk permintaan
        headers = {
            "Accept": "application/json; indent=2",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Content-Length": "0",
            "Content-Type": "application/json",
            "Origin": "https://lfg.supermeow.vip",
            "Pragma": "no-cache",
            "Priority": "u=1, i",
            "Referer": "https://lfg.supermeow.vip/",
            "Sec-Ch-Ua": "\"Microsoft Edge\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\", \"Microsoft Edge WebView2\";v=\"125\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
        }

        # Mengirim permintaan POST untuk setiap auth_data di dalam data_list
        for auth_data in data_list:
            url = f"https://api.supermeow.vip/meow/claim?telegram=1600062444&is_on_chain=false&{auth_data}"
            response = requests.post(url, headers=headers)
            
            if response.ok:
                raw_response = response.json()  # Mengubah respons menjadi JSON
                username = extract_username(auth_data)
                
                # Mendapatkan data yang diperlukan dari respons JSON
                balance = raw_response.get("balance", "N/A")
                claimable = raw_response.get("claimable", "N/A")
                last_claim = raw_response.get("last_claim", "N/A")
                mining_speed = raw_response.get("mining_speed", "N/A")
                max_time = raw_response.get("max_time", "N/A")
                
                # Mengambil nilai bonus dari daftar bonus
                bonus_list = raw_response.get("bonus", [])
                check_balance = extract_bonus(bonus_list, "check_balance")
                check_in = extract_bonus(bonus_list, "check_in")
                
                # Mencetak informasi dalam format yang diminta
                print("=========SUPERMEOW BOT BY KUTUJAYA=============")
                print(f"USER NAME: {username}")
                print(f"BALANCE: {balance}")
                print(f"claimable: {claimable}")
                print(f"last_claim: {last_claim}   | mining_speed: {mining_speed}    | max_time: {max_time}")
                print(f"bonus: check_balance: {check_balance} | check_in: {check_in}")
                print("=================================================")
            else:
                print(f"Failed to retrieve data: {response.status_code}")
        
        # Countdown setelah script berjalan dan sebelum mengulang
        for i in range(int(delay), 0, -1):
            print(f"MENGULANGI SCRIPT: {i} detik", end='\r')
            time.sleep(1)

if __name__ == "__main__":
    main()