class Polynom() :
    def __init__(self,line):
        self.degree=len(line)
        self.koef=list(str(line))


    def add(self,polynom):
        new_koef=[(x+y)%2 for x,y in zip(self.koef, polynom.koef)]
        return
