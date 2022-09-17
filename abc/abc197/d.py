import math
n=int(input())
x_0,y_0=map(int,input().split())
x_1,y_1=map(int,input().split())


p_x=(x_1-x_0)/2
p_y=(y_1-y_0)/2




kaku=math.atan2(p_y,p_x)
kaku=kaku-2*math.pi/n
print(p_x,p_y,kaku)
x=math.cos(kaku)*x_0-math.sin(kaku)*y_0+p_x-p_x*math.cos(kaku)+p_y*math.sin(kaku)
y=math.sin(kaku)*x_0+math.cos(kaku)*y_0+p_y-p_x*math.sin(kaku)-p_y*math.cos(kaku)
print(x,y)

