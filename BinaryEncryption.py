import random
from BasicOperations import *

class Cryptographic_Processor:


    def __init__(self,l):
        self.__l=l
        self.safekey=3

    # 기본 연산
    def pow(self, a, b):
        return pow(a,b,self.__l)

    # 문자-숫자 변환함수
    def ttn(self,t):
        n=0
        for char in t:
            n*=128
            n+=ord(char)
        return n
    def ntt(self,n):
        t=""
        while n:
            t=chr(n%128)+t
            n//=128
        return t

    # 서로소 만들기
    @staticmethod
    def gcd(p,q):
        if q==0: return p
        else: return Cryptographic_Processor.gcd(q,p%q)
    def make_exp(self):
        k=random.randint(0,1<<self.__l)
        while Cryptographic_Processor.gcd(k,(1<<self.__l)-1)!=1: #키에 따라 코드가 달라짐.
            k=random.randint(0,1<<self.__l)
        return k
    def make_safe_openkey(self):
        k=self.make_exp()
        return self.pow(self.safekey,k)
    
    # 공개키 만들기
    def makePublic(self):
        self.__n=random.randint(1<<(self.__l-1),1<<self.__l)
        self.__p1=self.make_safe_openkey()
        self.__p2=self.pow(self.__p1,self.__n)
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
