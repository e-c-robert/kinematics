#import guiWindow so that you can get the entry box inputs from the window wihtout having the 
#code in this file directly 
import guiWindow as g
import calculations as c
import tkinter as tk

#finds the computers machine epsilon so we can actually get a 0 answer 
#found this out the hard way 
def fuck():
    ep = 1
    while True :
        if ep+1 <=1:
            ep *= 2
            break
        else:
            ep /= 2
    return ep 

#main function 
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

    #list of all variables and their string form so that i cna call the correct index in places 
    allvar = [vi, vf, theta, xi, xf, yi, yf, t, fw, m]
    strallvar = ['vi', 'vf','theta','xi','xf','yi','yf','t','fw','m']

    #emplty list of inputs to be added in the next for loop 
    inputs = []
    
    #find count for print statments later 
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

    #all dictionaries and lists are in the same order (so they have the same index)
    #even tho dictionaries are unorder, this was done for the sake of those coding 

    #string version of all the required variables and the number of required inputs 
    #dictionary -> keys: the missing variable ('find') : list of all alternative equations
    #inside list is a list of the required variables for that alternative
    strrequires = {'vi': [[]], 
                   'vf': [[]], 
                   'theta': [[]], 
                   'xi': [['vi','theta','t','fw','m','xf', 6]], 
                   'xf':[['xi','vi','theta','t','fw','m', 6]],
                   'yi': [['vi','theta','t', 'yf',4]],
                   'yf':[['yi','vi','theta','t',4]], 
                   't': [['vi','theta','fw','m','xf','xi', 6],
                         ['vi','theta','yf','yi', 4]],
                   'fw':[['xf','xi','vi','theta','t','m', 6]],
                   'm':[['fw','t','xf','xi','vi','theta',6]]}
    #variable version of previous dictionary 
    #created so i can unpack the list
    #instead of a count, there is a unique marker for that alt equation so that
    #we can create an if statement with that marker to toggle between the variations in the 
    # function itself
    requires = {'vi': [[]], 
                'vf': [[]], 
                'theta': [[]], 
                'xi': [[vi,theta,t,fw,m,xf]], 
                'xf':[[xi,vi,theta,t,fw,m]],
                'yi': [[vi,theta,t,yf]],
                'yf':[[yi,vi,theta,t]], 
                't': [[vi,theta,fw,m,xf,xi, 'x'],
                      [vi,theta,yf,yi, 'y']],
                'fw':[[xf,xi,vi,theta,t,m]],
                'm':[[fw,t,xf,xi,vi,theta]]}
    #functions, alternative equations for each variable will be found and done within 
    #the function 
    functions = ['', 
                 '', 
                 '', 
                 c.m_xi, 
                 c.m_xf,
                 c.m_yi,
                 c.m_yf, 
                 c.m_t,
                 c.m_fw,
                 c.m_m]
    
    #for loop : goes through the inputs once
    for ind1, value1, in enumerate(inputs):
        #if there is a variable to find 
        if value1 == 'find':
            #find key from dictionary and all the alt equations 
            key1 = strrequires[strallvar[ind1]]
            #loop through alt equations 
            for alt in range(len(key1)):
                #count for found variables 
                count1 = 0
                #loops through the inputs again to check if needed variable are filled 
                for i,v in enumerate(inputs):
                    #if the varible is in the nth (alt) equation and it is not unknown and it is not empty 
                    if strallvar[i] in key1[alt] and v != '' and v!='find':
                        count1 += 1
                    #if there are 2 variables to solve for then this is moved off the to side 
                    if fcount == 2 and count1 == key1[alt][-1]:
                        #calculates the answer 
                        ans = functions[ind1](requires[strallvar[ind1]][alt])
                        #if the found answer is less than the machine epsilon, ans is 0, yay
                        if ans <= fuck(): 
                            ans = 0
                        #puts the answer in the input list for reference for next unknown 
                        inputs[ind1] = ans
                        #displays the ans in the gui 
                        answer = tk.Label(g.window, text=strallvar[ind1] + ': ' + str(ans), 
                                          fg = 'blue')
                        answer.grid(row = 16, column = 1, sticky = 'w')
                        #changes f count so the display does not overlap  for next unknown
                        fcount = 1
                    elif fcount == 1 and count1==key1[alt][-1]:
                        #find the keys for the variables
                        #because this would be on the second theoretical run 
                        #there needs to be an if statement if this unknwon is dependent on the rpevious 
                        #because im (emma) stupid and the calculation functions dont pull directly from the 
                        #inputs list, the if statement is needed
                        key2 = requires[strallvar[ind1]][alt]
                        #loops through the values of the needed variables
                        for inde, valu in enumerate(key2):
                            if valu == 'find': 
                                #changes the previously unknown to the found ans 
                                key2[inde]=ans
                        #now that the key is changed to the correct ans, we can overwrite that 
                        #variable with this answer yay!
                        ans = functions[ind1](key2)
                        if ans <= fuck(): 
                            ans = 0
                        inputs[ind1] = ans
                        answer = tk.Label(g.window, text=strallvar[ind1] + ': ' + str(ans), 
                                          fg = 'blue')
                        answer.grid(row = 16, column = 0, sticky = 'w')
           
    #bc im (emma) lazy and dont want to figure out a different way...
    #this checks to see if there is still an unknown 
    #this unknown would have been in the inputs list before the previously solved one
    #BUT to solve this, the previously solved one had to be done first so rip 
    #bitch is j copied pasted from above 
    if 'find' in inputs :
        for ind, value, in enumerate(inputs):
            if value == 'find':
                key1 = strrequires[strallvar[ind]]
                for alt in range(len(key1)):
                    count1 = 0
                    for i,v in enumerate(inputs):
                        if strallvar[i] in key1[alt] and v != '' and v!='find':
                            count1 += 1
                        if count1 == key1[alt][-1]: 
                            key2 = requires[strallvar[ind]][alt]
                            for inde, valu in enumerate(key2):
                                if valu == 'find': 
                                    key2[inde]=ans
                            ans = functions[ind](key2)
                            if ans <= fuck(): 
                                ans = 0
                            inputs[ind] = ans
                            answer = tk.Label(g.window, text=strallvar[ind] + ': ' + str(ans), 
                                              fg = 'blue')
                            answer.grid(row = 16, column = 0, sticky = 'w')
