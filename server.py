#is socket server file use for response to client
from socket import *
import time

import pyaes
import hashlib
import base64
# import os
# from sys import path
import urllib3
import ctypes
from crypto import Random

arr = [1,2,3,4,5,6,7,78,8]
res = Random.new(arr)
print(res)
# ctypes.

s =socket(2,1)
s.bind(('192.168.1.100',1234))
s.listen(5)

s.settimeout(10000)

print ("runing ...\n")

# data = 'hello world alireza'.encode()
# hashcode = hashlib.shake_128(data)
aes = pyaes.AESModeOfOperationCTR('hello123P{/e3sc}'.encode())
en = aes.encrypt('hello world that is your chance for live better than another people for live better')

while True:

	c , addr = s.accept()

	print ("connected to " + str(addr))

	c.send(base64.b64encode(en))
	time.sleep(5)
	

c.close()


# os.re