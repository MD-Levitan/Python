from CipherAffine import CipherAffine
class CipherCaesar(CipherAffine):

    def __init__(self,shift):
        CipherAffine.__init__(self,shift,1)

    def encrypt(self,line):
        return CipherAffine.encrypt(self,line)

    def decrypt(self,line):
        return CipherAffine.decrypt(self,line)
