import math

#finds the computers machine epsilon so we can actually get a 0 answer 
#found this out the hard way 
def zero(ans5):
    ep = 1
    while True :
        if ep+1 <=1: 
            ep *= 2
            break
        else:
            ep /= 2
    if abs(ans5)<=ep:
        return 0
    else:
        return ans5

#calculation functions 
def m_xf(key1):
    x1,v1,th,time,forcew,mass = key1
    a = float(forcew)/float(mass)
    rad = float(th)*(math.pi/180)
    x2 = float(x1)+ (float(v1)*float(time)*math.cos(rad)) + (0.5*a*(float(time)**2))
    return x2

def m_yf(key2):
    y1,v2,the,time1 = key2
    rad = float(the)*(math.pi/180)
    y2 = float(y1)+ (float(v2)*math.sin(rad)*float(time1)) +(-0.5*9.81*(float(time1)**2))
    return y2 
   
def m_m(key3):
    fw1,t1,xf1,xi1,vi1,th1 = key3
    denom = float(fw1)*(float(t1)**2)*0.5
    rad = float(th1)*(math.pi/180)
    num = float(xf1)-float(xi1) - (float(vi1)*math.cos(rad) *float(t1))
    m = num/denom
    return m 

def m_t(key4):
    #if statement checks if the given numbers are for the x or y direction 
    #the direction changes the trig and acceleration 
    if key4[-1] == 'x':
        vi,theta,fw,m,sf,si,s = key4
        rad = float(theta)*(math.pi/180)
        a = 0.5*(float(fw)/float(m))
        b = -float(vi)*math.cos(rad)
    elif key4[-1] == 'y': 
        vi,theta, sf,si,s = key4
        rad = float(theta)*(math.pi/180)
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
    rad = float(th)*(math.pi/180)
    term2 = float(vi)*math.cos(rad)*float(t)
    fw = (term1-term2)*2*float(m)*(float(t)**(-2))
    return fw

def m_xi(key):
    vi,th,t,fw,m,xf = key 
    a = float(fw)/float(m)
    rad = float(th)*(math.pi/180)
    term1 = -float(vi)*math.cos(rad)*float(t)
    term2 = -0.5*a*(float(t)**2)
    xi = term1 +term2 +float(xf)
    return xi 

def m_yi(key):
    vi,th,t,yf = key 
    a = -9.81
    rad = float(th)*(math.pi/180)
    term1 = -float(vi)*math.sin(rad)*float(t)
    term2 = -0.5*a*(float(t)**2)
    yi = term1 +term2 +float(yf)
    return yi 

#Andres 
    

def m_vi(key1):    
      Vox,Voy,theta = key
      Vo = math.sqrt(Vox**2 + Voy**2)

def m_vi(key2):  #w
      Xf,Xi,time,f = key
      Vo = (Xf - Xi - 0.5*f*time**2) / (time*math.sqrt(2*(Xf - Xi - f*time**2)))
    
def m_vi(key3):
      Vfx,Vfy,Xi,Yi,time = key
      Vo = math.sqrt((Vfx - Xi)**2 + (Vfy - Yi + 0.5*-9.81*time**2)**2) / (1 - math.exp(-2*math.atan((Vfy - Yi + 0.5*g*time**2)/(Vfx - Xi))))

 def m_vi(key4):   
      Vfx, Vfy, Xi, Yi,m,f = key
      Vo = sqrt((Vfx - Xi)**2 + (Vfy - Yi + 0.5*(f/m)*time**2)**2) / (1 - math.exp(-2*math.atan((Vfy - Yi + 0.5*(f/m)*time**2)/(Vfx - Xi))))   
        
def m_vi(key5):
      Xf, Xi, Yf, Yi, time = key
      Vo = math.sqrt((Xf - Xi)**2 + (Yf - Yi - 0.5*(9.81)*time**2)**2) / time

def m_vi(key6):
     Xf, Xi, Yf, Yi, time,m,f:
     Vo = sqrt((Xf - Xi)**2 + (Yf - Yi - 0.5*(f/m)*time**2)**2) / time   
    
    
    
