from array import array
import ujson,utime

data = '{"lon":[{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"},{"name":"duysy"}]}'
file = open ("data.txt", "w")
file.write(data)

start = utime.ticks_us()
f = open('data.txt',"r")
c = f.readline()
print(c)
print(ujson.loads(c).get("lon")[20])
print(ujson.loads(c).get("lon")[20])
print(ujson.loads(c).get("lon")[20])
print(ujson.loads(c).get("lon")[20])
print(ujson.loads(c).get("lon")[20])
print((utime.ticks_us()-start)/1000000)
print(utime.ticks_us())