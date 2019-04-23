import pdb
import hashlib

#print(sys.path(WebDriverWait))

m = hashlib.md5()
print(m)
pdb.set_trace()
m.update(b'itcast')
print(m.hexdigest())
