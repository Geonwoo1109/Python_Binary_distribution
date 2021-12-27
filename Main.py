import turtle as t
import random as r

times = input("시행 횟수: ")

t.speed(0)
t.up()
t.goto (-400, -300)
t.down()
t.goto (400, -300)
t.goto (-400, -300)


t.left(90)
for i in range (int(times) + 1):
    print(i)
    t.goto(((800/int(times)-1)*i)-400, -300)
    t.forward(20)
    t.up()
    t.back(40)
    t.write(i, align="center", font=("", 5))
    t.forward(20)
    t.down()
    

cnt = []

for i in range (int(times) + 1):
    cnt.append(0)

print(cnt)

for i in range (int(times)): #둘중에 하나 고정시키기!
    temp = 0
    
    for j in range (int(times)):
        rNumber = r.randrange(0, 2)
        if rNumber == 1:
            temp = temp + 1
            
    cnt[temp] = cnt[temp] + 1


print("시행 횟수: {times}".format(times=times))
print(cnt)

t.pensize(5)
for i in range (int(times) + 1):
    print("앞이 {n1}번 나온 횟수: {n2}".format(n1=i, n2=cnt[i]))
    t.goto(((800/int(times)-1)*i)-400, -300)
    t.forward(cnt[i]*50)
    t.back(cnt[i]*50)
