from turtle import forward, left, right, fillcolor, exitonclick, penup, pendown, begin_fill, end_fill, color
n = 20
pocetKostek = int(input("Zvol velikost mozaiky a udej počet kostek:"))
for _ in range(pocetKostek):
    for _ in range(pocetKostek):
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
        #presun1
        penup()
        right(60)
        forward(n*2)
        left(120)
        pendown()
    #presun2    
    penup()
    left(60)
    forward(n*(pocetKostek*2-1))
    left(120)
    forward(n*(pocetKostek-2))
    left(180)

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
     

