import hashlib

#_input = input('DATA: ').encode()

num = 1

_input = str(num).encode()

print(hashlib.sha1(_input).hexdigest())