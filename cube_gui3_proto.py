from tkinter import*
from math import*
#기본 명령어 모음

def reset():
    a = [["white", "white", "white"], ["white", "white", "white"], ["white", "white", "white"]]
    b = [["red", "red", "red"], ["red", "red", "red"], ["red", "red", "red"]]
    c = [["blue", "blue", "blue"], ["blue", "blue", "blue"], ["blue", "blue", "blue"]]
    d = [["#FC9B1B", "#FC9B1B", "#FC9B1B"], ["#FC9B1B", "#FC9B1B", "#FC9B1B"], ["#FC9B1B", "#FC9B1B",  "#FC9B1B"]]
    e = [["green", "green", "green"], ["green", "green", "green"], ["green", "green", "green"]]
    f = [["yellow", "yellow", "yellow"], ["yellow", "yellow", "yellow"], ["yellow", "yellow", "yellow"]]
    return a,b,c,d,e,f
def right(a,b,c,d,e,f):
    h=[[],[],[]]
    g=[[],[],[]]
    i=[e[2],e[1],e[0]]
    h[0]=[d[0][2],d[0][1],d[0][0]]#e
    h[1]=[d[1][2],d[1][1],d[1][0]]#e
    h[2]=[d[2][2],d[2][1],d[2][0]]#e
    g[0]=[c[2][2],c[2][1],c[2][0]]#d
    g[1]=[c[1][2],c[1][1],c[1][0]]#d
    g[2]=[c[0][2],c[0][1],c[0][0]]#d
    a0, a1, a2 = a[0], a[1], a[2]
    a[0] = [a2[0], a1[0], a0[0]]
    a[1] = [a2[1], a1[1], a0[1]]
    a[2] = [a2[2], a1[2], a0[2]]
    f0, f1, f2 = f[0], f[1], f[2]
    f[0] = [f0[2], f1[2], f2[2]]
    f[1] = [f0[1], f1[1], f2[1]]
    f[2] = [f0[0], f1[0], f2[0]]
    return a,i,b,g,h,f
def left(a,b,c,d,e,f):#시점전환 - 큐브 자체를 왼쪽으로 돌린다
    g = [[], [], []]#바꾸고 난 c
    h = [[], [], []]#바꾸고 난 d
    i = [b[2],b[1],b[0]]#바꾸고 난 e
    g[0]=[d[2][2],d[2][1],d[2][0]]
    g[1]=[d[1][2],d[1][1],d[1][0]]
    g[2]=[d[0][2],d[0][1],d[0][0]]
    h[0]=[e[0][2],e[0][1],e[0][0]]
    h[1]=[e[1][2],e[1][1],e[1][0]]
    h[2]=[e[2][2],e[2][1],e[2][0]]
    a0, a1, a2 = a[0], a[1], a[2]
    a[0] = [a0[2], a1[2], a2[2]]
    a[1] = [a0[1], a1[1], a2[1]]
    a[2] = [a0[0], a1[0], a2[0]]
    f0, f1, f2 = f[0], f[1], f[2]
    f[0] = [f2[0], f1[0], f0[0]]
    f[1] = [f2[1], f1[1], f0[1]]
    f[2] = [f2[2], f1[2], f0[2]]
    return a,c,g,h,i,f
def up(a,b,c,d,e,f):#시점전환 - 큐브 자체를 위로 돌린다
    c0,c1,c2=c[0],c[1],c[2]
    c[0]=[c0[2],c1[2],c2[2]]
    c[1]=[c0[1],c1[1],c2[1]]
    c[2]=[c0[0],c1[0],c2[0]]
    e0,e1,e2=e[0],e[1],e[2]
    e[0] = [e0[2], e1[2], e2[2]]
    e[1] = [e0[1], e1[1], e2[1]]
    e[2] = [e0[0], e1[0], e2[0]]
    return b,f,c,a,e,d
