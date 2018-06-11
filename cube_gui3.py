from tkinter import *
from math import*
from time import*
import random

#기본 큐브 함수
def reset():
    a = [["white", "white", "white"], ["white", "white", "white"], ["white", "white", "white"]]
    b = [["red", "red", "red"], ["red", "red", "red"], ["red", "red", "red"]]
    c = [["blue", "blue", "blue"], ["blue", "blue", "blue"], ["blue", "blue", "blue"]]
    d = [["#FC9B1B", "#FC9B1B", "#FC9B1B"], ["#FC9B1B", "#FC9B1B", "#FC9B1B"], ["#FC9B1B", "#FC9B1B",  "#FC9B1B"]]
    e = [["green", "green", "green"], ["green", "green", "green"], ["green", "green", "green"]]
    f = [["yellow", "yellow", "yellow"], ["yellow", "yellow", "yellow"], ["yellow", "yellow", "yellow"]]
    return a,b,c,d,e,f
def right(a,b,c,d,e,f):
    b[0][0],b[1][0],b[2][0],c[0][0],c[1][0],c[2][0],d[2][2],d[1][2],d[0][2],e[2][0],e[1][0],e[0][0]=e[2][0],e[1][0],e[0][0],b[0][0],b[1][0],b[2][0],c[0][0],c[1][0],c[2][0],d[2][2],d[1][2],d[0][2]
    b[0][1],b[1][1],b[2][1],c[0][1],c[1][1],c[2][1],d[2][1],d[1][1],d[0][1],e[2][1],e[1][1],e[0][1]=e[2][1],e[1][1],e[0][1],b[0][1],b[1][1],b[2][1],c[0][1],c[1][1],c[2][1],d[2][1],d[1][1],d[0][1]
    b[0][2],b[1][2],b[2][2],c[0][2],c[1][2],c[2][2],d[2][0],d[1][0],d[0][0],e[2][2],e[1][2],e[0][2]=e[2][2],e[1][2],e[0][2],b[0][2],b[1][2],b[2][2],c[0][2],c[1][2],c[2][2],d[2][0],d[1][0],d[0][0]
    a0, a1, a2 = a[0], a[1], a[2]
    a[0] = [a2[0], a1[0], a0[0]]
    a[1] = [a2[1], a1[1], a0[1]]
    a[2] = [a2[2], a1[2], a0[2]]
    f0, f1, f2 = f[0], f[1], f[2]
    f[0] = [f0[2], f1[2], f2[2]]
    f[1] = [f0[1], f1[1], f2[1]]
    f[2] = [f0[0], f1[0], f2[0]]
    return a,b,c,d,e,f
def left(a,b,c,d,e,f):
    b[0][0],b[1][0],b[2][0],c[0][0],c[1][0],c[2][0],d[2][2],d[1][2],d[0][2],e[2][0],e[1][0],e[0][0]=c[0][0],c[1][0],c[2][0],d[2][2],d[1][2],d[0][2],e[2][0],e[1][0],e[0][0],b[0][0],b[1][0],b[2][0]
    b[0][1],b[1][1],b[2][1],c[0][1],c[1][1],c[2][1],d[2][1],d[1][1],d[0][1],e[2][1],e[1][1],e[0][1]=c[0][1],c[1][1],c[2][1],d[2][1],d[1][1],d[0][1],e[2][1],e[1][1],e[0][1],b[0][1],b[1][1],b[2][1]
    b[0][2],b[1][2],b[2][2],c[0][2],c[1][2],c[2][2],d[2][0],d[1][0],d[0][0],e[2][2],e[1][2],e[0][2]=c[0][2],c[1][2],c[2][2],d[2][0],d[1][0],d[0][0],e[2][2],e[1][2],e[0][2],b[0][2],b[1][2],b[2][2]
    a0, a1, a2 = a[0], a[1], a[2]
    a[0] = [a0[2], a1[2], a2[2]]
    a[1] = [a0[1], a1[1], a2[1]]
    a[2] = [a0[0], a1[0], a2[0]]
    f0, f1, f2 = f[0], f[1], f[2]
    f[0] = [f2[0], f1[0], f0[0]]
    f[1] = [f2[1], f1[1], f0[1]]
    f[2] = [f2[2], f1[2], f0[2]]
    return a,b,c,d,e,f
def up(a,b,c,d,e,f):
    c0,c1,c2=c[0],c[1],c[2]
    c[0]=[c0[2],c1[2],c2[2]]
    c[1]=[c0[1],c1[1],c2[1]]
    c[2]=[c0[0],c1[0],c2[0]]
    e0,e1,e2=e[0],e[1],e[2]
    e[0] = [e0[2], e1[2], e2[2]]
    e[1] = [e0[1], e1[1], e2[1]]
    e[2] = [e0[0], e1[0], e2[0]]
    return b,f,c,a,e,d
def down(a,b,c,d,e,f):
    c0, c1, c2 = c[0], c[1], c[2]
    c[0] = [c2[0], c1[0], c0[0]]
    c[1] = [c2[1], c1[1], c0[1]]
    c[2] = [c2[2], c1[2], c0[2]]
    e0, e1, e2 = e[0], e[1], e[2]
    e[0] = [e2[0], e1[0], e0[0]]
    e[1] = [e2[1], e1[1], e0[1]]
    e[2] = [e2[2], e1[2], e0[2]]
    return d,a,c,f,e,b
def h_right(a,b,c,d,e,f):
    b0, b1, b2 = b[0], b[1], b[2]
    b[0] = [b0[2], b1[2], b2[2]]
    b[1] = [b0[1], b1[1], b2[1]]
    b[2] = [b0[0], b1[0], b2[0]]
    d0, d1, d2 = d[0], d[1], d[2]
    d[0] = [d2[0], d1[0], d0[0]]
    d[1] = [d2[1], d1[1], d0[1]]
    d[2] = [d2[2], d1[2], d0[2]]
    a[0], a[1], a[2], c[0], c[1], c[2], f[0], f[1], f[2], e[0], e[1], e[2] = [e[2][2], e[1][2], e[0][2]], [e[2][1], e[1][1], e[0][1]], [e[2][0], e[1][0], e[0][0]], [a[0][2], a[1][2], a[2][2]], [a[0][1], a[1][1], a[2][1]], [a[0][0], a[1][0], a[2][0]], [c[0][2], c[1][2], c[2][2]], [c[0][1], c[1][1], c[2][1]], [c[0][0], c[1][0], c[2][0]], [f[0][0], f[1][0], f[2][0]], [f[0][1], f[1][1], f[2][1]], [f[0][2], f[1][2], f[2][2]]
    return a,b,c,d,e,f
def h_left(a,b,c,d,e,f):
    b0, b1, b2 = b[0], b[1], b[2]
    b[0] = [b2[0], b1[0], b0[0]]
    b[1] = [b2[1], b1[1], b0[1]]
    b[2] = [b2[2], b1[2], b0[2]]
    d0, d1, d2 = d[0], d[1], d[2]
    d[0] = [d0[2], d1[2], d2[2]]
    d[1] = [d0[1], d1[1], d2[1]]
    d[2] = [d0[0], d1[0], d2[0]]
    a[0], a[1], a[2], c[0], c[1], c[2], f[0], f[1], f[2], e[0], e[1], e[2] = [c[2][0], c[1][0], c[0][0]], [c[2][1], c[1][1], c[0][1]], [c[2][2], c[1][2], c[0][2]], [f[2][0], f[1][0], f[0][0]], [f[2][1], f[1][1], f[0][1]], [f[2][2], f[1][2], f[0][2]], [e[0][0], e[1][0], e[2][0]], [e[0][1], e[1][1], e[2][1]], [e[0][2], e[1][2], e[2][2]], [a[2][2], a[1][2], a[0][2]], [a[2][1], a[1][1], a[0][1]], [a[2][0], a[1][0], a[0][0]]
    return a,b,c,d,e,f
def R(a,b,c,d,e,f):
    a[2], b[2], f[2], d[2]=b[2],f[2],d[2],a[2]
    c0, c1, c2 = c[0], c[1], c[2]
    c[0] = [c0[2], c1[2], c2[2]]
    c[1] = [c0[1], c1[1], c2[1]]
    c[2] = [c0[0], c1[0], c2[0]]
    return a,b,c,d,e,f
def RR(a,b,c,d,e,f):
    a[2], b[2], f[2], d[2] =  d[2],a[2],b[2],f[2]
    c0, c1, c2 = c[0], c[1], c[2]
    c[0] = [c2[0], c1[0], c0[0]]
    c[1] = [c2[1], c1[1], c0[1]]
    c[2] = [c2[2], c1[2], c0[2]]
    return a,b,c,d,e,f
def L(a,b,c,d,e,f):
    a[0], b[0], f[0], d[0] = b[0], f[0], d[0], a[0]
    e0, e1, e2 = e[0], e[1], e[2]
    e[0] = [e0[2], e1[2], e2[2]]
    e[1] = [e0[1], e1[1], e2[1]]
    e[2] = [e0[0], e1[0], e2[0]]
    return a,b,c,d,e,f
