- ๐ Hi, Iโm @piaojungwoo# 14a_p1.py
# ๋ฌธ์  ๋ง๋ค๊ธฐ
#

import random

n1= random.randint(1,10)
n2= random.randint(1,10)

q=str(n1)
q= q+ '+'
q= q+ str(n2)

a= eval(q)

print(q, '=',a)

# 14a_p2.py
# ๋ฌธ์  ๋ง๋ค๊ธฐ(๋ง์,๋บ์)

import random

# ๋ ์์ ์ฐ์ฐ์ ๋์ ์์ฑ
n1=random.randint(1,10)
n2=random.randint(1,10)
op=random.randint(1,2)

q=str(n1)
if op ==1:
    q=q+'+'
else:
    q=q+'-'
q= q+str(n2)

print(q)

# 13a_l.py
# ํ๊ทน ๋ชจ์ ๊ทธ๋ฆฌ๊ธฐ
# 14a_p4.py
# ๋ฌธ์  ๋ง๋ค๊ธฐ

import random

def make_quiz():

        n1=random.randint(1,10)
        n2=random.randint(1,10)
        op=random.randint(1,3)
        if op ==1:
            ops='+'
        elif op ==2:
            ops='-'
        else:
            ops='*'

        # ๋ ๊ฐ์ ์ซ์(n1,n2)์ ์ฐ์ฐ์(ops)๋ก ๋ฌธ์  ์์ฑ
        q= f'{n1} {ops} {n2}'
        return q

    for x in range(10):
        q=make_quiz()
        a=eval(q)
        print(f'{q}={a}')

# 14a_p3.py
# ๋ฌธ์  ๋ง๋ค๊ธฐ(+,-,*)

import random

n1=random.randint(1,10)
n2=random.randint(1,10)
op=random.randint(1,3)

q=str(n1)
if op ==1:
    q=q+'+'
elif op ==2:
    q=q+'-'
else:
    q=q+'*'
q=q+str(n2)

a=eval(q)
print

import turtle as t

t.bgcolor('black')
t.speed(0)

for x in range(500):
    mod=x%3
    if mod==0:
        t.color('red')
    elif mod ==1:
        t.color('yellow')
    else:
        t.color('blue')
    t.forward(x * 2)
    t.left(119)

# 13a_p1.py
# ๋๋จธ์ง ์ฐ์ต

print('1~10๊น์ง 3์ผ๋ก ๋๋ ๋๋จธ์ง ๊ตฌํ๊ธฐ')
for x in range(10):
    print(f'{x} % 3= {x%3}')

print('-' * 30)

print('๊ฐ์, ๋ฐ์, ๋ณด ๋ฐ๋ณต ์ถ๋ ฅํ๊ธฐ')
for x in range(10):
    mod= x%3
    if mod == 0:
        print('๊ฐ์')
    elif mod == 1:
        print('๋ฐ์')
    else:
        print('๋ณด')

print('ํ์, ์ง์ ์ถ๋ ฅํ๊ธฐ')
for x in range(10):
    mod=x%2
    if mod ==0:
        print(f'{x}์(๋) ์ง์')
    else:
        print(f'{x}์(๋) ํ์')

# ch05ex01.py
# ํ๊ทน๋ชจ์ ๊ทธ๋ฆฌ๊ธฐ

import turtle as t

t.bgcolor('purple')
t.speed(0)

for x in range(500):
    mod=x%4
    if mod==0:
        t.color('yellow')
    elif mod==1:
        t.color('blue')
    elif mod==2:
        t.color('blue')
    else:
        t.color('green')
    t.forward(x * 2)
    t.left(89)

# 13b_p1
# ๊ฑฐ๋ถ์ด ์ด๋

import turtle as t

def move():
    t.setheading(90)
    t.forward(10)

t.shape('turtle')

# ํจ์ ํธ์ถ
# move()

# ์ด๋ฒคํธ ์ฌ์ฉํ๊ธฐ
t.onkeypress(move, 'Up')
t.listen()

# 13b_w
# ๊ฑฐ๋ถ์ด ์ด๋ํ๊ธฐ

import turtle as t

t.bgcolor('black')
t.color('orange')

def t_up():
    t.setheading(90)
    t.forward(10)

def t_down():
    t.setheading(270)
    t.forward(10)

def t_left():
    t.setheading(180)
    t.forward(10)

def t_right():
    t.setheading(0)
    t.forward(10)

def p_size1():
    t.pensixe(1)

def p_size5():
    t.pensize(5)

def t_coly():
    t.color('yellow')

def t_colo():
    t.color('orange')

def clear():
    t.clear()

t.onkeypress(clear, "Escape")
t.onkeypress(t_up, 'Up')
t.onkeypress(t_down, 'Down')
t.onkeypress(t_left, 'Left')
t.onkeypress(t_right, 'Right')
t.onkeypress(p_up, 'u')
t.onkeypress(p_down, 'd')
t.onkeypress(p_size1, '1')
t.onkeypress(p_size5, '5')
t.onkeypress(t_coly, 'y')
t.onkeypress(t_colop, 'o')

t.onkeypress(t_up,'Up')
t.onkeypress(t_down, 'Down')
t.onkeypress(t_left, 'Left')
t.onkeypress(t_right, 'Right')
t.listen()


# 13c_d.py
# ๋ง์ฐ์ค๋ก ๊ฑฐ๋ถ์ด ์ด๋ํ๊ธฐ

import turtle as t

t.speed(0)
t.hideturtle()
t.onscreenclick(t.goto)

- ๐ Iโm interested in ...
- ๐ฑ Iโm currently learning ...
- ๐๏ธ Iโm looking to collaborate on ...
- ๐ซ How to reach me ...

<!---
piaojungwoo/piaojungwoo is a โจ special โจ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
