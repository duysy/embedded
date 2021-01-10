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
import select

ap = network.WLAN(network.AP_IF)
sta_if = network.WLAN(network.STA_IF)

def resetMaching():
    machine.reset()

def connectToWifi():
    start = utime.ticks_us()
    essid = "Iphone11"
    passwork = "namvanghia"
    sta_if.active(True)
    sta_if.connect(essid,passwork)
    while not sta_if.isconnected():
        if((utime.ticks_us() - start) > 10**6*15):
            break
        print('connecting to network...',essid,passwork)
    print('network config:', sta_if.ifconfig())
    return sta_if.ifconfig()
    
connectToWifi()

try:
    print("start server")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    poll = select.poll()
    poll.register(s, select.POLLIN)
    while True:
        print("Helllo")
        events = poll.poll(100)
        if events:
            print("Hello")
            conn, addr = s.accept()
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            conn.send(request)
            conn.close()
except:
   resetMaching()

