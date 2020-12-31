from array import array
import ujson,utime

for i in range(200000):
    data = '{"lon":"'+str(i)+'"}'
    file = open ("data.txt", "w")
    file.write(data)
    f = open('data.txt',"r")
    c = f.readline()
    print(ujson.loads(c))
    utime.sleep(1)