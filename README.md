- 👋 Hi, I’m @piaojungwoo# 14a_p1.py
# 문제 만들기
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
# 문제 만들기(덧셈,뺄셈)

import random

# 두 수와 연산자 난수 생성
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
# 태극 모양 그리기
# 14a_p4.py
# 문제 만들기

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

        # 두 개의 숫자(n1,n2)와 연산자(ops)로 문제 생성
        q= f'{n1} {ops} {n2}'
        return q

    for x in range(10):
        q=make_quiz()
        a=eval(q)
        print(f'{q}={a}')

# 14a_p3.py
# 문제 만들기(+,-,*)

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
# 나머지 연습

print('1~10까지 3으로 나눈 나머지 구하기')
for x in range(10):
    print(f'{x} % 3= {x%3}')

print('-' * 30)

print('가위, 바위, 보 반복 출력하기')
for x in range(10):
    mod= x%3
    if mod == 0:
        print('가위')
    elif mod == 1:
        print('바위')
    else:
        print('보')

print('홀수, 짝수 출력하기')
for x in range(10):
    mod=x%2
    if mod ==0:
        print(f'{x}은(는) 짝수')
    else:
        print(f'{x}은(는) 홀수')

# ch05ex01.py
# 태극모양 그리기

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
# 거북이 이동

import turtle as t

def move():
    t.setheading(90)
    t.forward(10)

t.shape('turtle')

# 함수 호출
# move()

# 이벤트 사용하기
t.onkeypress(move, 'Up')
t.listen()

# 13b_w
# 거북이 이동하기

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
# 마우스로 거북이 이동하기

import turtle as t

t.speed(0)
t.hideturtle()
t.onscreenclick(t.goto)

- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
piaojungwoo/piaojungwoo is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
