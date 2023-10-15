import random, turtle

background=turtle.Turtle()
background.speed(0)
background.color("lawn green")
background.ht()
background.pu()
background.goto(-800,-200)
background.width(500)
background.pd()
background.fd(1600)
background.lt(90)
background.pu()
background.fd(500)
background.pd()
background.lt(90)
background.color("deep sky blue")
background.fd(1600)

fdrawer=turtle.Turtle()
fdrawer.speed(0)
fdrawer.pu()
fdrawer.ht()
fdrawer.lt(90)
colorstem=['green2', 'green3', 'chartreuse2', 'chartreuse3']
colormid=['sienna4', 'yellow4', 'orange red', 'blue4', 'purple4']
colorpetal=['blue', 'snow', 'gold,' 'yellow', 'orchid1', 'orange', 'red']


def flower():
    xcor=random.randint(-800,800)
    ycor=random.randint(-400,50)
    fdrawer.setx(xcor)
    fdrawer.sety(ycor)
    if ycor >= 0:
        sizemag=1
    elif 0 > ycor >= -50:
        sizemag=1.12
    elif -50 > ycor >= -100:
        sizemag=1.25
    elif -100 > ycor >= -150:
        sizemag=1.37
    elif -150 > ycor >= -200:
        sizemag=1.50
    elif -200 > ycor >= -250:
        sizemag=1.62
    elif -250 > ycor >= -300:
        sizemag=1.75
    elif -300 > ycor >- -350:
        sizemag=1.87
    else:
        sizemag=2
    stem=round(100 * sizemag)
    radius=round(50 * sizemag)
    leafs=(50 * sizemag)
    side=random.randint(0,1)
    stemcolor=colorstem[random.randrange(0,4)]
    fdrawer.color(stemcolor)
    fdrawer.width(5 * sizemag)
    fdrawer.pd()
    for x in range (stem):
        curve=random.randint(0,5)
        if side == 0:
            if curve > 3:
                fdrawer.fd(2)
                fdrawer.lt(1)
        elif side == 1:
            if curve > 3:
                fdrawer.fd(2)
                fdrawer.rt(1)    
    newxcor=(fdrawer.xcor())
    newycor=(fdrawer.ycor())
    fdrawer.pu()
    fdrawer.setx(newxcor)
    fdrawer.sety(newycor)
    fdrawer.begin_fill()
    
    fdrawer.color('black')
    
    fdrawer.pendown()
    #fdrawer.goto(0,0)
    fdrawer.fd(radius)
    fdrawer.pd()
    fdrawer.circle(radius)
    #fdrawer.forward(radius)
    fdrawer.ht()
    
    fdrawer.stamp()
    fdrawer.seth(0)
    midcolor=colormid[random.randrange(0,5)]
    #fdrawer.color(midcolor)
    
    """fdrawer.fd(radius)
    fdrawer.pd()
    fdrawer.circle(radius)
    fdrawer.forward(radius)"""
    print(newxcor)
    print(newycor)
    print(radius)
    
    
        
        
            
                
            
fdrawer._tracer(False)


flower()
fdrawer.xcor()
fdrawer.ycor()

turtle.Screen().exitonclick()