def down(a,b,c,d,e,f):#시점전환 - 큐브 자체를 아래로 돌린다
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
def shuffle(canv,a1,b1,c1,d1,e1,f1):
    import random
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    com_list = [random.randint(0,11) for i in range(30)]
    for i in range(30):
        a,b,c,d,e,f=run_shuf(a,b,c,d,e,f,com_list[i])
    li=[]
    pr_cube(canv, a, b, c, d, e, f)
def undo(canv,a1,b1,c1,d1,e1,f1):
    
    global li
    global a
    global b
    global c
    global d
    global e
    global f
    if len(li)==0:
        print("no command to undo!")
    else:
        canv.delete("all")
        if li[-1]==12:
            a, b, c, d, e, f = left(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==13:
            a, b, c, d, e, f = right(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==14:
            a, b, c, d, e, f = down(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==15:
            a, b, c, d, e, f = up(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==16:
            a, b, c, d, e, f = h_left(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==17:
            a, b, c, d, e, f = h_right(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==0:
            a, b, c, d, e, f = RR(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==1:
            a, b, c, d, e, f = R(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==2:
            a, b, c, d, e, f = LR(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==3:
            a, b, c, d, e, f = L(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==4:
            a, b, c, d, e, f = UR(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==5:
            a, b, c, d, e, f = U(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==6:
            a, b, c, d, e, f = DR(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==7:
            a, b, c, d, e, f = D(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==8:
            a, b, c, d, e, f = FR(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==9:
            a, b, c, d, e, f = F(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==10:
            a, b, c, d, e, f = BR(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        elif li[-1]==11:
            a, b, c, d, e, f = B(a1, b1, c1, d1, e1, f1)
            pr_cube(canv, a, b, c, d, e, f)
            li.pop(-1)
        else:
            li.pop(-1)



#GUI 명령어 모음
def pr_cube(canv, a, b, c, d, e, f):

        # 앞면의 블럭 한칸 가로세로 (50)
        # 앞면 블럭 간격 (5)
    b00 = canv.create_rectangle(500, 100, 550, 150, fill=b[0][0])
    b01 = canv.create_rectangle(500, 155, 550, 205, fill=b[0][1])
    b02 = canv.create_rectangle(500, 210, 550, 260, fill=b[0][2])
    b10 = canv.create_rectangle(555, 100, 605, 150, fill=b[1][0])
    b11 = canv.create_rectangle(555, 155, 605, 205, fill=b[1][1])
    b12 = canv.create_rectangle(555, 210, 605, 260, fill=b[1][2])
    b20 = canv.create_rectangle(610, 100, 660, 150, fill=b[2][0])
    b21 = canv.create_rectangle(610, 155, 660, 205, fill=b[2][1])
    b22 = canv.create_rectangle(610, 210, 660, 260, fill=b[2][2])

        # 오른면 블럭 가로(30) 세로(50) 우상상승폭(20)
        # 오른면 블럭 간격 가로세로(5) 우상상승폭(3)
    c00 = canv.create_polygon(665, 97, 665, 147, 695, 127, 695, 77, fill=c[0][0], outline='black')
    c01 = canv.create_polygon(665, 152, 665, 202, 695, 182, 695, 132, fill=c[0][1], outline='black')
    c02 = canv.create_polygon(665, 207, 665, 257, 695, 237, 695, 187, fill=c[0][2], outline='black')
    c10 = canv.create_polygon(700, 74, 700, 124, 730, 104, 730, 54, fill=c[1][0], outline='black')
    c11 = canv.create_polygon(700, 129, 700, 179, 730, 159, 730, 109, fill=c[1][1], outline='black')
    c12 = canv.create_polygon(700, 184, 700, 234, 730, 214, 730, 164, fill=c[1][2], outline='black')
    c20 = canv.create_polygon(735, 51, 735, 101, 765, 81, 765, 31, fill=c[2][0], outline='black')
    c21 = canv.create_polygon(735, 106, 735, 156, 765, 136, 765, 86, fill=c[2][1], outline='black')
    c22 = canv.create_polygon(735, 161, 735, 211, 765, 191, 765, 141, fill=c[2][2], outline='black')

        # 윗면 블럭 가로(50) 세로(30)
        # 윗면 블럭간격 가로(5) 세로(3)
    a00 = canv.create_polygon(570, 49, 620, 49, 650, 29, 600, 29, fill=a[0][0], outline='black')
    a01 = canv.create_polygon(535, 72, 585, 72, 615, 52, 565, 52, fill=a[0][1], outline='black')
    a02 = canv.create_polygon(500, 95, 550, 95, 580, 75, 530, 75, fill=a[0][2], outline='black')
    a10 = canv.create_polygon(625, 49, 675, 49, 705, 29, 655, 29, fill=a[1][0], outline='black')
    a11 = canv.create_polygon(590, 72, 640, 72, 670, 52, 620, 52, fill=a[1][1], outline='black')
    a12 = canv.create_polygon(555, 95, 605, 95, 635, 75, 585, 75, fill=a[1][2], outline='black')
    a20 = canv.create_polygon(680, 49, 730, 49, 760, 29, 710, 29, fill=a[2][0], outline='black')
    a21 = canv.create_polygon(645, 72, 695, 72, 725, 52, 675, 52, fill=a[2][1], outline='black')
    a22 = canv.create_polygon(610, 95, 660, 95, 690, 75, 640, 75, fill=a[2][2], outline='black')

        # 왼쪽면
    e00 = canv.create_polygon(65, 97, 65, 147, 95, 127, 95, 77, fill=e[0][0], outline='black')
    e01 = canv.create_polygon(65, 152, 65, 202, 95, 182, 95, 132, fill=e[0][1], outline='black')
    e02 = canv.create_polygon(65, 207, 65, 257, 95, 237, 95, 187, fill=e[0][2], outline='black')
    e10 = canv.create_polygon(100, 74, 100, 124, 130, 104, 130, 54, fill=e[1][0], outline='black')
    e11 = canv.create_polygon(100, 129, 100, 179, 130, 159, 130, 109, fill=e[1][1], outline='black')
    e12 = canv.create_polygon(100, 184, 100, 234, 130, 214, 130, 164, fill=e[1][2], outline='black')
    e20 = canv.create_polygon(135, 51, 135, 101, 165, 81, 165, 31, fill=e[2][0], outline='black')
    e21 = canv.create_polygon(135, 106, 135, 156, 165, 136, 165, 86, fill=e[2][1], outline='black')
    e22 = canv.create_polygon(135, 161, 135, 211, 165, 191, 165, 141, fill=e[2][2], outline='black')

        # 뒷면
    d00 = canv.create_rectangle(170, 138, 220, 188, fill=d[0][0])
    d01 = canv.create_rectangle(170, 83, 220, 133, fill=d[0][1])
    d02 = canv.create_rectangle(170, 28, 220, 78, fill=d[0][2])
    d10 = canv.create_rectangle(225, 138, 275, 188, fill=d[1][0])
    d11 = canv.create_rectangle(225, 83, 275, 133, fill=d[1][1])
    d12 = canv.create_rectangle(225, 28, 275, 78, fill=d[1][2])
    d20 = canv.create_rectangle(280, 138, 330, 188, fill=d[2][0])
    d21 = canv.create_rectangle(280, 83, 330, 133, fill=d[2][1])
    d22 = canv.create_rectangle(280, 28, 330, 78, fill=d[2][2])

        # 아랫면
    f00 = canv.create_polygon(70, 260, 120, 260, 150, 240, 100, 240, fill=f[0][0], outline='black')
    f01 = canv.create_polygon(105, 237, 155, 237, 185, 217, 135, 217, fill=f[0][1], outline='black')
    f02 = canv.create_polygon(140, 214, 190, 214, 220, 194, 170, 194, fill=f[0][2], outline='black')
    f10 = canv.create_polygon(125, 260, 175, 260, 205, 240, 155, 240, fill=f[1][0], outline='black')
    f11 = canv.create_polygon(160, 237, 210, 237, 240, 217, 190, 217, fill=f[1][1], outline='black')
    f12 = canv.create_polygon(195, 214, 245, 214, 275, 194, 225, 194, fill=f[1][2], outline='black')
    f20 = canv.create_polygon(180, 260, 230, 260, 260, 240, 210, 240, fill=f[2][0], outline='black')
    f21 = canv.create_polygon(215, 237, 265, 237, 295, 217, 245, 217, fill=f[2][1], outline='black')
    f22 = canv.create_polygon(250, 214, 300, 214, 330, 194, 280, 194, fill=f[2][2], outline='black')
def pr_right(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(12)
    a,b,c,d,e,f=right(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_left(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(13)
    a,b,c,d,e,f=left(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_up(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(14)
    a,b,c,d,e,f=up(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_down(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(15)
    a,b,c,d,e,f=down(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_h_right(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(16)
    a,b,c,d,e,f=h_right(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_h_left(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(17)
    a,b,c,d,e,f=h_left(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_R(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(0)
    a,b,c,d,e,f=R(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_RR(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(1)
    a,b,c,d,e,f=RR(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_L(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(2)
    a,b,c,d,e,f=L(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_LR(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(3)
    a,b,c,d,e,f=LR(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_U(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(4)
    a,b,c,d,e,f=U(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_UR(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(5)
    a,b,c,d,e,f=UR(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_D(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(6)
    a,b,c,d,e,f=D(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_DR(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(7)
    a,b,c,d,e,f=DR(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_F(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(8)
    a,b,c,d,e,f=F(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_FR(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(9)
    a,b,c,d,e,f=FR(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_B(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(10)
    a,b,c,d,e,f=B(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_BR(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li.append(11)
    a,b,c,d,e,f=BR(a1,b1,c1,d1,e1,f1)
    pr_cube(canv,a,b,c,d,e,f)
def pr_reset(canv):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    li=[]
    a,b,c,d,e,f=reset()
    pr_cube(canv,a,b,c,d,e,f)


def pr_R3(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    li.append(0)
    a,b,c,d,e,f=R(a1,b1,c1,d1,e1,f1)
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
def pr_RR3(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    li.append(1)
    a,b,c,d,e,f=RR(a1,b1,c1,d1,e1,f1)
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
def pr_L3(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    li.append(2)
    a,b,c,d,e,f=L(a1,b1,c1,d1,e1,f1)
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
def pr_LR3(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    li.append(3)
    a,b,c,d,e,f=LR(a1,b1,c1,d1,e1,f1)
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
def pr_U3(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    li.append(4)
    a,b,c,d,e,f=U(a1,b1,c1,d1,e1,f1)
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
def pr_UR3(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    li.append(5)
    a,b,c,d,e,f=UR(a1,b1,c1,d1,e1,f1)
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
def pr_D3(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    li.append(6)
    a,b,c,d,e,f=D(a1,b1,c1,d1,e1,f1)
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
def pr_DR3(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    li.append(7)
    a,b,c,d,e,f=DR(a1,b1,c1,d1,e1,f1)
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
def pr_F3(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    li.append(8)
    a,b,c,d,e,f=F(a1,b1,c1,d1,e1,f1)
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
def pr_FR3(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    li.append(9)
    a,b,c,d,e,f=FR(a1,b1,c1,d1,e1,f1)
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
def pr_B3(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    li.append(10)
    a,b,c,d,e,f=B(a1,b1,c1,d1,e1,f1)
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
def pr_BR3(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global a
    global b
    global c
    global d
    global e
    global f
    global li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    li.append(11)
    a,b,c,d,e,f=BR(a1,b1,c1,d1,e1,f1)
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)




class App(Frame):
    def __init__(self,master,right_key,left_key,up_key,down_key,h_right_key,h_left_key,R_key,RR_key,L_key,LR_key,U_key,UR_key,D_key,DR_key,F_key,FR_key,B_key,BR_key):
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
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="View Change").grid(row=0,column=0)
        
        Label(self, text="Right").grid(row=1,column=0)
        self.right_entry=Entry(self,width=10,justify=CENTER)
        self.right_entry.grid(row=1,column=1)
        self.right_entry.insert(0,self.right_key)

        Label(self, text="Left").grid(row=1,column=3)
        self.left_entry=Entry(self,width=10,justify=CENTER)
        self.left_entry.grid(row=1,column=4)
        self.left_entry.insert(0,self.left_key)

        Label(self, text="Up").grid(row=1,column=5)
        self.up_entry=Entry(self,width=10,justify=CENTER)
        self.up_entry.grid(row=1,column=6)
        self.up_entry.insert(0,self.up_key)

        Label(self, text="Down").grid(row=1,column=7)
        self.down_entry=Entry(self,width=10,justify=CENTER)
        self.down_entry.grid(row=1,column=8)
        self.down_entry.insert(0,self.down_key)

        Label(self, text="H_Right").grid(row=2,column=0)
        self.h_right_entry=Entry(self,width=10,justify=CENTER)
        self.h_right_entry.grid(row=2,column=1)
        self.h_right_entry.insert(0,self.h_right_key)

        Label(self, text="H_Left").grid(row=2,column=3)
        self.h_left_entry=Entry(self,width=10,justify=CENTER)
        self.h_left_entry.grid(row=2,column=4)
        self.h_left_entry.insert(0,self.h_left_key)

        Label(self, text="  ").grid(row=3,column=0)
        Label(self, text="Command").grid(row=4,column=0)

        Label(self, text="R").grid(row=5,column=0)
        self.r_entry=Entry(self,width=10,justify=CENTER)
        self.r_entry.grid(row=5,column=1)
        self.r_entry.insert(0,self.R_key)

        Label(self, text="R\'").grid(row=5,column=3)
        self.rr_entry=Entry(self,width=10,justify=CENTER)
        self.rr_entry.grid(row=5,column=4)
        self.rr_entry.insert(0,self.RR_key)

        Label(self, text="L").grid(row=5,column=5)
        self.l_entry=Entry(self,width=10,justify=CENTER)
        self.l_entry.grid(row=5,column=6)
        self.l_entry.insert(0,self.L_key)

        Label(self, text="L\'").grid(row=5,column=7)
        self.lr_entry=Entry(self,width=10,justify=CENTER)
        self.lr_entry.grid(row=5,column=8)
        self.lr_entry.insert(0,self.LR_key)

        Label(self, text="U").grid(row=6,column=0)
        self.u_entry=Entry(self,width=10,justify=CENTER)
        self.u_entry.grid(row=6,column=1)
        self.u_entry.insert(0,self.U_key)

        Label(self, text="U\'").grid(row=6,column=3)
        self.ur_entry=Entry(self,width=10,justify=CENTER)
        self.ur_entry.grid(row=6,column=4)
        self.ur_entry.insert(0,self.UR_key)

        Label(self, text="D").grid(row=6,column=5)
        self.d_entry=Entry(self,width=10,justify=CENTER)
        self.d_entry.grid(row=6,column=6)
        self.d_entry.insert(0,self.D_key)

        Label(self, text="D\'").grid(row=6,column=7)
        self.dr_entry=Entry(self,width=10,justify=CENTER)
        self.dr_entry.grid(row=6,column=8)
        self.dr_entry.insert(0,self.DR_key)

        Label(self, text="F").grid(row=7,column=0)
        self.f_entry=Entry(self,width=10,justify=CENTER)
        self.f_entry.grid(row=7,column=1)
        self.f_entry.insert(0,self.F_key)

        Label(self, text="F\'").grid(row=7,column=3)
        self.fr_entry=Entry(self,width=10,justify=CENTER)
        self.fr_entry.grid(row=7,column=4)
        self.fr_entry.insert(0,self.FR_key)

        Label(self, text="B").grid(row=7,column=5)
        self.b_entry=Entry(self,width=10,justify=CENTER)
        self.b_entry.grid(row=7,column=6)
        self.b_entry.insert(0,self.B_key)

        Label(self, text="B\'").grid(row=7,column=7)
        self.br_entry=Entry(self,width=10,justify=CENTER)
        self.br_entry.grid(row=7,column=8)
        self.br_entry.insert(0,self.BR_key)
        
        Label(self, text=" ").grid(row=8,column=0)
        Button(self,text="Reset",command=self.reset).grid(row=9,column=6)
        Button(self,text="Apply",command=self.apply).grid(row=9,column=7)
        Button(self,text="Quit",command=self.master.destroy).grid(row=9,column=8)

    def reset(self):
        global right_key
        global left_key
        global up_key
        global down_key
        global h_right_key
        global h_left_key
        global R_key
        global RR_key
        global L_key
        global LR_key
        global U_key
        global UR_key
        global D_key
        global DR_key
        global F_key
        global FR_key
        global B_key
        global BR_key
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

    def apply(self):
        global right_key
        global left_key
        global up_key
        global down_key
        global h_right_key
        global h_left_key
        global R_key
        global RR_key
        global L_key
        global LR_key
        global U_key
        global UR_key
        global D_key
        global DR_key
        global F_key
        global FR_key
        global B_key
        global BR_key
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

def bubble_sort(list1,list2):
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
    return list2

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


def setting():
    global right_key
    global left_key
    global up_key
    global down_key
    global h_right_key
    global h_left_key
    global R_key
    global RR_key
    global L_key
    global LR_key
    global U_key
    global UR_key
    global D_key
    global DR_key
    global F_key
    global FR_key
    global B_keys
    global BR_key
    set_win=Toplevel(root)
    set_win.title("Setting")
    set_win.geometry("800x700")
    App(set_win,right_key,left_key,up_key,down_key,h_right_key,h_left_key,R_key,RR_key,L_key,LR_key,U_key,UR_key,D_key,DR_key,F_key,FR_key,B_key,BR_key)
    
def keyboard(event):
    global right_key
    global left_key
    global up_key
    global down_key
    global h_right_key
    global h_left_key
    global R_key
    global RR_key
    global L_key
    global LR_key
    global U_key
    global UR_key
    global D_key
    global DR_key
    global F_key
    global FR_key
    global B_key
    global BR_key
    global can
    global a
    global b
    global c
    global d
    global e
    global f
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
def keyboard3(event):
    global right_key
    global left_key
    global up_key
    global down_key
    global h_right_key
    global h_left_key
    global R_key
    global RR_key
    global L_key
    global LR_key
    global U_key
    global UR_key
    global D_key
    global DR_key
    global F_key
    global FR_key
    global B_key
    global BR_key
    global can
    global a
    global b
    global c
    global d
    global e
    global f
    if event.char==right_key:
        pr_right3(can,a,b,c,d,e,f)
    elif event.char==left_key:
        pr_left3(can,a,b,c,d,e,f)
    elif event.char==up_key:
        pr_up3(can,a,b,c,d,e,f)
    elif event.char==down_key:
        pr_down3(can,a,b,c,d,e,f)
    elif event.char==h_right_key:
        pr_h_right3(can,a,b,c,d,e,f)
    elif event.char==h_left_key:
        pr_h_left3(can,a,b,c,d,e,f)
    elif event.char==R_key:
        pr_R3(can,a,b,c,d,e,f)
    elif event.char==RR_key:
        pr_RR3(can,a,b,c,d,e,f)
    elif event.char==L_key:
        pr_L3(can,a,b,c,d,e,f)
    elif event.char==LR_key:
        pr_LR3(can,a,b,c,d,e,f)
    elif event.char==U_key:
        pr_U3(can,a,b,c,d,e,f)
    elif event.char==UR_key:
        pr_UR3(can,a,b,c,d,e,f)
    elif event.char==D_key:
        pr_D3(can,a,b,c,d,e,f)
    elif event.char==DR_key:
        pr_DR3(can,a,b,c,d,e,f)
    elif event.char==F_key:
        pr_F3(can,a,b,c,d,e,f)
    elif event.char==FR_key:
        pr_FR3(can,a,b,c,d,e,f)
    elif event.char==B_key:
        pr_B3(can,a,b,c,d,e,f)
    elif event.char==BR_key:
        pr_BR3(can,a,b,c,d,e,f)

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

def first_page(canv):
    canv.delete("all")
    mode_button=Button(text="next",command=lambda:mod_select(canv))
    mode_button.place(x = 0, y = 723)

def mod_select(canv):
    canv.delete("all")
    normal_button=Button(text="normal mode",command=lambda:norm_main(can))
    normal_button.place(x = 0, y = 50)
    real_button=Button(text="real mode",command=lambda:real_main(can))
    real_button.place(x = 0, y= 100)

def norm_main(canv):
    global root
    canv.delete("all")
    global a,b,c,d,e,f
    global f_icon, fr_icon, b_icon, br_icon, l_icon, lr_icon, r_icon, rr_icon, u_icon, ur_icon, d_icon, dr_icon
    pr_cube(can,a,b,c,d,e,f)
    frame=Frame(root)
    frame.bind("<Key>",keyboard)
    frame.pack()
    frame.focus_set()
    
    right_button= Button(text="right",command=lambda:pr_right(can,a,b,c,d,e,f))
    right_button.place(x = 0, y = 723)
    left_button= Button(text="left",command=lambda:pr_left(can,a,b,c,d,e,f))
    left_button.place(x = 50, y = 723)
    up_button= Button(text="up",command=lambda:pr_up(can,a,b,c,d,e,f))
    up_button.place(x = 100, y = 723)
    down_button= Button(text="down",command=lambda:pr_down(can,a,b,c,d,e,f))
    down_button.place(x = 150, y = 723)
    h_right_button= Button(text="h_right",command=lambda:pr_h_right(can,a,b,c,d,e,f))
    h_right_button.place(x = 200, y = 723)
    h_left_button= Button(text="h_left",command=lambda:pr_h_left(can,a,b,c,d,e,f))
    h_left_button.place(x = 250, y = 723)
    R_button= Button(text= "R" ,command=lambda:pr_R(can,a,b,c,d,e,f))
    R_button.place(x = 485, y = 723)
    RR_button= Button(text= "RR",command=lambda:pr_RR(can,a,b,c,d,e,f))
    RR_button.place(x = 535, y = 723)
    L_button= Button(text="L",command=lambda:pr_L(can,a,b,c,d,e,f))
    L_button.place(x = 585, y = 723)
    LR_button= Button(text= "LR",command=lambda:pr_LR(can,a,b,c,d,e,f))
    LR_button.place(x=635, y = 723)
    U_button= Button(text= "U",command=lambda:pr_U(can,a,b,c,d,e,f))
    U_button.place(x = 685, y = 723)
    UR_button= Button(text= "UR",command=lambda:pr_UR(can,a,b,c,d,e,f))
    UR_button.place(x = 735, y = 723)
    D_button= Button(text= "D",command=lambda:pr_D(can,a,b,c,d,e,f))
    D_button.place(x = 785, y = 723)
    DR_button= Button(text= "DR",command=lambda:pr_DR(can,a,b,c,d,e,f))
    DR_button.place(x = 835, y = 723)
    F_button= Button(text= "F",command=lambda:pr_F(can,a,b,c,d,e,f))
    F_button.place(x = 885, y = 723)
    FR_button= Button(text= "FR",command=lambda:pr_FR(can,a,b,c,d,e,f))
    FR_button.place(x = 935, y = 723)
    B_button= Button(text="B",command=lambda:pr_B(can,a,b,c,d,e,f))
    B_button.place(x = 985, y = 723)
    BR_button= Button(text="BR",command=lambda:pr_BR(can,a,b,c,d,e,f))
    BR_button.place(x = 1035, y = 723)
    undo_button= Button(text="undo",command=lambda:undo(can,a,b,c,d,e,f))
    undo_button.place(x = 400, y = 690)
    shuffle_button= Button(text="shuffle",command=lambda:shuffle(can,a,b,c,d,e,f))
    shuffle_button.place(x = 400, y = 710)
    reset_button= Button(text="reset",command=lambda:pr_reset(can))
    reset_button.place(x = 400, y = 730)
    setting_button=Button(text="setting",command=setting)
    setting_button.place(x = 400, y = 750)



def mat3_mul(m1,m2):
    coor=[0]*3
    coor[0]=m1[0][0]*m2[0]+m1[0][1]*m2[1]+m1[0][2]*m2[2]
    coor[1]=m1[1][0]*m2[0]+m1[1][1]*m2[1]+m1[1][2]*m2[2]
    coor[2]=m1[2][0]*m2[0]+m1[2][1]*m2[1]+m1[2][2]*m2[2]
    return coor
def set_click(event):
    global x0,y0
    x0,y0=event.x,event.y

def spin(event):
    can.delete("all")
    global x0,y0
    global a,b,c,d,e,f,li
    global a_coor,b_coor,c_coor,d_coor,e_coor,f_coor

    #rotational transform
    if event.x>x0:
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor=y_spin(-(pi/180),a_coor,b_coor,c_coor,d_coor,e_coor,f_coor)

    elif event.x<x0:
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor=y_spin((pi/180),a_coor,b_coor,c_coor,d_coor,e_coor,f_coor)

    if event.y>y0:
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor=x_spin((pi/180),a_coor,b_coor,c_coor,d_coor,e_coor,f_coor)

    elif event.y<y0:
        a_coor,b_coor,c_coor,d_coor,e_coor,f_coor=x_spin(-(pi/180),a_coor,b_coor,c_coor,d_coor,e_coor,f_coor)

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


def real_main(canv):
    global o_coor,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor
    global root
    canv.delete("all")
    global a,b,c,d,e,f
    global f_icon, fr_icon, b_icon, br_icon, l_icon, lr_icon, r_icon, rr_icon, u_icon, ur_icon, d_icon, dr_icon
    pr_cube3(canv,a_coor,b_coor,c_coor,d_coor,e_coor,f_coor,a,b,c,d,e,f)
    frame=Frame(root)
    frame.bind("<Key>",keyboard3)
    frame.pack()
    frame.focus_set()
    canv.bind("<Button-1>",set_click)
    canv.bind("<B1-Motion>",spin)



def coor_reset():
    a_coor=[0,-120,0]
    b_coor=[0,0,-120]
    c_coor=[120,0,0]
    d_coor=[0,0,120]
    e_coor=[-120,0,0]
    f_coor=[0,120,0]
    return a_coor,b_coor,c_coor,d_coor,e_coor,f_coor

li=[]
a,b,c,d,e,f=reset()
o_coor=[500,400,0]
a_coor,b_coor,c_coor,d_coor,e_coor,f_coor = coor_reset()
x0,y0=0,0

root=Tk()
root.title("Cube")
root.geometry('1080x768')
can=Canvas(root,bg="white",height=768, width=1080)
can.place(x = 0, y = 0)



first_page(can)


root.mainloop()