from Shape import Shape

x = Shape(1,2,3,4, "X")
x.PrintValues()

y = Shape(5,6,7,8, "Y")
y.PrintValues()

x.AddSubDesign(y)
x.PrintValues()

c = Shape(4,3,2,1,"C")
c.AddSubDesign(x)
c.PrintValues()

b = Shape(2,2,2,2,"B")
c.AddSubDesign(b)
c.PrintValues()