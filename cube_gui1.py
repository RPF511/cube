from tkinter import*
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
    com_list = [random.randint(0,11) for i in range(20)]
    for i in range(20):
        a,b,c,d,e,f=run_shuf(a,b,c,d,e,f,com_list[i])
    li=[]
    pr_cube(canv, a, b, c, d, e, f)
def undo(canv,a1,b1,c1,d1,e1,f1):
    canv.delete("all")
    global li
    global a
    global b
    global c
    global d
    global e
    global f
    if len(li)==0:
        print("no command to undo!")
    elif li[-1]==12:
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



li=[]
a,b,c,d,e,f=reset()
root=Tk()
root.title("Cube")
root.geometry('1080x768')
can=Canvas(root,bg="white",height=700,width=1000)
pr_cube(can,a,b,c,d,e,f)
can.pack()
right_button= Button(text="right",command=lambda:pr_right(can,a,b,c,d,e,f))
right_button.pack(side="left")
left_button= Button(text="left",command=lambda:pr_left(can,a,b,c,d,e,f))
left_button.pack(side="left")
up_button= Button(text="up",command=lambda:pr_up(can,a,b,c,d,e,f))
up_button.pack(side="left")
down_button= Button(text="down",command=lambda:pr_down(can,a,b,c,d,e,f))
down_button.pack(side="left")
h_right_button= Button(text="h_right",command=lambda:pr_h_right(can,a,b,c,d,e,f))
h_right_button.pack(side="left")
h_left_button= Button(text="h_left",command=lambda:pr_h_left(can,a,b,c,d,e,f))
h_left_button.pack(side="left")
R_button= Button(text="R",command=lambda:pr_R(can,a,b,c,d,e,f))
R_button.pack(side="right")
RR_button= Button(text="RR",command=lambda:pr_RR(can,a,b,c,d,e,f))
RR_button.pack(side="right")
L_button= Button(text="L",command=lambda:pr_L(can,a,b,c,d,e,f))
L_button.pack(side="right")
LR_button= Button(text="LR",command=lambda:pr_LR(can,a,b,c,d,e,f))
LR_button.pack(side="right")
U_button= Button(text="U",command=lambda:pr_U(can,a,b,c,d,e,f))
U_button.pack(side="right")
UR_button= Button(text="UR",command=lambda:pr_UR(can,a,b,c,d,e,f))
UR_button.pack(side="right")
D_button= Button(text="D",command=lambda:pr_D(can,a,b,c,d,e,f))
D_button.pack(side="right")
DR_button= Button(text="DR",command=lambda:pr_DR(can,a,b,c,d,e,f))
DR_button.pack(side="right")
F_button= Button(text="F",command=lambda:pr_F(can,a,b,c,d,e,f))
F_button.pack(side="right")
FR_button= Button(text="FR",command=lambda:pr_FR(can,a,b,c,d,e,f))
FR_button.pack(side="right")
B_button= Button(text="B",command=lambda:pr_B(can,a,b,c,d,e,f))
B_button.pack(side="right")
BR_button= Button(text="BR",command=lambda:pr_BR(can,a,b,c,d,e,f))
BR_button.pack(side="right")
undo_button= Button(text="undo",command=lambda:undo(can,a,b,c,d,e,f))
undo_button.pack(side="bottom")
shuffle_button= Button(text="shuffle",command=lambda:shuffle(can,a,b,c,d,e,f))
shuffle_button.pack(side="bottom")
reset_button= Button(text="reset",command=lambda:pr_reset(can))
reset_button.pack(side="bottom")
root.mainloop()