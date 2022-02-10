# t_timer2.py
# 0.1초마다 이동하는 거북이

import turtle as t
import random

def run():
    t.forward(5)
    ts.forward(3)

    if t.xcor()>350:
        t.goto(-350,50)
    if ts.xcor()>350:
        ts.goto(-350,-50)
    t.ontimer(run,100)

def d_line(y):
    t.up()
    t.goto(-350,y)
    t.down()
    t.goto(350,y)

# 환경설정
t.setup(700,300)
t.bgcolor('orange')

# 트랙 선 그리기
t.speed(0)
t.color('white')
t.up()
t.goto(-350,0)
t.down()
t.goto(350,0)
t.up()
t.goto(-350,100)
t.down()
t.goto(350,100)
t.up()
t.goto(-350,-100)
t.down()
t.goto(350,-100)

# 빨강 거북이
ts=t.Turtle()
ts.shape('turtle')
ts.color('red')
ts.up()
ts.goto(-300,-50)

# 흰 거북이
t.shape('turtle')
t.color('white')
t.up()
t.goto(-300,50)

# 달리기
run()
    
