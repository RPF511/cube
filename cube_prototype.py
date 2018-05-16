def reset():
    a = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
    b = [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
    c = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]
    d = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
    e = [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
    f = [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]
    return a,b,c,d,e,f
def pr_cube(a,b,c,d,e,f):
    print("   ", e[2][0], "  ", d[0][2], " ", d[1][2], " ", d[2][2], "           ")
    print(" ", e[1][0], e[2][1], "  ", d[0][1], " ", d[1][1], " ", d[2][1], "           ")
    print(e[0][0], e[1][1], e[2][2], "  ", d[0][0], " ", d[1][0], " ", d[2][0], "           ")
    print(e[0][1], e[1][2], "                    ")
    print(e[0][2], "    ", f[0][2], " ", f[1][2], " ", f[2][2], "    ", a[0][0], " ", a[1][0], " ", a[2][0], "   ")
    print("   ", f[0][1], " ", f[1][1], " ", f[2][1], "    ", a[0][1], " ", a[1][1], " ", a[2][1], "  ", c[2][0])
    print(" ", f[0][0], " ", f[1][0], " ", f[2][0], "    ", a[0][2], " ", a[1][2], " ", a[2][2], "  ", c[1][0], c[2][1])
    print("                           ", c[0][0], c[1][1], c[2][2], )
    print("               ", b[0][0], " ", b[1][0], " ", b[2][0], " ", c[0][1], c[1][2], "  ")
    print("               ", b[0][1], " ", b[1][1], " ", b[2][1], " ", c[0][2], "    ")
    print("               ", b[0][2], " ", b[1][2], " ", b[2][2], "       ")
    return 0
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
def shuffle(a,b,c,d,e,f):
    import random
    com_list = [random.randint(0,11) for i in range(20)]
    for i in range(20):
        a,b,c,d,e,f=run_shuf(a,b,c,d,e,f,com_list[i])
    li=[]
    return a,b,c,d,e,f,li
def undo(a,b,c,d,e,f,li):
    if len(li)==0:
        print("no command to undo!")
        return a,b,c,d,e,f,li
    elif li[-1]=='right':
        a,b,c,d,e,f=left(a,b,c,d,e,f)
        li.pop(-1)
        return a,b,c,d,e,f,li
    elif li[-1]=='left':
        a, b, c, d, e, f = right(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='up':
        a, b, c, d, e, f = down(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='down':
        a, b, c, d, e, f = up(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='h_right':
        a, b, c, d, e, f = h_left(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='h_left':
        a, b, c, d, e, f = h_right(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='r':
        a, b, c, d, e, f = RR(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='rr':
        a, b, c, d, e, f = R(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='l':
        a, b, c, d, e, f = LR(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='lr':
        a, b, c, d, e, f = L(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='u':
        a, b, c, d, e, f = UR(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='ur':
        a, b, c, d, e, f = U(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='d':
        a, b, c, d, e, f = DR(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='dr':
        a, b, c, d, e, f = D(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='f':
        a, b, c, d, e, f = FR(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='fr':
        a, b, c, d, e, f = F(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='b':
        a, b, c, d, e, f = BR(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    elif li[-1]=='br':
        a, b, c, d, e, f = B(a, b, c, d, e, f)
        li.pop(-1)
        return a, b, c, d, e, f, li
    else:
        li.pop(-1)
        return a, b, c, d, e, f, li
def main():
    com_list=[]
    a,b,c,d,e,f=reset()
    pr_cube(a, b, c, d, e, f)
    while True:
        key=input("input command. if you want to see the command list, input \'command list\'")
        while not (key=='stop' or key=='right' or key=='left' or key=='up' or key=='down' or key=='h_right' or key=='h_left' or key=='r' or key=='rr' or key=='l' or key=='lr' or key=='u' or key=='ur' or key=='d' or key=='dr' or key=='f' or key=='fr' or key=='b' or key=='br' or key=='command list' or key=='reset' or key=='shuffle' or key=='undo'):
            key = input("input command. if you want to know the command, input \'command list\'")
        if not (key == 'command list' or key == 'reset' or key == 'shuffle' or key == 'undo' or key == 'stop'):
            com_list.append(key)
        if (key=='stop'):
            break
        elif (key=='right'):
            a,b,c,d,e,f=right(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key=='left'):
            a, b, c, d, e, f =left(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key=='up'):
            a, b, c, d, e, f =up(a, b, c, d, e, f)
            pr_cube(a, b, c, d, e, f)
        elif (key=='down'):
            a, b, c, d, e, f =down(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key=='h_right'):
            a, b, c, d, e, f =h_right(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key=='h_left'):
            a, b, c, d, e, f =h_left(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key=='r'):
            a, b, c, d, e, f =R(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key=='rr'):
            a, b, c, d, e, f =RR(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key=='l'):
            a, b, c, d, e, f =L(a, b, c, d, e, f)
            pr_cube(a, b, c, d, e, f)
        elif (key=='lr'):
            a, b, c, d, e, f =LR(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key=='u'):
            a, b, c, d, e, f =U(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key == 'ur'):
            a, b, c, d, e, f =UR(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key == 'd'):
            a, b, c, d, e, f =D(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key == 'dr'):
            a, b, c, d, e, f =DR(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key == 'f'):
            a, b, c, d, e, f =F(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key == 'fr'):
            a, b, c, d, e, f =FR(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key == 'b'):
            a, b, c, d, e, f =B(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key == 'br'):
            a, b, c, d, e, f =BR(a,b,c,d,e,f)
            pr_cube(a, b, c, d, e, f)
        elif (key=='reset'):
            a, b, c, d, e, f = reset()
            pr_cube(a, b, c, d, e, f)
        elif (key=='command list'):
            print("change the view - \'right\', \'left\', \'up\', \'down\', \'h_right\', \'h_left\'")
            print("move - \'r\', \'rr\', \'l\', \'lr\', \'u\', \'ur\', \'d\', \'dr\', \'f\', \'fr\', \'b\', \'br\'")
            print("if you want to shuffle, input \'shuffle\'")
            print("if you want to stop, input \'stop\'")
            print("if you want to reset, input \'reset\'")
        elif (key=='shuffle'):
            a,b,c,d,e,f,com_list=shuffle(a,b,c,d,e,f)
            pr_cube(a,b,c,d,e,f)
        elif (key=='undo'):
            a,b,c,d,e,f,com_list=undo(a,b,c,d,e,f,com_list)
            pr_cube(a,b,c,d,e,f)
main()
