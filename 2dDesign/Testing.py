from Shape import Shape

x = Shape(1,2,3,4,"X")
x.PrintValues(-1)

y = Shape(5,6,7,8,"Y")
y.PrintValues(-1)

x.AddSubDesign(y)
x.PrintValues(-1)

c = Shape(4,3,2,1,"C")
c.AddSubDesign(x)
c.PrintValues(-1)

b = Shape(2,2,2,2,"B")
c.AddSubDesign(b)
c.PrintValues(2)

#c.SortArea()
#c.PrintValues(-1)

a = Shape(0,0,3,3,"A")
x.AddSubDesign(a)
c.PrintValues(-1)

c.SortArea()
c.PrintValues(-1)

c.PrintValues(0)
c.PrintValues(1)
c.PrintValues(2)

c.ReturnOneLevel()