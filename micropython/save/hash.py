import uhashlib
m = uhashlib.sha1()
m.update('b{}'.format("dhsadsahddsadsagashdsadasdaaddaddsdsadsadag"))
c= m.digest()
print(c)