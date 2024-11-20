from BinaryEncryption import Cryptographic_Processor

P=eval(input("Open key: "))
ec=Cryptographic_Processor(131)
ec.setEncrypt(P)
try:
    while True:
        C=ec.Encrypt(input("Message: "))
        print(C)
except:
    pass