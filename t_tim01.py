# t_tim01.py
# 타이머

import turtle as t

def run():
    t.forward(50)
    print(t.xcor())

    if t.xcor() <400:
        t.ontimer(run,2000) # 재귀 함수
    
t.shape('turtle')

# t.ontimer(함수, 시간)
# t.ontimer(run, 2000)

run()

