import urandom,uhashlib

def sha1(value):
    m = uhashlib.sha1()
    m.update('b{}'.format(value))
    hashValue = m.digest()
    return hashValue
def random():
    return str(urandom.getrandbits(30))+ str(urandom.getrandbits(30))

print(sha1(random()))