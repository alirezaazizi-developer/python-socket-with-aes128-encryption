'''
import socket

__socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM) # tcp connection
print'nice'
__socket.connect(('192.0.0.1',80))
print 'connected'
result = __socket.recv(1024)
print result
__socket.close()
'''

import pyaes
import os
from socket import *
import tkinter # graphical libaries
import base64
'''
key_128 = os.urandom(16)
print(key_128)
aes = pyaes.AESModeOfOperationCTR(key_128)
plaintext = "hello that is big exprement of python power to today you should be jadge it is jadgement day"
ciphertext = aes.encrypt(plaintext)
cipher = ciphertext

print(cipher)
#en = cipher.decode()
#print(en)
aesdec = pyaes.AESModeOfOperationCTR(key_128)
a = aesdec.decrypt(cipher)
print(a)

print(repr(a.decode()))
'''
'''
top = tkinter.Tk()
# Code to add widgets will go here...


tkinter.Label(top , text = a).pack()
top.mainloop()
'''

'''
Key = "Key_is_python_AH"

aes = pyaes.AESModeOfOperationCTR(Key)
'''
s =socket(2,1)
s.connect(('192.168.1.100',8080))
data = s.recv(1024)
print(data)
data = base64.b64decode(data)
print(data)
key = 'hello123P{/e3sc}'.encode()
aes = pyaes.AESModeOfOperationCTR(key)
data = aes.decrypt(data)
#data = data.decode()
print('decrypted message is '+data.decode())
s.close()