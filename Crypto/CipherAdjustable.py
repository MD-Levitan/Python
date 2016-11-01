from CipherInterface import CipherInterface
class CipherAdjustable(CipherInterface):

    def __init__(self,key):
        self.key=str(key)
        for alpha in self.key:
            if not alpha.isalpha() and not alpha.isspace():
                raise Exception("Illegal arguments. There are some illegal symbols in key.")
        if len(set(self.key))!=len(self.key):
            raise Exception("Illegal key. There are some similar symbols.")
        self.key_per=self.key_permutation()
        self.len_key = len(self.key_per)
        self.key_per_reverse=self.key_permutation_reverse()


    def key_permutation(self):
        sort_key=list(self.key)
        sort_key.sort()
        return [sort_key.index(x) for x in self.key]

    def key_permutation_reverse(self):
        return [self.key_per.index(x) for x in range(0,self.len_key)]

    def permutation(self,line):
        if len(line)!=self.len_key:
            line=str(line)+(' '*(self.len_key-len(line)))
        return ''.join([str(line)[x] for x in self.key_per])

    def depermutation(self,line):
        if len(line)!=self.len_key:
            line=str(line)+(' '*(self.len_key-len(line)))
        return ''.join([str(line)[x] for x in self.key_per_reverse])

    def encrypt(self,line):
        index=0
        ret_line=''
        while index<len(line):
            ret_line+=self.permutation(line[index:index+self.len_key])
            index += self.len_key
        return ''.join(ret_line)

    def decrypt(self,line):
        index = 0
        ret_line = ''
        while index < len(line):
            ret_line += self.depermutation(line[index:index+self.len_key])
            index += self.len_key
        return ''.join(ret_line)