def LR(a,b,c,d,e,f):
    a[0], b[0], f[0], d[0] = d[0], a[0], b[0], f[0]
    e0, e1, e2 = e[0], e[1], e[2]
    e[0] = [e2[0], e1[0], e0[0]]
    e[1] = [e2[1], e1[1], e0[1]]
    e[2] = [e2[2], e1[2], e0[2]]
    return a,b,c,d,e,f
def U(a,b,c,d,e,f):
    a0, a1, a2 = a[0], a[1], a[2]
    a[0] = [a0[2], a1[2], a2[2]]
    a[1] = [a0[1], a1[1], a2[1]]
    a[2] = [a0[0], a1[0], a2[0]]
    b[0][0], b[1][0], b[2][0], c[0][0], c[1][0], c[2][0], d[0][2], d[1][2], d[2][2], e[2][0], e[1][0], e[0][0] = c[0][0], c[1][0], c[2][0], d[2][2],d[1][2],d[0][2], e[0][0], e[1][0], e[2][0], b[0][0], b[1][0], b[2][0]
    return a,b,c,d,e,f
def UR(a,b,c,d,e,f):
    a0, a1, a2 = a[0], a[1], a[2]
    a[0] = [a2[0], a1[0], a0[0]]
    a[1] = [a2[1], a1[1], a0[1]]
    a[2] = [a2[2], a1[2], a0[2]]
    b[0][0], b[1][0], b[2][0], c[0][0], c[1][0], c[2][0], d[0][2], d[1][2], d[2][2],e[2][0], e[1][0], e[0][0] = e[2][0], e[1][0], e[0][0], b[0][0], b[1][0], b[2][0], c[2][0], c[1][0], c[0][0], d[2][2], d[1][2], d[0][2]
    return a,b,c,d,e,f
def D(a,b,c,d,e,f):
    f0, f1, f2 = f[0], f[1], f[2]
    f[0] = [f2[0], f1[0], f0[0]]
    f[1] = [f2[1], f1[1], f0[1]]
    f[2] = [f2[2], f1[2], f0[2]]
    b[0][2], b[1][2], b[2][2], c[0][2], c[1][2], c[2][2], d[0][0], d[1][0], d[2][0], e[2][2], e[1][2], e[0][2] = c[0][2], c[1][2], c[2][2], d[2][0], d[1][0], d[0][0], e[0][2], e[1][2], e[2][2], b[0][2], b[1][2], b[2][2]
    return a,b,c,d,e,f
def DR(a,b,c,d,e,f):
    f0, f1, f2 = f[0], f[1], f[2]
    f[0] = [f0[2], f1[2], f2[2]]
    f[1] = [f0[1], f1[1], f2[1]]
    f[2] = [f0[0], f1[0], f2[0]]
    b[0][2], b[1][2], b[2][2], c[0][2], c[1][2], c[2][2], d[0][0], d[1][0], d[2][0], e[2][2], e[1][2], e[0][2] = e[2][2], e[1][2], e[0][2], b[0][2], b[1][2], b[2][2], c[2][2], c[1][2], c[0][2], d[2][0], d[1][0], d[0][0]
    return a,b,c,d,e,f
def F(a,b,c,d,e,f):
    b0, b1, b2 = b[0], b[1], b[2]
    b[0] = [b0[2], b1[2], b2[2]]
    b[1] = [b0[1], b1[1], b2[1]]
    b[2] = [b0[0], b1[0], b2[0]]
    c[0], e[0], a[0][2], a[1][2], a[2][2], f[0][0], f[1][0], f[2][0] = [a[0][2], a[1][2], a[2][2]], [f[0][0], f[1][0], f[2][0]], e[0][2], e[0][1], e[0][0], c[0][2], c[0][1], c[0][0]
    return a,b,c,d,e,f
def FR(a,b,c,d,e,f):
    b0, b1, b2 = b[0], b[1], b[2]
    b[0] = [b2[0], b1[0], b0[0]]
    b[1] = [b2[1], b1[1], b0[1]]
    b[2] = [b2[2], b1[2], b0[2]]
    c[0], e[0], a[0][2], a[1][2], a[2][2], f[0][0], f[1][0], f[2][0] = [f[2][0], f[1][0], f[0][0]], [a[2][2], a[1][2], a[0][2]], c[0][0], c[0][1], c[0][2], e[0][0], e[0][1], e[0][2]
    return a,b,c,d,e,f
def B(a,b,c,d,e,f):
    d0, d1, d2 = d[0], d[1], d[2]
    d[0] = [d2[0], d1[0], d0[0]]
    d[1] = [d2[1], d1[1], d0[1]]
    d[2] = [d2[2], d1[2], d0[2]]
    c[2], e[2], a[0][0], a[1][0], a[2][0], f[0][2], f[1][2], f[2][2] = [a[0][0], a[1][0], a[2][0]], [f[0][2], f[1][2], f[2][2]], e[2][2], e[2][1], e[2][0], c[2][2], c[2][1], c[2][0]
    return a,b,c,d,e,f
def BR(a,b,c,d,e,f):
    d0, d1, d2 = d[0], d[1], d[2]
    d[0] = [d0[2], d1[2], d2[2]]
    d[1] = [d0[1], d1[1], d2[1]]
    d[2] = [d0[0], d1[0], d2[0]]
    c[2], e[2], a[0][0], a[1][0], a[2][0], f[0][2], f[1][2], f[2][2] = [f[2][2], f[1][2], f[0][2]], [a[2][0], a[1][0], a[0][0]], c[2][0], c[2][1], c[2][2], e[2][0], e[2][1], e[2][2]
    return a,b,c,d,e,f
def run_shuf(a,b,c,d,e,f,i):
    if i==0:
        return R(a,b,c,d,e,f)
    elif i==1:
        return RR(a,b,c,d,e,f)
    elif i==2:
        return L(a,b,c,d,e,f)
    elif i==3:
        return LR(a,b,c,d,e,f)
    elif i==4:
        return U(a,b,c,d,e,f)
    elif i==5:
        return UR(a,b,c,d,e,f)
    elif i==6:
        return D(a,b,c,d,e,f)
    elif i==7:
        return DR(a,b,c,d,e,f)
    elif i==8:
        return F(a,b,c,d,e,f)
    elif i==9:
        return FR(a,b,c,d,e,f)
    elif i==10:
        return B(a,b,c,d,e,f)
    elif i==11:
        return BR(a,b,c,d,e,f)
def shuffle(a1,b1,c1,d1,e1,f1):
    global li
    com_list = [random.randint(0,11) for i in range(30)]
    for i in range(30):
        a,b,c,d,e,f=run_shuf(a1,b1,c1,d1,e1,f1,com_list[i])
    li=[]
    return a,b,c,d,e,f
