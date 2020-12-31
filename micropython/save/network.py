try:
  import usocket as socket
except:
  import socket
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

#-----connect to wifi----
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect('B501','123456789')
    while not sta_if.isconnected():
        print('connecting to network...')
print('network config:', sta_if.ifconfig())
#------make Ap -------
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="Duysy", password="123456789")

while ap.active() == False:
  print("Start")

print('Connection successful')
print(ap.ifconfig())

def web_page():
  html = "SQSmartHome"
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  response = web_page()
  conn.send(response)
  conn.close()