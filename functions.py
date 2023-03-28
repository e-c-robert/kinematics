import math
import guiWindow as g
import tkinter as tk

def m_xf(key1):
    x1,v1,th,time,forcew,mass = key1
    a = float(forcew)/float(mass)
    rad = float(th)*(180/math.pi)
    x2 = float(x1)+ (float(v1)*float(time)*math.cos(rad)) + (0.5*a*(float(time)**2))
    return x2


def m_yf(key2):
    y1,v2,the,time1 = key2
    y2 = float(y1)+ (float(v2)*float(the)*float(time1)) +(-0.5*9.81*(float(time1)**2))
    return y2 
   
def m_m(key3):
    fw1,t1,xf1,xi1,vi1,th1 = key3
    denom = float(fw1)*(float(t1)**2)*0.5
    rad = float(th1)*(180/math.pi)
    num = float(xf1)-float(xi1) - (float(vi1)*math.cos(rad) *float(t1))
    m = num/denom
    return m 

def m_t(key4):
    vi,theta,fw,m,sf,si,s = key4
    #T = -(vi)*cos(th) + sqrt((vi*cos(th))^2+2*(a*(X))/(fw/m)
    rad = float(theta)*(180/math.pi)
    if s == 'x':
        a = 0.5*(float(fw)/float(m))
        b = -float(vi)*math.cos(rad)
    elif s == 'y': 
        a = -0.5*9.81
        b = -float(vi)*math.sin(rad)
    c = float(sf)-float(si)
    squ = (b**2) + (4*a*c)
    square = math.sqrt(squ)
    t1 = (b+square)/(2*a)
    t2 = (b-square)/(2*a)
    if t1<0 and t2>0:
        return t2
    elif t2<0 and t1>0 :
        return t1
    elif t2<t1 and t2>0 :
        return t2
    elif t1<t2 and t1>0 :
        return t1
    
def check():
    #gets inputs from all boxes 
    vi = g.vientry.get()
    vf = g.vfentry.get()
    theta = g.tentry.get()
    xi = g.xientry.get()
    xf = g.xfentry.get()
    yi = g.yientry.get()
    yf = g.yfentry.get()
    t = g.tientry.get()
    fw = g.wentry.get()
    m = g.mentry.get()

    global allvar
    global strallvar
    
    #list of all variables and their string form so that i cna call the correct index in places 
    allvar = [vi, vf, theta, xi, xf, yi, yf, t, fw, m]
    strallvar = ['vi', 'vf','theta','xi','xf','yi','yf','t','fw','m']

    #emplty list of inputs to be added in the next for loop 
    inputs = []
    
    fcount = 0
    
    #adds to the input list 
    for index, val in enumerate(allvar):
        if val == 'find':
            inputs.append(val)
            fcount+=1
        elif val != '':
            inputs.append(allvar[index])
        else :
            inputs.append('')
          
    
    #list if there is a independent variable that needs to be solved for first
    backtrack = []

    global strrequires
    global requires
    global functions 
    strrequires = {'vi': [], 
                   'vf': [], 
                   'theta': [], 
                   'xi': [], 
                   'xf':['xi','vi','theta','t','fw','m', 6],
                   'yi': [],
                   'yf':['yi','vi','theta','t',4], 
                   't': ['vi','theta','fw','m','xf','xi', 6],
                   # ,['vi','theta','fw','m','yf','yi', 6]],
                   'fw':[],
                   'm':['fw','t','xf','xi','vi','theta',6]}
    requires = {'vi': [], 
                'vf': [], 
                'theta': [], 
                'xi': [], 
                'xf':[xi,vi,theta,t,fw,m],
                'yi': [],
                'yf':[yi,vi,theta,t], 
                't': [vi,theta,fw,m,xf,xi, 'x'],
                      # [vi,theta,fw,m,yf,yi, 'y']],
                'fw':[],
                'm':[fw,t,xf,xi,vi,theta]}
    functions = ['', 
                 '', 
                 '', 
                 '', 
                 m_xf,
                 '',
                 m_yf, 
                 m_t,
                 '',
                 m_m]
    for ind1, value1, in enumerate(inputs):
        if value1 == 'find':
            key1 = strrequires[strallvar[ind1]]
            count1 = 0
            for i,v in enumerate(inputs):
                if strallvar[i] in key1 and v != '' and v!='find' and v!= 'expected':
                    count1 += 1
                elif strallvar[i] in key1 and v == 'find' and i != ind1: 
                    backtrack.append(i)
                    break
                if count1 != key1[-1] and backtrack != [] and fcount==2:
                    inputs[ind1] = 'expected'
                    continue 
            if fcount == 2 and count1 == key1[-1]:
                ans = functions[ind1](requires[strallvar[ind1]])
                inputs[ind1] = functions[ind1](requires[strallvar[ind1]])
                answer = tk.Label(g.window, text=strallvar[ind1] + ': ' + str(ans), 
                                  fg = 'blue')
                answer.grid(row = 16, column = 1, sticky = 'w')
                fcount = 1
            elif fcount == 1 and count1==key1[-1]:
                ans = functions[ind1](requires[strallvar[ind1]])
                inputs[ind1] = functions[ind1](requires[strallvar[ind1]])
                answer = tk.Label(g.window, text=strallvar[ind1] + ': ' + str(ans), 
                                  fg = 'blue')
                answer.grid(row = 16, column = 0, sticky = 'w')
                        
    if backtrack != [] :
        for place in backtrack :
            key2 = strrequires[strallvar[ind1]]
            count = 0
            for i1,v1 in enumerate(inputs):
                if strallvar[i1] in key2 and v1!= '' and v1!='find' and v1!= 'expected':
                    count +=1
            if count == key2[-1]:
                ans1 = functions[place](requires[strallvar[place]])
                inputs[place] = functions[place](requires[strallvar[place]])
                answer = tk.Label(g.window, text=strallvar[place] + ': ' + str(ans1), 
                                  fg = 'blue')
                answer.grid(row = 16, column = 0, sticky = 'w')
