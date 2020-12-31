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

def slove(request):
    method = request.get("method")
    url = request.get("url")
    data = request.get("data")
    file = loadFileData()
    if str(method).upper() == "POST":
        cookie = str(file.get("account")[0].get("cookie"))
        if(cookie==data["cookie"]):
            if url == "/change-password-admin":
                file["account"][0]["password"]=data["password"]
        else:
            if url == "/login":
                usernamePost = data.get("username")
                passwordPost = data.get("password")
                usernameFile = file["account"][0].get("username")
                passwordFile = file["account"][0].get("password")
                if(usernamePost == usernameFile and passwordPost == passwordFile):
                    newcookie  = str(sha1(random()))
                    file["account"][0]["cookie"] = newcookie
                    saveFileData(ujson.dumps(file))
                    return newcookie

    
    return "hello"
def random():
    return str(urandom.getrandbits(30))+ str(urandom.getrandbits(30))
def saveFileData(data):
    try:
        file = open ("data.json", "w")
        file.write(data)
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
#------make ap wifi --------
data = loadFileData()
username = str(data.get("account")[0].get("username"))
password = str(data.get("account")[0].get("password")) # passwork len > 8
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid = username, password = password )
while ap.active() == False:
    print("ap wifi is opening...")
print("AP successful  ",ap.ifconfig())
#---------------------------------
#-----------connect wifi ---------
essid = str(data.get("wifiHome").get("essid"))
passwork = str(data.get("wifiHome").get("passwork"))
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect(essid,passwork)
    while not sta_if.isconnected():
        utime.sleep(2)
        print('connecting to network...',essid,passwork)
print('network config:', sta_if.ifconfig())
#-------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    data = ujson.loads(str(request.decode("UTF-8"))) # json data mothod,url,data....
    print('Content = {}'.format(data))
    conn.send(slove(data))
    conn.close()

