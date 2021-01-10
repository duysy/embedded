from array import array
import ujson,utime

for i in range(10):
    data = '{"lon":"'+str(i)+'"}'
    file = open ("data.txt", "w")
    file.write(data)
    file.close()
    with open('data.txt') as json_file:
        c = json_file.read()
    print(ujson.loads(c))
    