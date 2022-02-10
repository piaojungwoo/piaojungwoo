# t_timer.py
# 이동하는 거북이

import turtle as t

def run():
    t.forward(10)
    # print(t.xcor())
    if t.xcor()>400:
        t.goto(-400,0)
    t.ontimer(run,100)

# 환경 설성
t.setup(800,500)
t.bgcolor('orange')

# 거북이 설정

t.speed(0)
t.color('white')
t.up()
t.goto(-400,0)
t.shape('turtle')

# 함수 실행
run()


