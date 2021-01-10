#----import socket-------
try:
  import usocket as socket
except:
  import socket
import network,ujson,utime,machine,uhashlib,urandom

import esp
esp.osdebug(None)
import gc
gc.collect()

from machine import Pin
led = Pin(2, Pin.OUT)
ap = network.WLAN(network.AP_IF)
sta_if = network.WLAN(network.STA_IF)
def slove(request):
    method = request.get("method")
    url = request.get("url")
    data = request.get("data")
    file = loadFileData()
    if str(method).upper() == "POST":
        cookie = str(file.get("account")[0].get("cookie"))
        if url == "/change-password-admin":
            if(cookie == str(request["cookie"])):
                password = data.get("password")
                print(password)
                if len(password) > 8:
                    file["account"][0]["password"]=password
                    print(saveFileData(ujson.dumps(file)))
                    fastBlinkSuccess()
                    return "Success"
                else:
                    return "Passwork length > 9"
            else:
                return "You not login"
        elif url == "/login":
            print("login")
            usernamePost = data.get("username")
            passwordPost = data.get("password")
            usernameFile = file["account"][0].get("username")
            passwordFile = file["account"][0].get("password")
            print(usernamePost,passwordPost,usernameFile,passwordFile)
            if(usernamePost == usernameFile and passwordPost == passwordFile):
                newcookie  = str(random()+random()+random())
                file["account"][0]["cookie"] = newcookie
                print(saveFileData(ujson.dumps(file)))
                fastBlinkSuccess()
                return newcookie
        elif url == "/set-wifi":
            if(cookie == str(request["cookie"])):
                essid = data.get("essid")
                passwork = data.get("passwork")
                file["wifiHome"]["essid"] = essid
                file["wifiHome"]["passwork"] = passwork
                print(saveFileData(ujson.dumps(file)))
                fastBlinkSuccess()
                return str(connectToWifi())
            return "You not login"
        elif url == "/seset-device":
            if(cookie == str(request["cookie"])):
                print("reset maching")
                resetMaching()
        elif url == "/turn-off-ap":
            if(cookie == str(request["cookie"])):
                print(ap.active())
                ap.active(False)
                while ap.active() == True:
                    ap.active(False)
                    print("ap wifi is stop ...")
                print("0k0k")
                return "Success"
            return "You not login"
        elif url == "/turn-on-ap":
            if(cookie == str(request["cookie"])):
                print(ap.active())
                ap.active(True)
                while ap.active() == False:
                    ap.active(True)
                    print("ap wifi is opening...")
                return "Success"
            return "You not login"
        elif url == "/device/add":
            if(cookie == str(request["cookie"])):
                iddevice = data.get("iddevice")
                file["device"][iddevice]={"status":""}
                print(saveFileData(ujson.dumps(file)))
                fastBlinkSuccess()
                return "Success"
            return "You not login"
    elif str(method).upper() == "GET":
        return ujson.dumps(file)
    return "SqSmart"
def random():
    return str(urandom.getrandbits(30))+ str(urandom.getrandbits(30))
def saveFileData(data):
    try:
        file = open ("data.json", "w")
        file.write(data)
        file.close()
    except:
        return False
    return True
def loadFileData():
    #-----open file json -------
    with open('data.json') as json_file:
        data = json_file.read()
    data = ujson.loads(data)
    return data
def resetMaching():
    machine.reset()
def sha1(value):
    m = uhashlib.sha1()
    m.update('b{}'.format(value))
    hashValue = m.digest()
    return hashValue
def fastBlinkError():
    for i in range(20):
        led.on()
        utime.sleep(0.1)
        led.off()
        utime.sleep(0.1)
def fastBlinkSuccess():
    for i in range(3):
        led.on()
        utime.sleep(0.1)
        led.off()
        utime.sleep(0.1)
def slowBlink():
    led.on()
    utime.sleep(1)
    led.off()
    utime.sleep(1)
def connectToWifi():
    start = utime.ticks_us()
    data = loadFileData()
    essid = str(data.get("wifiHome").get("essid"))
    passwork = str(data.get("wifiHome").get("passwork"))
    #{}
    sta_if.active(True)
    sta_if.connect(essid,passwork)
    while not sta_if.isconnected():
        slowBlink()
        if((utime.ticks_us() - start) > 10**6*15):
            fastBlinkError()
            break
        print('connecting to network...',essid,passwork)
    print('network config:', sta_if.ifconfig())
    return sta_if.ifconfig()
    
#------make ap wifi --------
data = loadFileData()
username = str(data.get("account")[0].get("username"))
password = str(data.get("account")[0].get("password")) # passwork len > 8
#{}
ap.active(True)
ap.config(essid = username, password = password )
while ap.active() == False:
    print("ap wifi is opening...")
print("AP successful  ",ap.ifconfig())
#---------------------------------
#-----------connect wifi ---------
connectToWifi()
#-------------------------------------

led.off()
try:
    print("start server")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        print(request)
        try:
            data = ujson.loads(str(request.decode("UTF-8"))) # json data mothod,url,data....
            print('Content = {}'.format(data))
            response = slove(data)
        except:
            with open('index.html') as html:
                response = html.read()
        conn.send(response)
        conn.close()
except:
    resetMaching()

