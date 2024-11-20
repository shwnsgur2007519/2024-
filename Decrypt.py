from BinaryEncryption import Cryptographic_Processor
import time
# 2053
# 131
# 7
dc=Cryptographic_Processor(131)
st=time.time()

P=dc.makePublic()
print("Open key: ",P)
print(time.time()-st)
try:
    while True:
        C=eval(input("Cryptography: "))
        M=dc.Decrypt(C)
        print(M)
except:
    pass