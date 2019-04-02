from turtle import forward, left, right, fillcolor, exitonclick, penup, pendown, begin_fill, end_fill, color
n = 20
for _ in range (11):
    #prvni kosoctverec
    begin_fill()
    for _ in range(2):
        forward(n)
        left(60)
        forward(n)
        left(120)
    color("steelblue")
    end_fill()
    #druhy kosoctverec
    begin_fill()
    for _ in range(2):
        forward(n)
        right(60)
        forward(n)
        right(120)
    color("midnightblue")
    end_fill()
    #treti kosoctverec
    forward(n)
    right(60)
    begin_fill()
    for _ in range(2):
        forward(n)
        left(120)
        forward(n)
        left(60)
    color("lavender")
    end_fill()
    #presun
    penup()
    right(60)
    forward(n*2)
    left(120)
    pendown()

exitonclick()






#delkaStrany = 1
#m = 0.02
#for _ in range(1000):
#    forward(m)
#    left(180 - (180*(1-2/95)))
#    m = m + 0.002

#n = int(input("Zadej počet:" ))
#for _ in range(n):
#    forward(delkaStrany)
#    left(180 - (180*(1-2/n)))
     

