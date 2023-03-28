import math as m
import guiWindow as g
import tkinter as tk

def m_xf(key1):
    x1,v1,th,time,forcew,mass = key1
    a = float(forcew)/float(mass)
    rad = float(th)*(180/m.pi)
    x2 = float(x1)+ (float(v1)*float(time)*m.cos(rad)) + (0.5*a*(float(time)**2))
    return x2


def m_yf(key2):
    y1,v2,the,time1 = key2
    y2 = float(y1)+ (float(v2)*float(the)*float(time1)) +(-0.5*9.81*(float(time1)**2))
    return y2

    
    
def check():
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
    global strrequires
    global requires
    global functions 
    allvar = [vi, vf, theta, xi, xf, yi, yf, t, fw, m]
    strallvar = ['vi', 'vf','theta','xi','xf','yi','yf','t','fw','m']
    strrequires = {'vi': [], 
                   'vf': [], 
                   'theta': [], 
                   'xi': [], 
                   'xf':['xi','vi','theta','t','fw','m', 6],
                   'yi': [],
                   'yf':['yi','vi','theta','t',4], 
                   't': [],
                   'fw':[],
                   'm':[]}
    requires = {'vi': [], 
                'vf': [], 
                'theta': [], 
                'xi': [], 
                'xf':[xi,vi,theta,t,fw,m],
                'yi': [],
                'yf':[yi,vi,theta,t], 
                't': [],
                'fw':[],
                'm':[]}
    functions = ['', 
                 '', 
                 '', 
                 '', 
                  m_xf,
                  '',
                  m_yf, 
                 '',
                 '',
                 '']

    inputs = []
    for index, val in enumerate(allvar):
        # fcount = 0
        if val != '':
            inputs.append(allvar[index])
        elif val == 'find': 
            inputs.append(val)
            # fcount+=1
        else :
            inputs.append('')
  #modify to include for 2 unknown but one has to be solved for first           
    for ind, value, in enumerate(inputs):
        if value == 'find':
            key = strrequires[strallvar[ind]]
            count = 0
            for i,v in enumerate(inputs):
                if strallvar[i] in key and v != '':
                    count += 1
            if key[-1] != count:
                print(f'error more information required, ensure that {key} inputs are filled')
            else: 
                ans = functions[ind](requires[strallvar[ind]])
                answer = tk.Label(g.window, text=strallvar[ind] + ': ' + str(ans), 
                                  fg = 'blue')
                answer.grid(row = 14, column = 0, columnspan = 2, sticky = 'w')