def undo(canv,a1,b1,c1,d1,e1,f1):
    global li
    global a,b,c,d,e,f
    if len(li)==0:
        print("no command to undo!")
    else:
        canv.delete("all")
        if li[-1]==12:
            a, b, c, d, e, f = left(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==13:
            a, b, c, d, e, f = right(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==14:
            a, b, c, d, e, f = down(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==15:
            a, b, c, d, e, f = up(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==16:
            a, b, c, d, e, f = h_left(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==17:
            a, b, c, d, e, f = h_right(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==0:
            a, b, c, d, e, f = RR(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==1:
            a, b, c, d, e, f = R(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==2:
            a, b, c, d, e, f = LR(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==3:
            a, b, c, d, e, f = L(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==4:
            a, b, c, d, e, f = UR(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==5:
            a, b, c, d, e, f = U(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==6:
            a, b, c, d, e, f = DR(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==7:
            a, b, c, d, e, f = D(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==8:
            a, b, c, d, e, f = FR(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==9:
            a, b, c, d, e, f = F(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==10:
            a, b, c, d, e, f = BR(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==11:
            a, b, c, d, e, f = B(a1, b1, c1, d1, e1, f1)
            pr_print(canv, a, b, c, d, e, f)
            li.pop(-1)
        else:
            li.pop(-1)
def cube_check(a,b,c):
    if (a[0]==a[1] and a[1]==a[2]) and (b[0]==b[1] and b[1]==b[2]) and (c[0]==c[1] and c[1]==c[2]):
        return True
    else:
        return False


#pr_관련 함수 2d mostly
def pr_shuffle(canv,a1,b1,c1,d1,e1,f1):
    import random
    global a,b,c,d,e,f
    global li
    com_list = [random.randint(0,11) for i in range(30)]
    for i in range(30):
        a,b,c,d,e,f=run_shuf(a,b,c,d,e,f,com_list[i])
    li=[]
    pr_print(canv, a, b, c, d, e, f)
def pr_print(canv,a,b,c,d,e,f):
    global can
    global mode
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    if mode==1:
        pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
    elif mode==0:
        pr_cube(canv,a,b,c,d,e,f)
def pr_cube(canv, a, b, c, d, e, f):
        # 앞면의 블럭 한칸 가로세로 (50)
        # 앞면 블럭 간격 (5)
    b00 = canv.create_polygon(450, 300, 450, 350, 500, 350, 500, 300, fill=b[0][0], outline='black')
    b01 = canv.create_polygon(450, 355, 450, 405, 500, 405, 500, 355, fill=b[0][1], outline='black')
    b02 = canv.create_polygon(450, 410, 450, 460, 500, 460, 500, 410, fill=b[0][2], outline='black')
    b10 = canv.create_polygon(505, 300, 505, 350, 555, 350, 555, 300, fill=b[1][0], outline='black')
    b11 = canv.create_polygon(505, 355, 505, 405, 555, 405, 555, 355, fill=b[1][1], outline='black')
    b12 = canv.create_polygon(505, 410, 505, 460, 555, 460, 555, 410, fill=b[1][2], outline='black')
    b20 = canv.create_polygon(560, 300, 560, 350, 610, 350, 610, 300, fill=b[2][0], outline='black')
    b21 = canv.create_polygon(560, 355, 560, 405, 610, 405, 610, 355, fill=b[2][1], outline='black')
    b22 = canv.create_polygon(560, 410, 560, 460, 610, 460, 610, 410, fill=b[2][2], outline='black')

        # 오른면 블럭 가로(30) 세로(50) 우상상승폭(20)
        # 오른면 블럭 간격 가로세로(5) 우상상승폭(3)
    c00 = canv.create_polygon(615, 297, 615, 347, 645, 327, 645, 277, fill=c[0][0], outline='black')
    c01 = canv.create_polygon(615, 352, 615, 402, 645, 382, 645, 332, fill=c[0][1], outline='black')
    c02 = canv.create_polygon(615, 407, 615, 457, 645, 437, 645, 387, fill=c[0][2], outline='black')
    c10 = canv.create_polygon(650, 274, 650, 324, 680, 304, 680, 254, fill=c[1][0], outline='black')
    c11 = canv.create_polygon(650, 329, 650, 379, 680, 359, 680, 309, fill=c[1][1], outline='black')
    c12 = canv.create_polygon(650, 384, 650, 434, 680, 414, 680, 364, fill=c[1][2], outline='black')
    c20 = canv.create_polygon(685, 251, 685, 301, 715, 281, 715, 231, fill=c[2][0], outline='black')
    c21 = canv.create_polygon(685, 306, 685, 356, 715, 336, 715, 286, fill=c[2][1], outline='black')
    c22 = canv.create_polygon(685, 361, 685, 411, 715, 391, 715, 341, fill=c[2][2], outline='black')

        # 윗면 블럭 가로(50) 세로(30)
        # 윗면 블럭간격 가로(5) 세로(3)
    a00 = canv.create_polygon(520, 249, 570, 249, 600, 229, 550, 229, fill=a[0][0], outline='black')
    a01 = canv.create_polygon(485, 272, 535, 272, 565, 252, 515, 252, fill=a[0][1], outline='black')
    a02 = canv.create_polygon(450, 295, 500, 295, 530, 275, 480, 275, fill=a[0][2], outline='black')
    a10 = canv.create_polygon(575, 249, 625, 249, 655, 229, 605, 229, fill=a[1][0], outline='black')
    a11 = canv.create_polygon(540, 272, 590, 272, 620, 252, 570, 252, fill=a[1][1], outline='black')
    a12 = canv.create_polygon(505, 295, 555, 295, 585, 275, 535, 275, fill=a[1][2], outline='black')
    a20 = canv.create_polygon(630, 249, 680, 249, 710, 229, 660, 229, fill=a[2][0], outline='black')
    a21 = canv.create_polygon(595, 272, 645, 272, 675, 252, 625, 252, fill=a[2][1], outline='black')
    a22 = canv.create_polygon(560, 295, 610, 295, 640, 275, 590, 275, fill=a[2][2], outline='black')

        # 왼쪽면
    e00 = canv.create_polygon(270, 297, 270, 347, 300, 327, 300, 277, fill=e[0][0], outline='black')
    e01 = canv.create_polygon(270, 352, 270, 402, 300, 382, 300, 332, fill=e[0][1], outline='black')
    e02 = canv.create_polygon(270, 407, 270, 457, 300, 437, 300, 387, fill=e[0][2], outline='black')
    e10 = canv.create_polygon(305, 274, 305, 324, 335, 304, 335, 254, fill=e[1][0], outline='black')
    e11 = canv.create_polygon(305, 329, 305, 379, 335, 359, 335, 309, fill=e[1][1], outline='black')
    e12 = canv.create_polygon(305, 384, 305, 434, 335, 414, 335, 364, fill=e[1][2], outline='black')
    e20 = canv.create_polygon(340, 251, 340, 301, 370, 281, 370, 231, fill=e[2][0], outline='black')
    e21 = canv.create_polygon(340, 306, 340, 356, 370, 336, 370, 286, fill=e[2][1], outline='black')
    e22 = canv.create_polygon(340, 361, 340, 411, 370, 391, 370, 341, fill=e[2][2], outline='black')

        # 뒷면
    d00 = canv.create_polygon(760, 30, 760, 80, 810, 80, 810, 30, fill=d[0][2], outline='black')
    d01 = canv.create_polygon(760, 85, 760, 135, 810, 135, 810, 85, fill=d[0][1], outline='black')
    d02 = canv.create_polygon(760, 140, 760, 190, 810, 190, 810, 140, fill=d[0][0], outline='black')
    d10 = canv.create_polygon(815, 30, 815, 80, 865, 80, 865, 30, fill=d[1][2], outline='black')
    d11 = canv.create_polygon(815, 85, 815, 135, 865, 135, 865, 85, fill=d[1][1], outline='black')
    d12 = canv.create_polygon(815, 140, 815, 190, 865, 190, 865, 140, fill=d[1][0], outline='black')
    d20 = canv.create_polygon(870, 30, 870, 80, 920, 80, 920, 30, fill=d[2][2], outline='black')
    d21 = canv.create_polygon(870, 85, 870, 135, 920, 135, 920, 85, fill=d[2][1], outline='black')
    d22 = canv.create_polygon(870, 140, 870, 190, 920, 190, 920, 140, fill=d[2][0], outline='black')

        # 아랫면
    f00 = canv.create_polygon(450, 610, 500, 610, 530, 590, 480, 590, fill=f[0][0], outline='black')
    f01 = canv.create_polygon(485, 587, 535, 587, 565, 567, 515, 567, fill=f[0][1], outline='black')
    f02 = canv.create_polygon(520, 564, 570, 564, 600, 544, 550, 544, fill=f[0][2], outline='black')
    f10 = canv.create_polygon(505, 610, 555, 610, 585, 590, 535, 590, fill=f[1][0], outline='black')
    f11 = canv.create_polygon(540, 587, 590, 587, 620, 567, 570, 567, fill=f[1][1], outline='black')
    f12 = canv.create_polygon(575, 564, 625, 564, 655, 544, 605, 544, fill=f[1][2], outline='black')
    f20 = canv.create_polygon(560, 610, 610, 610, 640, 590, 590, 590, fill=f[2][0], outline='black')
    f21 = canv.create_polygon(595, 587, 645, 587, 675, 567, 625, 567, fill=f[2][1], outline='black')
    f22 = canv.create_polygon(630, 564, 680, 564, 710, 544, 660, 544, fill=f[2][2], outline='black') 
def pr_right(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(12)
    a,b,c,d,e,f=right(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_left(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(13)
    a,b,c,d,e,f=left(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_up(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(14)
    a,b,c,d,e,f=up(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_down(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(15)
    a,b,c,d,e,f=down(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_h_right(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(16)
    a,b,c,d,e,f=h_right(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_h_left(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(17)
    a,b,c,d,e,f=h_left(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_R(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(0)
    a,b,c,d,e,f=R(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_RR(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(1)
    a,b,c,d,e,f=RR(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_L(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(2)
    a,b,c,d,e,f=L(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_LR(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(3)
    a,b,c,d,e,f=LR(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_U(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(4)
    a,b,c,d,e,f=U(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_UR(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(5)
    a,b,c,d,e,f=UR(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_D(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(6)
    a,b,c,d,e,f=D(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_DR(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(7)
    a,b,c,d,e,f=DR(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_F(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(8)
    a,b,c,d,e,f=F(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_FR(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(9)
    a,b,c,d,e,f=FR(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_B(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(10)
    a,b,c,d,e,f=B(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_BR(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li.append(11)
    a,b,c,d,e,f=BR(a1,b1,c1,d1,e1,f1)
    pr_print(canv,a,b,c,d,e,f)
def pr_reset(canv):
    canv.delete("all")
    global a,b,c,d,e,f
    global li
    li=[]
    a,b,c,d,e,f=reset()
    pr_print(canv,a,b,c,d,e,f)



#단축키
class App(Frame):
    def __init__(self,master,right_key,left_key,up_key,down_key,h_right_key,h_left_key,R_key,RR_key,L_key,LR_key,U_key,UR_key,D_key,DR_key,F_key,FR_key,B_key,BR_key,sens):
        super().__init__(master)
        self.place(x=100, y=200)
        self.right_key=right_key
        self.left_key=left_key
        self.up_key=up_key
        self.down_key=down_key
        self.h_right_key=h_right_key
        self.h_left_key=h_left_key
        self.R_key=R_key
        self.RR_key=RR_key
        self.L_key=L_key
        self.LR_key=LR_key
        self.U_key=U_key
        self.UR_key=UR_key
        self.D_key=D_key
        self.DR_key=DR_key
        self.F_key=F_key
        self.FR_key=FR_key
        self.B_key=B_key
        self.BR_key=BR_key
        self.sens=sens
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="큐브 돌리기").grid(row=0,column=0)
        
        Label(self, text="오른쪽").grid(row=1,column=0)
        self.right_entry=Entry(self,width=10,justify=CENTER)
        self.right_entry.grid(row=1,column=1)
        self.right_entry.insert(0,self.right_key)

        Label(self, text="왼쪽").grid(row=1,column=3)
        self.left_entry=Entry(self,width=10,justify=CENTER)
        self.left_entry.grid(row=1,column=4)
        self.left_entry.insert(0,self.left_key)

        Label(self, text="위").grid(row=1,column=5)
        self.up_entry=Entry(self,width=10,justify=CENTER)
        self.up_entry.grid(row=1,column=6)
        self.up_entry.insert(0,self.up_key)

        Label(self, text="아래").grid(row=1,column=7)
        self.down_entry=Entry(self,width=10,justify=CENTER)
        self.down_entry.grid(row=1,column=8)
        self.down_entry.insert(0,self.down_key)

        Label(self, text="시계 회전").grid(row=2,column=0)
        self.h_right_entry=Entry(self,width=10,justify=CENTER)
        self.h_right_entry.grid(row=2,column=1)
        self.h_right_entry.insert(0,self.h_right_key)

        Label(self, text="반시계 회전").grid(row=2,column=3)
        self.h_left_entry=Entry(self,width=10,justify=CENTER)
        self.h_left_entry.grid(row=2,column=4)
        self.h_left_entry.insert(0,self.h_left_key)

        Label(self, text="  ").grid(row=3,column=0)
        Label(self, text="큐브 조작").grid(row=4,column=0)

        Label(self, text="R").grid(row=5,column=0)
        self.r_entry=Entry(self,width=10,justify=CENTER)
        self.r_entry.grid(row=5,column=1)
        self.r_entry.insert(0,self.R_key)

        Label(self, text="Rr").grid(row=5,column=3)
        self.rr_entry=Entry(self,width=10,justify=CENTER)
        self.rr_entry.grid(row=5,column=4)
        self.rr_entry.insert(0,self.RR_key)

        Label(self, text="L").grid(row=5,column=5)
        self.l_entry=Entry(self,width=10,justify=CENTER)
        self.l_entry.grid(row=5,column=6)
        self.l_entry.insert(0,self.L_key)

        Label(self, text="Lr").grid(row=5,column=7)
        self.lr_entry=Entry(self,width=10,justify=CENTER)
        self.lr_entry.grid(row=5,column=8)
        self.lr_entry.insert(0,self.LR_key)

        Label(self, text="U").grid(row=6,column=0)
        self.u_entry=Entry(self,width=10,justify=CENTER)
        self.u_entry.grid(row=6,column=1)
        self.u_entry.insert(0,self.U_key)

        Label(self, text="Ur").grid(row=6,column=3)
        self.ur_entry=Entry(self,width=10,justify=CENTER)
        self.ur_entry.grid(row=6,column=4)
        self.ur_entry.insert(0,self.UR_key)

        Label(self, text="D").grid(row=6,column=5)
        self.d_entry=Entry(self,width=10,justify=CENTER)
        self.d_entry.grid(row=6,column=6)
        self.d_entry.insert(0,self.D_key)

        Label(self, text="Dr").grid(row=6,column=7)
        self.dr_entry=Entry(self,width=10,justify=CENTER)
        self.dr_entry.grid(row=6,column=8)
        self.dr_entry.insert(0,self.DR_key)

        Label(self, text="F").grid(row=7,column=0)
        self.f_entry=Entry(self,width=10,justify=CENTER)
        self.f_entry.grid(row=7,column=1)
        self.f_entry.insert(0,self.F_key)

        Label(self, text="Fr").grid(row=7,column=3)
        self.fr_entry=Entry(self,width=10,justify=CENTER)
        self.fr_entry.grid(row=7,column=4)
        self.fr_entry.insert(0,self.FR_key)

        Label(self, text="B").grid(row=7,column=5)
        self.b_entry=Entry(self,width=10,justify=CENTER)
        self.b_entry.grid(row=7,column=6)
        self.b_entry.insert(0,self.B_key)

        Label(self, text="Br").grid(row=7,column=7)
        self.br_entry=Entry(self,width=10,justify=CENTER)
        self.br_entry.grid(row=7,column=8)
        self.br_entry.insert(0,self.BR_key)
        
        Label(self,text="sensitivity").grid(row=8,column=0)
        self.sens_entry=Entry(self,width=10,justify=CENTER)
        self.sens_entry.grid(row=8,column=1)
        self.sens_entry.insert(0,self.sens)

        Label(self, text=" ").grid(row=9,column=0)
        Button(self,text="기본값",command=self.reset).grid(row=10,column=6)
        Button(self,text="적용",command=self.apply).grid(row=10,column=7)
        Button(self,text="나가기",command=self.master.destroy).grid(row=10,column=8)
    
    def reset(self):
        global right_key,left_key,up_key,down_key,h_right_key,h_left_key,R_key,RR_key,L_key,LR_key,U_key,UR_key,D_key,DR_key,F_key,FR_key,B_key,BR_key
        global sens
        right_key="l"
        left_key="j"
        up_key="i"
        down_key="k"
        h_right_key="o"
        h_left_key="u"
        R_key="d"
        RR_key="c"
        L_key="s"
        LR_key="x"
        U_key="w"
        UR_key="e"
        D_key="z"
        DR_key="v"
        F_key="f"
        FR_key="a"
        B_key="q"
        BR_key="r"
        sens=180

        self.right_entry.delete(0,END)
        self.left_entry.delete(0,END)
        self.up_entry.delete(0,END)
        self.down_entry.delete(0,END)
        self.h_right_entry.delete(0,END)
        self.h_left_entry.delete(0,END)
        self.r_entry.delete(0,END)
        self.rr_entry.delete(0,END)
        self.l_entry.delete(0,END)
        self.lr_entry.delete(0,END)
        self.u_entry.delete(0,END)
        self.ur_entry.delete(0,END)
        self.d_entry.delete(0,END)
        self.dr_entry.delete(0,END)
        self.f_entry.delete(0,END)
        self.fr_entry.delete(0,END)
        self.b_entry.delete(0,END)
        self.br_entry.delete(0,END)
        self.sens_entry.delete(0,END)

        self.right_entry.insert(0,"l")
        self.left_entry.insert(0,"j")
        self.up_entry.insert(0,"i")
        self.down_entry.insert(0,"k")
        self.h_right_entry.insert(0,"o")
        self.h_left_entry.insert(0,"u")
        self.r_entry.insert(0,"d")
        self.rr_entry.insert(0,"c")
        self.l_entry.insert(0,"s")
        self.lr_entry.insert(0,"x")
        self.u_entry.insert(0,"w")
        self.ur_entry.insert(0,"e")
        self.d_entry.insert(0,"z")
        self.dr_entry.insert(0,"v")
        self.f_entry.insert(0,"f")
        self.fr_entry.insert(0,"a")
        self.b_entry.insert(0,"q")
        self.br_entry.insert(0,"r")
        self.sens_entry.insert(0,"180")

    def apply(self):
        global right_key,left_key,up_key,down_key,h_right_key,h_left_key,R_key,RR_key,L_key,LR_key,U_key,UR_key,D_key,DR_key,F_key,FR_key,B_key,BR_key
        global sens
        right_key=self.right_entry.get()
        left_key=self.left_entry.get()
        up_key=self.up_entry.get()
        down_key=self.down_entry.get()
        h_right_key=self.h_right_entry.get()
        h_left_key=self.h_left_entry.get()
        R_key=self.r_entry.get()
        RR_key=self.rr_entry.get()
        L_key=self.l_entry.get()
        LR_key=self.lr_entry.get()
        U_key=self.u_entry.get()
        UR_key=self.ur_entry.get()
        D_key=self.d_entry.get()
        DR_key=self.dr_entry.get()
        F_key=self.f_entry.get()
        FR_key=self.fr_entry.get()
        B_key=self.b_entry.get()
        BR_key=self.br_entry.get()
        sens=int(self.sens_entry.get())
def setting():
    global right_key,left_key,up_key,down_key,h_right_key,h_left_key,R_key,RR_key,L_key,LR_key,U_key,UR_key,D_key,DR_key,F_key,FR_key,B_key,BR_key
    global sens
    set_win=Toplevel(root)
    set_win.title("Setting")
    set_win.geometry("700x600")
    App(set_win,right_key,left_key,up_key,down_key,h_right_key,h_left_key,R_key,RR_key,L_key,LR_key,U_key,UR_key,D_key,DR_key,F_key,FR_key,B_key,BR_key,sens)
def keyboard(event):
    global right_key,left_key,up_key,down_key,h_right_key,h_left_key,R_key,RR_key,L_key,LR_key,U_key,UR_key,D_key,DR_key,F_key,FR_key,B_key,BR_key
    global can
    global a,b,c,d,e,f
    global mode
    if mode==0 or mode==1:
        if event.char==right_key:
            pr_right(can,a,b,c,d,e,f)
        elif event.char==left_key:
            pr_left(can,a,b,c,d,e,f)
        elif event.char==up_key:
            pr_up(can,a,b,c,d,e,f)
        elif event.char==down_key:
            pr_down(can,a,b,c,d,e,f)
        elif event.char==h_right_key:
            pr_h_right(can,a,b,c,d,e,f)
        elif event.char==h_left_key:
            pr_h_left(can,a,b,c,d,e,f)
        elif event.char==R_key:
            pr_R(can,a,b,c,d,e,f)
        elif event.char==RR_key:
            pr_RR(can,a,b,c,d,e,f)
        elif event.char==L_key:
            pr_L(can,a,b,c,d,e,f)
        elif event.char==LR_key:
            pr_LR(can,a,b,c,d,e,f)
        elif event.char==U_key:
            pr_U(can,a,b,c,d,e,f)
        elif event.char==UR_key:
            pr_UR(can,a,b,c,d,e,f)
        elif event.char==D_key:
            pr_D(can,a,b,c,d,e,f)
        elif event.char==DR_key:
            pr_DR(can,a,b,c,d,e,f)
        elif event.char==F_key:
            pr_F(can,a,b,c,d,e,f)
        elif event.char==FR_key:
            pr_FR(can,a,b,c,d,e,f)
        elif event.char==B_key:
            pr_B(can,a,b,c,d,e,f)
        elif event.char==BR_key:
            pr_BR(can,a,b,c,d,e,f)

#3d
def pr_cube3(canv, a_coor, b_coor, c_coor, d_coor, e_coor, f_coor,a,b,c,d,e,f):

    ue, fe, se = edge_list(a_coor,b_coor,c_coor,d_coor,e_coor,f_coor)

    f00 = canv.create_polygon(fe[0][0], fe[0][1], fe[4][0], fe[4][1], fe[5][0], fe[5][1], fe[1][0], fe[1][1], fill=b[0][0], outline='black')
    f01 = canv.create_polygon(fe[4][0], fe[4][1], fe[8][0], fe[8][1], fe[9][0], fe[9][1], fe[5][0], fe[5][1], fill=b[0][1], outline='black')
    f02 = canv.create_polygon(fe[8][0], fe[8][1], fe[12][0], fe[12][1], fe[13][0], fe[13][1], fe[9][0], fe[9][1], fill=b[0][2], outline='black')
    f10 = canv.create_polygon(fe[1][0], fe[1][1], fe[5][0], fe[5][1], fe[6][0], fe[6][1], fe[2][0], fe[2][1], fill=b[1][0], outline='black')
    f11 = canv.create_polygon(fe[5][0], fe[5][1], fe[9][0], fe[9][1], fe[10][0], fe[10][1], fe[6][0], fe[6][1], fill=b[1][1], outline='black')
    f12 = canv.create_polygon(fe[9][0], fe[9][1], fe[13][0], fe[13][1], fe[14][0], fe[14][1], fe[10][0], fe[10][1], fill=b[1][2], outline='black')
    f20 = canv.create_polygon(fe[2][0], fe[2][1], fe[6][0], fe[6][1], fe[7][0], fe[7][1], fe[3][0], fe[3][1], fill=b[2][0], outline='black')
    f21 = canv.create_polygon(fe[6][0], fe[6][1], fe[10][0], fe[10][1], fe[11][0], fe[11][1], fe[7][0], fe[7][1], fill=b[2][1], outline='black')
    f22 = canv.create_polygon(fe[10][0], fe[10][1], fe[14][0], fe[14][1], fe[15][0], fe[15][1], fe[11][0], fe[11][1], fill=b[2][2], outline='black')

    if a_coor[2]<f_coor[2]:
        u00 = canv.create_polygon(ue[0][0], ue[0][1], ue[4][0], ue[4][1], ue[5][0], ue[5][1], ue[1][0], ue[1][1], fill=a[0][0], outline='black')
        u01 = canv.create_polygon(ue[4][0], ue[4][1], ue[8][0], ue[8][1], ue[9][0], ue[9][1], ue[5][0], ue[5][1], fill=a[0][1], outline='black')
        u02 = canv.create_polygon(ue[8][0], ue[8][1], ue[12][0], ue[12][1], ue[13][0], ue[13][1], ue[9][0], ue[9][1], fill=a[0][2], outline='black')
        u10 = canv.create_polygon(ue[1][0], ue[1][1], ue[5][0], ue[5][1], ue[6][0], ue[6][1], ue[2][0], ue[2][1], fill=a[1][0], outline='black')
        u11 = canv.create_polygon(ue[5][0], ue[5][1], ue[9][0], ue[9][1], ue[10][0], ue[10][1], ue[6][0], ue[6][1], fill=a[1][1], outline='black')
        u12 = canv.create_polygon(ue[9][0], ue[9][1], ue[13][0], ue[13][1], ue[14][0], ue[14][1], ue[10][0], ue[10][1], fill=a[1][2], outline='black')
        u20 = canv.create_polygon(ue[2][0], ue[2][1], ue[6][0], ue[6][1], ue[7][0], ue[7][1], ue[3][0], ue[3][1], fill=a[2][0], outline='black')
        u21 = canv.create_polygon(ue[6][0], ue[6][1], ue[10][0], ue[10][1], ue[11][0], ue[11][1], ue[7][0], ue[7][1], fill=a[2][1], outline='black')
        u22 = canv.create_polygon(ue[10][0], ue[10][1], ue[14][0], ue[14][1], ue[15][0], ue[15][1], ue[11][0], ue[11][1], fill=a[2][2], outline='black')

    else:
        u00 = canv.create_polygon(ue[0][0], ue[0][1], ue[4][0], ue[4][1], ue[5][0], ue[5][1], ue[1][0], ue[1][1], fill=f[0][0], outline='black')
        u01 = canv.create_polygon(ue[4][0], ue[4][1], ue[8][0], ue[8][1], ue[9][0], ue[9][1], ue[5][0], ue[5][1], fill=f[0][1], outline='black')
        u02 = canv.create_polygon(ue[8][0], ue[8][1], ue[12][0], ue[12][1], ue[13][0], ue[13][1], ue[9][0], ue[9][1], fill=f[0][2], outline='black')
        u10 = canv.create_polygon(ue[1][0], ue[1][1], ue[5][0], ue[5][1], ue[6][0], ue[6][1], ue[2][0], ue[2][1], fill=f[1][0], outline='black')
        u11 = canv.create_polygon(ue[5][0], ue[5][1], ue[9][0], ue[9][1], ue[10][0], ue[10][1], ue[6][0], ue[6][1], fill=f[1][1], outline='black')
        u12 = canv.create_polygon(ue[9][0], ue[9][1], ue[13][0], ue[13][1], ue[14][0], ue[14][1], ue[10][0], ue[10][1], fill=f[1][2], outline='black')
        u20 = canv.create_polygon(ue[2][0], ue[2][1], ue[6][0], ue[6][1], ue[7][0], ue[7][1], ue[3][0], ue[3][1], fill=f[2][0], outline='black')
        u21 = canv.create_polygon(ue[6][0], ue[6][1], ue[10][0], ue[10][1], ue[11][0], ue[11][1], ue[7][0], ue[7][1], fill=f[2][1], outline='black')
        u22 = canv.create_polygon(ue[10][0], ue[10][1], ue[14][0], ue[14][1], ue[15][0], ue[15][1], ue[11][0], ue[11][1], fill=f[2][2], outline='black')

    if c_coor[2]<e_coor[2]:
        s00 = canv.create_polygon(se[0][0], se[0][1], se[4][0], se[4][1], se[5][0], se[5][1], se[1][0], se[1][1], fill=c[0][0], outline='black')
        s01 = canv.create_polygon(se[4][0], se[4][1], se[8][0], se[8][1], se[9][0], se[9][1], se[5][0], se[5][1], fill=c[0][1], outline='black')
        s02 = canv.create_polygon(se[8][0], se[8][1], se[12][0], se[12][1], se[13][0], se[13][1], se[9][0], se[9][1], fill=c[0][2], outline='black')
        s10 = canv.create_polygon(se[1][0], se[1][1], se[5][0], se[5][1], se[6][0], se[6][1], se[2][0], se[2][1], fill=c[1][0], outline='black')
        s11 = canv.create_polygon(se[5][0], se[5][1], se[9][0], se[9][1], se[10][0], se[10][1], se[6][0], se[6][1], fill=c[1][1], outline='black')
        s12 = canv.create_polygon(se[9][0], se[9][1], se[13][0], se[13][1], se[14][0], se[14][1], se[10][0], se[10][1], fill=c[1][2], outline='black')
        s20 = canv.create_polygon(se[2][0], se[2][1], se[6][0], se[6][1], se[7][0], se[7][1], se[3][0], se[3][1], fill=c[2][0], outline='black')
        s21 = canv.create_polygon(se[6][0], se[6][1], se[10][0], se[10][1], se[11][0], se[11][1], se[7][0], se[7][1], fill=c[2][1], outline='black')
        s22 = canv.create_polygon(se[10][0], se[10][1], se[14][0], se[14][1], se[15][0], se[15][1], se[11][0], se[11][1], fill=c[2][2], outline='black')
    
    else:
        s00 = canv.create_polygon(se[0][0], se[0][1], se[4][0], se[4][1], se[5][0], se[5][1], se[1][0], se[1][1], fill=e[0][0], outline='black')
        s01 = canv.create_polygon(se[4][0], se[4][1], se[8][0], se[8][1], se[9][0], se[9][1], se[5][0], se[5][1], fill=e[0][1], outline='black')
        s02 = canv.create_polygon(se[8][0], se[8][1], se[12][0], se[12][1], se[13][0], se[13][1], se[9][0], se[9][1], fill=e[0][2], outline='black')
        s10 = canv.create_polygon(se[1][0], se[1][1], se[5][0], se[5][1], se[6][0], se[6][1], se[2][0], se[2][1], fill=e[1][0], outline='black')
        s11 = canv.create_polygon(se[5][0], se[5][1], se[9][0], se[9][1], se[10][0], se[10][1], se[6][0], se[6][1], fill=e[1][1], outline='black')
        s12 = canv.create_polygon(se[9][0], se[9][1], se[13][0], se[13][1], se[14][0], se[14][1], se[10][0], se[10][1], fill=e[1][2], outline='black')
        s20 = canv.create_polygon(se[2][0], se[2][1], se[6][0], se[6][1], se[7][0], se[7][1], se[3][0], se[3][1], fill=e[2][0], outline='black')
        s21 = canv.create_polygon(se[6][0], se[6][1], se[10][0], se[10][1], se[11][0], se[11][1], se[7][0], se[7][1], fill=e[2][1], outline='black')
        s22 = canv.create_polygon(se[10][0], se[10][1], se[14][0], se[14][1], se[15][0], se[15][1], se[11][0], se[11][1], fill=e[2][2], outline='black')
def mat3_edge(m1,m2,m3):
    coor=[0]*3
    coor[0]=m1[0]+m2[0]+m3[0]
    coor[1]=m1[1]+m2[1]+m3[1]
    coor[2]=m1[2]+m2[2]+m3[2]
    return coor
def edge_list(a,b,c,d,e,f):
    up_edge=[0]*16
    f_edge=[0]*16
    side_edge=[0]*16
    if a[2]<f[2]:
        up_edge[0],up_edge[3],up_edge[12],up_edge[15]=mat3_edge(a,d,e),mat3_edge(a,c,d),mat3_edge(a,e,b),mat3_edge(a,b,c)
    else:
        up_edge[0],up_edge[3],up_edge[12],up_edge[15]=mat3_edge(b,e,f),mat3_edge(b,c,f),mat3_edge(e,d,f),mat3_edge(c,d,f)
    f_edge[0],f_edge[3],f_edge[12],f_edge[15]=mat3_edge(a,e,b),mat3_edge(a,b,c),mat3_edge(b,e,f),mat3_edge(b,c,f)
    if c[2]<e[2]:
        side_edge[0],side_edge[3],side_edge[12],side_edge[15]=mat3_edge(a,b,c),mat3_edge(a,c,d),mat3_edge(b,c,f),mat3_edge(c,d,f)
    else: 
        side_edge[0],side_edge[3],side_edge[12],side_edge[15]=mat3_edge(a,e,b),mat3_edge(a,e,d),mat3_edge(e,b,f),mat3_edge(e,d,f)
    
    ue=edge_point_list(up_edge)
    fe=edge_point_list(f_edge)
    se=edge_point_list(side_edge)
    
    return ue,fe,se
def edge_point_list(li):
    global o_coor
    li[1]=[int((li[0][0]*2+li[3][0])/3)+o_coor[0],int((li[0][1]*2+li[3][1])/3)+o_coor[1]]
    li[2]=[int((li[0][0]+li[3][0]*2)/3)+o_coor[0],int((li[0][1]+li[3][1]*2)/3)+o_coor[1]]

    li[4]=[int((li[0][0]*2+li[12][0])/3)+o_coor[0],int((li[0][1]*2+li[12][1])/3)+o_coor[1]]
    li[8]=[int((li[0][0]+li[12][0]*2)/3)+o_coor[0],int((li[0][1]+li[12][1]*2)/3)+o_coor[1]]

    li[7]=[int((li[3][0]*2+li[15][0])/3)+o_coor[0],int((li[3][1]*2+li[15][1])/3)+o_coor[1]]
    li[11]=[int((li[3][0]+li[15][0]*2)/3)+o_coor[0],int((li[3][1]+li[15][1]*2)/3)+o_coor[1]]

    li[13]=[int((li[12][0]*2+li[15][0])/3)+o_coor[0],int((li[12][1]*2+li[15][1])/3)+o_coor[1]]
    li[14]=[int((li[12][0]+li[15][0]*2)/3)+o_coor[0],int((li[12][1]+li[15][1]*2)/3)+o_coor[1]]

    li[5]=[int((li[0][0]*2+li[15][0])/3)+o_coor[0],int((li[0][1]*2+li[15][1])/3)+o_coor[1]]
    li[6]=[int((li[12][0]+li[3][0]*2)/3)+o_coor[0],int((li[12][1]+li[3][1]*2)/3)+o_coor[1]]

    li[9]=[int((li[12][0]*2+li[3][0])/3)+o_coor[0],int((li[12][1]*2+li[3][1])/3)+o_coor[1]]
    li[10]=[int((li[0][0]+li[15][0]*2)/3)+o_coor[0],int((li[0][1]+li[15][1]*2)/3)+o_coor[1]]

    li[0]=[li[0][0]+o_coor[0],li[0][1]+o_coor[1]]
    li[3]=[li[3][0]+o_coor[0],li[3][1]+o_coor[1]]
    li[12]=[li[12][0]+o_coor[0],li[12][1]+o_coor[1]]
    li[15]=[li[15][0]+o_coor[0],li[15][1]+o_coor[1]]
    
    return li

def set_click(event):
    global x0,y0
    x0,y0=event.x,event.y
def mat3_mul(m1,m2):
    coor=[0]*3
    coor[0]=m1[0][0]*m2[0]+m1[0][1]*m2[1]+m1[0][2]*m2[2]
    coor[1]=m1[1][0]*m2[0]+m1[1][1]*m2[1]+m1[1][2]*m2[2]
    coor[2]=m1[2][0]*m2[0]+m1[2][1]*m2[1]+m1[2][2]*m2[2]
    return coor
def spin(event):
    can.delete("all")
    global sens
    global x0,y0
    global a,b,c,d,e,f,li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor

    #rotational transform
    if event.x>x0:
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor=y_spin(-(pi/sens),a_coor,b_coor,c_coor,d_coor,e_coor,f_coor)

    elif event.x<x0:
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor=y_spin((pi/sens),a_coor,b_coor,c_coor,d_coor,e_coor,f_coor)

    if event.y>y0:
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor=x_spin((pi/sens),a_coor,b_coor,c_coor,d_coor,e_coor,f_coor)

    elif event.y<y0:
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor=x_spin(-(pi/sens),a_coor,b_coor,c_coor,d_coor,e_coor,f_coor)

    #spint the cube
    if c_coor[2]<b_coor[2]:
        a,b,c,d,e,f=left(a,b,c,d,e,f)
        li.append(13)
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor = a_coor,c_coor,d_coor,e_coor,b_coor,f_coor
    if e_coor[2]<b_coor[2]:
        a,b,c,d,e,f=right(a,b,c,d,e,f)
        li.append(12)
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor = a_coor,e_coor,b_coor,c_coor,d_coor,f_coor
    if a_coor[2]<b_coor[2]:
        a,b,c,d,e,f=down(a,b,c,d,e,f)
        li.append(15)
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor = d_coor,a_coor,c_coor,f_coor,e_coor,b_coor
    if f_coor[2]<b_coor[2]:
        a,b,c,d,e,f=up(a,b,c,d,e,f)
        li.append(14)
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor = b_coor,f_coor,c_coor,a_coor,e_coor,d_coor
    if c_coor[1]<a_coor[1]:
        a,b,c,d,e,f=h_left(a,b,c,d,e,f)
        li.append(17)
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor = c_coor,b_coor,f_coor,d_coor,a_coor,e_coor
    if e_coor[1]<a_coor[1]:
        a,b,c,d,e,f=h_right(a,b,c,d,e,f)
        li.append(16)
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor = e_coor,b_coor,a_coor,d_coor,f_coor,c_coor


    pr_cube3(can,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
    x0,y0=event.x,event.y
def y_spin(theta,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor):
    maty=[[cos(theta),0,sin(theta)],[0,1,0],[-sin(theta),0,cos(theta)]]
    ac=mat3_mul(maty,a_coor)
    bc=mat3_mul(maty,b_coor)
    cc=mat3_mul(maty,c_coor)
    dc=mat3_mul(maty,d_coor)
    ec=mat3_mul(maty,e_coor)
    fc=mat3_mul(maty,f_coor)
    return ac,bc,cc,dc,ec,fc
def x_spin(theta,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor):
    matx=[[1,0,0],[0,cos(theta),-sin(theta)],[0,sin(theta),cos(theta)]]
    ac=mat3_mul(matx,a_coor)
    bc=mat3_mul(matx,b_coor)
    cc=mat3_mul(matx,c_coor)
    dc=mat3_mul(matx,d_coor)
    ec=mat3_mul(matx,e_coor)
    fc=mat3_mul(matx,f_coor)
    return ac,bc,cc,dc,ec,fc


def coor_reset():
    a_coor=[0,-120,0]
    b_coor=[0,0,-120]
    c_coor=[120,0,0]
    d_coor=[0,0,120]
    e_coor=[-120,0,0]
    f_coor=[0,120,0]
    return a_coor,b_coor,c_coor,d_coor,e_coor,f_coor







def norm_main(canv):
    global mode,mode2
    if ta_stat==2:
        mode2=0
    else:
        mode=0
    global root
    global timestr, elapsedtime
    if not ta_stat==2:
        right_button.place(x = 980, y = 390)
        left_button.place(x = 820, y = 390)
        up_button.place(x = 910, y = 300)
        down_button.place(x = 910, y = 460)
        h_right_button.place(x = 980, y = 300)
        h_left_button.place(x = 820, y = 300)
        R_button.place(x = 720, y = 280)
        RR_button.place(x = 720, y = 350)
        L_button.place(x = 375, y = 290)
        LR_button.place(x= 375, y = 360)
        U_button.place(x = 550, y = 155)
        UR_button.place(x = 630, y = 155)
        D_button.place(x = 455, y = 470)
        DR_button.place(x = 530, y = 470)
        F_button.place(x = 635, y = 445)
        FR_button.place(x = 375, y = 450)
        B_button.place(x = 720, y = 200)
        BR_button.place(x = 410, y = 200)

    canv.delete("all")
    global a,b,c,d,e,f
    global f_icon, fr_icon, b_icon, br_icon, l_icon, lr_icon, r_icon, rr_icon, u_icon, ur_icon, d_icon, dr_icon
    pr_cube(can,a,b,c,d,e,f)
    normal_button.place_forget()
    real_button.place(x = 20, y = 100)
    canv.unbind("<Button-1>")
    canv.unbind("<B1-Motion>")


def real_main(canv):
    global mode,mode2
    if ta_stat==2:
        mode2=1
    else:
        mode=1
    global o_coor,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    global root
    global timestr, elapsedtime
    canv.delete("all")
    global a,b,c,d,e,f
    global f_icon, fr_icon, b_icon, br_icon, l_icon, lr_icon, r_icon, rr_icon, u_icon, ur_icon, d_icon, dr_icon
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
    real_button.place_forget()
    right_button.place_forget()
    left_button.place_forget()
    up_button.place_forget()
    down_button.place_forget()
    h_right_button.place_forget()
    h_left_button.place_forget()
    R_button.place_forget()
    RR_button.place_forget()
    L_button.place_forget()
    LR_button.place_forget()
    U_button.place_forget()
    UR_button.place_forget()
    D_button.place_forget()
    DR_button.place_forget()
    F_button.place_forget()
    FR_button.place_forget()
    B_button.place_forget()
    BR_button.place_forget()
    normal_button.place(x = 20, y = 100)
    canv.bind("<Button-1>",set_click)
    canv.bind("<B1-Motion>",spin)


#timer
def update_time(): 
    global root, elapsedtime, start, stop, timer
    elapsedtime = time() - start
    set_time(elapsedtime)
    timer = root.after(50, update_time)

def set_time(elap):
    global run, timestr
    minutes = int(elap/60)
    seconds = int(elap - minutes*60.0)
    hseconds = int((elap - minutes*60.0 - seconds)*100)
    timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

def start_time():
    global run, start, elapsedtime
    if not run:
        start = time() - elapsedtime
        update_time()
        run = True


def stop_time():
    global root, elapsedtime, timer, start, run
    set_time(elapsedtime)
    if run:
        root.after_cancel(timer)
        elapsedtime = time() - start
        set_time(elapsedtime)
        run = False


def reset_time():
    global start, elapsedtime
    start = time()
    elapsedtime = 0.0
    set_time(elapsedtime)

def get_time(elap):
    minutes = int(elap/60)
    seconds = int(elap - minutes*60.0)
    hseconds = int((elap - minutes*60.0 - seconds)*100)
    
    return minutes, seconds, hseconds


#time_Attack
def time_attack(a1,b1,c1,d1,e1,f1):
    global a,b,c,d,e,f
    global can
    global mode,mode2
    global ta_stat
    ta_stat=2
    a,b,c,d,e,f=shuffle(a1,b1,c1,d1,e1,f1)
    if mode==1:
        global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
        mode2=1
        can.delete("all")
        pr_cube3(can,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
        
    elif mode==0:
        mode2=0
        can.delete("all")
        pr_cube(can,a,b,c,d,e,f)
        
    mode=2
    right_button.place_forget()
    left_button.place_forget()
    up_button.place_forget()
    down_button.place_forget()
    h_right_button.place_forget()
    h_left_button.place_forget()
    R_button.place_forget()
    RR_button.place_forget()
    L_button.place_forget()
    LR_button.place_forget()
    U_button.place_forget()
    UR_button.place_forget()
    D_button.place_forget()
    DR_button.place_forget()
    F_button.place_forget()
    FR_button.place_forget()
    B_button.place_forget()
    BR_button.place_forget()
    shuffle_button.pack_forget()
    reset_button.pack_forget()
    undo_button.pack_forget()
    start_time_button.place_forget()
    stop_time_button.place_forget()
    reset_time_button.place_forget()
    ta_button.place_forget()
    ta_start.place(x=315,y=50)

def time_attack_start(a,b,c,d,e,f):
    global mode,mode2
    global ta_stat
    ta_stat=1
    mode=mode2
    ta_start.place_forget()
    undo_button.place(x = 1000, y = 600)
    if mode==0:
        right_button.place(x = 980, y = 390)
        left_button.place(x = 820, y = 390)
        up_button.place(x = 910, y = 300)
        down_button.place(x = 910, y = 460)
        h_right_button.place(x = 980, y = 300)
        h_left_button.place(x = 820, y = 300)
        R_button.place(x = 720, y = 280)
        RR_button.place(x = 720, y = 350)
        L_button.place(x = 375, y = 290)
        LR_button.place(x= 375, y = 360)
        U_button.place(x = 550, y = 155)
        UR_button.place(x = 630, y = 155)
        D_button.place(x = 455, y = 470)
        DR_button.place(x = 530, y = 470)
        F_button.place(x = 635, y = 445)
        FR_button.place(x = 375, y = 450)
        B_button.place(x = 720, y = 200)
        BR_button.place(x = 410, y = 200)
    
    undo_button.pack(side="bottom")
    shuffle_button.pack(side="bottom")
    reset_button.pack(side="bottom")
    start_time()
    ta_stop.place(x=315,y=50)
    ta_skip.place(x=200,y=50)
    
def txt_get():
    t=open("boardname.txt","r")
    a=t.readlines()
    t.close()
    b=len(a)
    for i in range(b):
        a[i]=str(a[i])
    return a
def txt_get_int():
    t=open("boardtime.txt","r")
    a=t.readlines()
    t.close()
    b=len(a)
    for i in range(b):
        a[i]=float(a[i])
    return a

def time_attack_finish():
    global a,b,c
    global ta_stat
    global elapsedtime
    
    if cube_check(a,b,c):
        stop_time()
        ta_stop.place_forget()
        ta_button.place(x=300,y=50)
        leaderboard=elapsedtime
        save_txt(leaderboard)
        reset_time()
        ta_stat=0
        timer_text.place(x=500, y=30)
        start_time_button.place(x=30,y=150)
        stop_time_button.place(x=30,y=200)
        reset_time_button.place(x=30,y=250)
        
    else:
        start_time()


def ta_skip():
    stop_time()
    ta_skip.place_forget()
    ta_stop.place_forget()
    ta_button.place(x=300,y=50)
    reset_time()
    start_time_button.place(x=30,y=150)
    stop_time_button.place(x=30,y=200)
    reset_time_button.place(x=30,y=250)


def save_txt(elap):
    win=Toplevel(root)
    win.title("Save")
    win.geometry("500x400")
    n=txt_get()
    t=txt_get_int()
    st(win,elap,t,n)

class st(Frame):
    def __init__(self,master,elap,score_l,name_l):
        super().__init__(master)
        self.place(x=50,y=100)
        self.elap=elap
        
        self.score_l=score_l
        self.name_l=name_l
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="name").grid(row=0,column=0)

        self.name_entry=Entry(self,width=20,justify=CENTER)
        self.name_entry.grid(row=0,column=1)
        self.app_b=Button(self,text="apply",command=self.apply)
        self.app_b.grid(row=0,column=2)
        self.summary=Text(self,width=40,height=10,wrap=WORD)
        self.summary.grid(row=1,column=0,columnspan=3,sticky=S)
    def bubble_sort(self,list1,list2):
        n0=len(list1)
        for i in range(n0-1):
            for j in range(0,n0-i-1):
                if (list1[j]>list1[j+1]):
                    b=list1[j]
                    list1[j]=list1[j+1]
                    list1[j+1]=b
                    c=list2[j]
                    list2[j]=list2[j+1]
                    list2[j+1]=c
        return list1,list2
    
    def apply(self):
        self.name=self.name_entry.get()
        t=open("boardname.txt","a")
        t.write(str(self.name)+"\n")
        t.close()
        s=open("boardtime.txt","a")
        s.write(str(self.elap)+"\n")
        s.close()
        self.app_b.grid_forget()
        self.score_l.append(self.elap)
        self.name_l.append(self.name)
        self.score,self.name=self.bubble_sort(self.score_l,self.name_l)
        print(self.name)
        print(self.score)
        self.nn=len(self.name)
        self.m,self.s,self.hs=0,0,0
        self.m,self.s,self.hs=get_time(self.score[0])
        summary=str(self.name[0])
        for i in range(1,self.nn):
            self.m,self.s,self.hs=get_time(self.score[i])
            summary+=str(i)+" "+str(self.name[i])+" "+str(self.m)+str(" ")+str(self.s)+str(" ")+str(self.hs)+str("\n")
        self.summary.delete(0.0,END)
        self.summary.insert(0.0,summary)


#leaderboard
def leader():
    wind=Toplevel(root)
    wind.title("LeaderBoard")
    wind.geometry("400x650")
    name_list=txt_get()
    time_list=txt_get_int()
    ld(wind,name_list,time_list)
    
class ld(Frame):
    def __init__(self,master,name_l,time_l):
        super().__init__(master)
        self.place(x=40,y=30)
        self.name_l=name_l
        self.time_l=time_l
        self.create_widgets()

    def create_widgets(self):
        self.summary=Text(self,width=40,height=33,wrap=WORD)
        self.summary.grid(row=0,column=0,columnspan=3,sticky=S)
        self.score,self.name=self.bubble_sort(self.time_l,self.name_l)
        self.nn=len(self.name)
        self.m,self.s,self.hs=0,0,0
        self.m,self.s,self.hs=get_time(self.score[0])
        summary=str(self.name[0])
        for i in range(1,self.nn):
            self.m,self.s,self.hs=get_time(self.score[i])
            summary+=str(i)+" "+str(self.name[i])+" "+str(self.m)+str(" ")+str(self.s)+str(" ")+str(self.hs)+str("\n")
        self.summary.delete(0.0,END)
        self.summary.insert(0.0,summary)

    def bubble_sort(self,list1,list2):
        n0=len(list1)
        for i in range(n0-1):
            for j in range(0,n0-i-1):
                if (list1[j]>list1[j+1]):
                    b=list1[j]
                    list1[j]=list1[j+1]
                    list1[j+1]=b
                    c=list2[j]
                    list2[j]=list2[j+1]
                    list2[j+1]=c
        return list1,list2
    
    

################################################################


sens=180
right_key="l"
left_key="j"
up_key="i"
down_key="k"
h_right_key="o"
h_left_key="u"
R_key="d"
RR_key="c"
L_key="s"
LR_key="x"
U_key="w"
UR_key="e"
D_key="z"
DR_key="v"
F_key="f"
FR_key="a"
B_key="q"
BR_key="r"


ta_stat=0
mode=0
mode2=0

li=[]
a,b,c,d,e,f=reset()
o_coor=[600,400,0]
a_coor,b_coor,c_coor,d_coor,e_coor,f_coor = coor_reset()
x0,y0=0,0

root=Tk()
root.title("Cube")
root.geometry('1080x768')
    


can=Canvas(root, bg="white", width = 3000,  height = 3000)
can.place(x=0, y=0)


#keyboard shortcut
frame=Frame(root)
frame.bind("<Key>",keyboard)
frame.pack()
frame.focus_set()




right_button= Button(text = "right",  command=lambda:pr_right(can,a,b,c,d,e,f))
left_button= Button(text = "left", command=lambda:pr_left(can,a,b,c,d,e,f))
up_button= Button(text = "up",command=lambda:pr_up(can,a,b,c,d,e,f))
down_button= Button(text = "down",  command=lambda:pr_down(can,a,b,c,d,e,f))
h_right_button= Button(text = "h_right", command=lambda:pr_h_right(can,a,b,c,d,e,f))
h_left_button= Button(text = "h_left",  command=lambda:pr_h_left(can,a,b,c,d,e,f))
R_button= Button(text = "R", command=lambda:pr_R(can,a,b,c,d,e,f))
RR_button= Button(text = "RR", command=lambda:pr_RR(can,a,b,c,d,e,f))
L_button= Button(text = "L",  command=lambda:pr_L(can,a,b,c,d,e,f))
LR_button= Button(text = "LR",  command=lambda:pr_LR(can,a,b,c,d,e,f))
U_button= Button(text = "U",  command=lambda:pr_U(can,a,b,c,d,e,f))
UR_button= Button(text = "UR",  command=lambda:pr_UR(can,a,b,c,d,e,f))
D_button= Button(text = "D",  command=lambda:pr_D(can,a,b,c,d,e,f))
DR_button= Button(text = "DR",  command=lambda:pr_DR(can,a,b,c,d,e,f))
F_button= Button(text = "F",  command=lambda:pr_F(can,a,b,c,d,e,f))
FR_button= Button(text = "FR", command=lambda:pr_FR(can,a,b,c,d,e,f))
B_button= Button(text = "B", command=lambda:pr_B(can,a,b,c,d,e,f))
BR_button= Button(text = "BR",  command=lambda:pr_BR(can,a,b,c,d,e,f))
shuffle_button= Button(text = "shuffle",  command=lambda:pr_shuffle(can,a,b,c,d,e,f))
reset_button= Button(text = "reset",  command=lambda:pr_reset(can))
undo_button= Button( text = "undo",command=lambda:undo(can,a,b,c,d,e,f))
setting_button=Button(text="key setting",  command=setting)
normal_button = Button(text="2D",  command=lambda:norm_main(can))
real_button = Button(text="Reality Mode", command=lambda:real_main(can))
leader_button = Button(text="leaderboard", command=leader)



ta_button = Button(text="Time Attack", command=lambda:time_attack(a,b,c,d,e,f))
ta_start = Button(text="Start", command=lambda:time_attack_start(a,b,c,d,e,f))
ta_stop = Button(text="stop",command=time_attack_finish)
ta_skip = Button(text="skip",command=ta_skip)

start_time_button = Button(text='Start', command = start_time)
stop_time_button = Button(text='Stop', command = stop_time)
reset_time_button = Button(text='Reset', command = reset_time)

#time variables
start = 0.0
elapsedtime = 0.0
timer=0.0
run = False
timestr = StringVar()

global timer_text
timer_text = Label(textvariable = timestr, font = ("Arial","40"))
set_time(elapsedtime)
timer_text.place(x=500, y=30)
start_time_button.place(x=30,y=150)
stop_time_button.place(x=30,y=200)
reset_time_button.place(x=30,y=250)
right_button.place(x = 980, y = 390)
left_button.place(x = 820, y = 390)
up_button.place(x = 910, y = 300)
down_button.place(x = 910, y = 460)
h_right_button.place(x = 980, y = 300)
h_left_button.place(x = 820, y = 300)
R_button.place(x = 720, y = 280)
RR_button.place(x = 720, y = 350)
L_button.place(x = 375, y = 290)
LR_button.place(x= 375, y = 360)
U_button.place(x = 550, y = 155)
UR_button.place(x = 630, y = 155)
D_button.place(x = 455, y = 470)
DR_button.place(x = 530, y = 470)
F_button.place(x = 635, y = 445)
FR_button.place(x = 375, y = 450)
B_button.place(x = 720, y = 200)
BR_button.place(x = 410, y = 200)
undo_button.pack(side="bottom")
setting_button.pack(side="bottom")
shuffle_button.pack(side="bottom")
reset_button.pack(side="bottom")
ta_button.place(x=300,y=50)
real_button.place(x = 20, y = 100)
leader_button.place(x=20, y=700)


pr_cube(can,a,b,c,d,e,f)
root.mainloop()                                                                                 #여기도 이미있음
