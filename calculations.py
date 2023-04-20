iimport math

#finds the computers machine epsilon so we can actually get a 0 answer 
#found this out the hard way 
def zero(ans5):
    ep = 1

    while ((ep / 2) + 1 > 1):
        ep /= 2
        
    if isinstance(ans5, str) == True:
        return ans5
    elif abs(ans5) <= ep:
        return 0
    else:
        return ans5

#calculation functions 
def m_xf(key1):
    x1, v1, theta, time, forcew, mass = key1
    a = float(forcew) / float(mass)
    rad = math.radians(float(theta))
    x2 = float(x1) + (float(v1)*float(time)*math.cos(rad)) + (0.5*a*(float(time)**2))
    return x2

def m_yf(key2):
    y1, v2, theta, time1 = key2
    rad = math.radians(float(theta))
    y2 = float(y1) + (float(v2)*math.sin(rad)*float(time1)) + (-0.5*9.81*(float(time1)**2))
    return y2 
   
def m_m(key3):
    fw1, t1, xf1, xi1, vi1, th1 = key3
    denom = float(fw1)*(float(t1)**2)*0.5
    rad = math.radians(float(th1))
    num = float(xf1) - float(xi1) - (float(vi1)*math.cos(rad)*float(t1))
    m = num / denom
    return m 

def m_t(key4):
    if key4[-1]=='x' or key4[-1]=='y':
        #if statement checks if the given numbers are for the x or y direction 
        #the direction changes the trig and acceleration 
        if key4[-1] == 'x':
            vi, theta, fw, m, sf, si, s = key4
            rad = math.radians(float(theta))
            a = 0.5*(float(fw)/float(m))
            b = -float(vi)*math.cos(rad)
        
        elif key4[-1] == 'y': 
            vi, theta, sf, si, s = key4
            rad = math.radians(float(theta))
            a = -0.5*9.81
            b = -float(vi)*math.sin(rad)
        
        c = float(sf) - float(si)
        squ = (b**2) + (4*a*c)
        square = math.sqrt(squ)
        t1 = (b + square) / (2*a)
        t2 = (b - square) / (2*a)
        #if statement to check the results bc quadratic gives 2 results 
        if t1 < 0 and t2 > 0:
            return t2
        elif t2 < 0 and t1 > 0 :
            return t1
        elif t2 < t1 and t2 > 0 :
            return t2
        elif t1 < t2 and t1 > 0 :
            return t1
       
def m_fw(key5):
    xf, xi, vi, theta, t, m = key5
    term1 = float(xf) - float(xi)
    rad = math.radians(float(theta))
    term2 = float(vi)*math.cos(rad)*float(t)
    fw = (term1 - term2)*2*float(m)*(float(t)**(-2))
    return fw

def m_xi(key):
    vi, theta, t, fw, m, xf = key 
    a = float(fw) / float(m)
    rad = math.radians(float(theta))
    term1 = -float(vi)*math.cos(rad)*float(t)
    term2 = -0.5*a*(float(t)**2)
    xi = term1 + term2 + float(xf)
    return xi 

def m_yi(key):
    vi, theta, t, yf = key 
    a = -9.81
    rad = math.radians(float(theta))
    term1 = -float(vi)*math.sin(rad)*float(t)
    term2 = -0.5*a*(float(t)**2)
    yi = term1 + term2 + float(yf)
    return yi 

def m_vi(key): 
    if key[-1]=='2': 
       xf,xi,t,theta,fw,m,throw = key
       rad = math.radians(float(theta))
       numerator = float(xf)-float(xi)-(0.5*(float(fw)/float(m))*(float(t)**2))
       if float(theta) == 90 or float(theta) == 270:
           vi = 'no vi in x direction'
       else: 
           vi = numerator/(math.cos(rad)*float(t))
    elif key[-1]=='3':
       yf,yi,t,theta,throw = key
       rad = math.radians(float(theta))
       numerator = float(yf)-float(yi)+(0.5*9.81*(float(t)**2))
       if float(theta) == 0 or float(theta) == 180:
           vi = 'no vi in y direction'
       else: 
           vi = numerator/(math.sin(rad)*float(t))
    return vi


def m_vf(key):
    vi,fw,m,xi,xf,yi,yf,th = key
    rad = math.radians(float(th))
    vfx = math.sqrt(((float(vi)*math.cos(rad))**2)+(2*(float(fw)/float(m))*(float(xf)-float(xi))))
    vfy = math.sqrt(((float(vi)*math.sin(rad))**2)-(2*(9.81)*(float(yf)-float(yi))))                
    vf = math.sqrt(vfx**2+vfy**2)  
    return vf
    

def m_th(key):
    if key[-1]=='1':
        xf,xi,vi,fw,m,t,trhow = key
        numer = (float(xf)-float(xi)-(0.5*(float(fw)/float(m))*(float(t)**2)))
        denom = (float(vi)*float(t))
        th = math.acos(numer/denom)
    elif key[-1]=='2':
        yf,yi,vi,t,throe = key
        numer = (float(yf)-float(yi)+(0.5*9.81*(float(t)**2)))
        denom = (float(vi)*float(t))
        th = math.asin(numer/denom)
    th = math.degrees(th)
    return th
