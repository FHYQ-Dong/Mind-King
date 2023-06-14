import os
from hmac import HMAC
from hashlib import sha256

class Hash():
    def __init__(self, password:bytes, salt:bytes=None, hashedpwd:bytes=None, target:bytes=None) -> None:
        self.password = password
        self.salt = salt
        self.hashedpwd = hashedpwd
        self.target = target

    def encrypt(self): # 关键词是None而非NULL
        if self.salt == None:
            self.salt = os.urandom(8) # 生成一个八个byte的随机串作为salt
        self.hashedpwd = self.password
        for i in range(10):
            self.hashedpwd = HMAC(self.hashedpwd, self.salt, sha256).digest() # 先生成一个HMAC()对象，然后再调用digest()生成hash之后的结果
        self.hashedpwd = self.salt + self.hashedpwd
        return self.hashedpwd
        
    def verify(self): # hashed_password的前8位是salt
        if self.salt == None:
            raise ValueError('salt不能为空')
        if self.encrypt() == self.target:
            return True
        else: return False
