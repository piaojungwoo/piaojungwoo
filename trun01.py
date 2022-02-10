# trun01.py
# 터틀 객체 생성하기

import turtle as t

#환경설정
t.setup(500,500) # 가로 500px, 세로 500px 창 생성
t.bgcolor('black')

te=t.Turtle()
te.shape('turtle')
te.color('red')
te.goto(100,100)
te.forward(100)

ts=t.Turtle()
ts.shape('circle')
ts.color('green')
ts.goto(-100,-100)
ts.forward(50)

t.color('blue')
t.shape('turtle')
t.forward(150)
