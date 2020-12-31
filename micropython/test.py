import socket
import time
import json,random
HOST = '192.168.4.1'  # The server's hostname or IP address
PORT = 80        # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # data = {
    #     "method":"POST",
    #     "url":"/change-password-admin",
    #     "cookie":"395575716486103612877167277639078691505195626225957641",
    #     "data":{
    #         "password":"adminsmarthome"
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
    data = {
        "method":"POST",
        "url":"/set-wifi",
        "cookie":"395575716486103612877167277639078691505195626225957641",
        "data":{
            "essid": "B401",
            "passwork": "123456789"
        }
    }
    # data = {
    #     "method":"POST",
    #     "url":"/seset-device",
    #     "cookie":"395575716486103612877167277639078691505195626225957641",
    # }
    # data = {
    #     "method":"POST",
    #     "url":"/device/add",
    #     "cookie":"395575716486103612877167277639078691505195626225957641",
    #     "data":{
    #         "iddevice": "ADB-h8dhda8-{}".format(random.randint(0,10000))
    #     }
    # }

    # data = {
    #     "method":"POST",
    #     "url":"/turn-off-ap",
    #     "cookie":"395575716486103612877167277639078691505195626225957641",
    # }

    # data = {
    #     "method":"GET",
    #     "url":"/login",
    #     "cookie":"jhkjhjkh",
    # }
    data = str(json.dumps(data)).encode()
    print(data)
    s.sendall(data)
    data = s.recv(1024)
    print('Received', repr(data))
     