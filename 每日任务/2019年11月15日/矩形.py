class Rectangle:
        langth = 5
        width = 4
        def setRect(self):
                print("请输入矩形的长和宽")
                self.length = float(input("长:"))
                self.width = float(input("宽:"))


        def getRect(self):
                print("这个矩形的长是：%.2f,宽是： %.2f" % (self.length,self.width))



        def gerArea(self):
                 s = self.length * self.width
                 print("这个矩形的面积是%d"%s)
p = Rectangle()
p.setRect()
p.getRect()
p.gerArea()
