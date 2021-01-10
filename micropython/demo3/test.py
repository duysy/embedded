import socket
import time
import json,random
HOST = '192.168.1.42'  # The server's hostname or IP address
PORT = 80        # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # data = {
    #     "method":"POST",
    #     "url":"/change-password-admin",
    #     "cookie":"106293043885906851010074510371038899934636562792395092483",
    #     "data":{
    #         "password":"adminsmarthome"
    #     }
    # }
    # data = {
    #     "method":"POST",
    #     "url":"/set-wifi",
    #     "cookie":"106293043885906851010074510371038899934636562792395092483",
    #     "data":{
    #         "essid": "Iphone11",
    #         "passwork": "namvanghia"
    #     }
    # }
    # data = {
    #     "method":"POST",
    #     "url":"/login",
    #     "cookie":"jhkjhjkh",
    #     "data":{
    #         "username":"adminsmarthome",
    #         "password":"adminsmarthome"
    #     }
    # }
    # data = {
    #     "method":"POST",
    #     "url":"/seset-device",
    #     "cookie":"106293043885906851010074510371038899934636562792395092483",
    # }
    data = {
        "method":"POST",
        "url":"/device/add",
        "cookie":"106293043885906851010074510371038899934636562792395092483",
        "data":{
            "iddevice": "ADB-h8dhda8-{}".format(random.randint(0,10000))
        }
    }
    # data = {
    #     "method":"POST",
    #     "url":"/turn-off-ap",
    #     "cookie":"106293043885906851010074510371038899934636562792395092483",
    # }
    data = {
        "method":"POST",
        "url":"/turn-on-ap",
        "cookie":"106293043885906851010074510371038899934636562792395092483",
    }

    # data = {
    #     "method":"GET",
    #     "url":"/login",
    #     "cookie":"jhkjhjkh",
    # }
    data = "[[{}]]".format(str(json.dumps(data))).encode()
    print(data)
    s.sendall(data)
    data = s.recv(1024)
    print('Received', repr(data))
     