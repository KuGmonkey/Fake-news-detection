class Circle:
    radius=5
    def setradius(self,a):
        self.radius=a
    def getperimter(self):
        print(3.14*2*self.radius)
    def getarea(self):
        print(3,14*self.radius*self.radius)
test=Circle()
test.getperimter()
test.getarea()
test.setradius(int(input()))
test.getperimter()
test.getarea()
