import random
from BasicOperations import *

class Cryptographic_Processor:


    def __init__(self,l):
        self.__l=l

    # 기본 연산
    def pow(self, a, b):
        return pow(a,b,self.__l)

    # 문자-숫자 변환함수
    def ttn(self,t):
        n=0
        for char in t:
            n*=4294967296
            n+=ord(char)
        return n
    def ntt(self,n):
        t=""
        while n:
            t=chr(n%4294967296)+t
            n//=4294967296
        return t

    # 서로소 만들기
    @staticmethod
    def gcd(p,q):
        if q==0: return p
        else: return Cryptographic_Processor.gcd(q,p%q)
    def make_exp(self):
        k=random.randint(0,1<<self.__l)
        while Cryptographic_Processor.gcd(k,(1<<self.__l)-1)!=1: #키에 따라 달라짐.
            k=random.randint(0,1<<self.__l)
        return k
    def make_safe_openkey(self):
        k=self.make_exp()
        safekey=3 # 아직 구하지 못한 생성원
        return self.pow(safekey,k)
    
    # 공기키 만들기
    def makePublic(self):
        self.__n=random.randint(1<<(self.__l-1),1<<self.__l)
        self.__p1=self.make_safe_openkey()
        # import time
        # stt=time.time()
        self.__p2=self.pow(self.__p1,self.__n)
        # print(time.time()-stt)
        return self.__p1,self.__p2
    
    # 암호화
    def setEncrypt(self,p:(tuple)):
        self.__p1=p[0]
        self.__p2=p[1]
    def encrypt(self,M:str):
        M=self.ttn(M)
        self.__m=self.make_exp()
        self.__c1=self.pow(self.__p2,self.__m)^M
        self.__c2=self.pow(self.__p1,self.__m)
        # print(f"Encrypted by (p1,p2,m,M):{self.__p1,self.__p2,self.__m,M}")
        return self.__c1,self.__c2
    def Encrypt(self,M:str):
        l=self.__l//32
        n=(len(M)-1)//l+1
        tu=tuple()
        for i in range(n):
            tu+=self.encrypt(M[l*i:l*(i+1)]),
        return tu

    # 복호화
    def setDecrypt(self,c:(tuple)):
        self.__c1=c[0]
        self.__c2=c[1]
    def decrypt(self):
        return self.ntt(self.__c1^self.pow(self.__c2,self.__n))
    
    def Decrypt(self,C):
        t=str()
        for c in C:
            self.setDecrypt(c)
            t+=self.decrypt()
        return t
    

    # 디버깅
    def Debugn(self):
        print("n: ",self.__n)
        return self.__n
    def Debugm(self):
        print("m: ",self.__m)
        return self.__m


# __name__="__Encrypt__"
# __name__="__Decrypt__"


if __name__=="__Encrypt__":
    l=47
    P=eval(input())
    ec=Cryptographic_Processor(l)
    ec.setEncrypt(P)
    try:
        while True:
            C=ec.Encrypt(input())
            print(C)
    except:
        pass

if __name__=="__Decrypt__":
    l=47
    dc=Cryptographic_Processor(l)
    P=dc.makePublic()
    print(P)
    try:
        while True:
            C=eval(input())
            M=dc.Decrypt(C)
            print(M)
    except:
        pass


if __name__=="__main__":
    import time
    M=23434
    l=2053
    st=time.time()
    dc=Cryptographic_Processor(l)
    ec=Cryptographic_Processor(l)
    P=dc.makePublic()
    print(f"MakePublic time: {time.time()-st}")
    st=time.time()
    ec.setEncrypt(P)
    C=ec.Encrypt(str(M))
    print(f"Enctypt time: {time.time()-st}")
    st=time.time()
    M_res=dc.Decrypt(C)
    print(f"Decrypt time: {time.time()-st}")
    # print(P,C,M_res)
    # n=dc.Debugn() # n
    # m=ec.Debugm() # m
    print(M_res)


    # print("p2: ",ec.pow(P[0],n))
    # print("c1: ",M^ec.pow(P[1],m))
    # print("c2: ",ec.pow(P[0],m))
'''
#'''