import math

#calculation functions 
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
    #if statement checks if the given numbers are for the x or y direction 
    #the direction changes the trig and acceleration 
    if key4[-1] == 'x':
        vi,theta,fw,m,sf,si,s = key4
        rad = float(theta)*(180/math.pi)
        a = 0.5*(float(fw)/float(m))
        b = -float(vi)*math.cos(rad)
    elif key4[-1] == 'y': 
        vi,theta, sf,si,s = key4
        rad = float(theta)*(180/math.pi)
        a = -0.5*9.81
        b = -float(vi)*math.sin(rad)
    c = float(sf)-float(si)
    squ = (b**2) + (4*a*c)
    square = math.sqrt(squ)
    t1 = (b+square)/(2*a)
    t2 = (b-square)/(2*a)
    #if statement to check the results bc quadratic gives 2 results 
    if t1<0 and t2>0:
        return t2
    elif t2<0 and t1>0 :
        return t1
    elif t2<t1 and t2>0 :
        return t2
    elif t1<t2 and t1>0 :
        return t1
    
def m_fw(key5):
    xf,xi,vi,th,t,m = key5
    term1 = float(xf)-float(xi)
    rad = float(th)*(180/math.pi)
    term2 = float(vi)*math.cos(rad)*float(t)
    fw = (term1-term2)*2*float(m)*(float(t)**(-2))
    return fw