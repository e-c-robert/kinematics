#import guiWindow so that you can get the entry box inputs from the window wihtout having the 
#code in this file directly 
import guiWindow as g
import calculations as c
import tkinter as tk

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
    
    # #list if there is a independent variable that needs to be solved for first
    # backtrack = []

    #all dictionaries and lists are in the same order (so they have the same index)
    #even tho dictionaries are unorder, this was done for the sake of those coding 

    #string version of all the required variables and the number of required inputs 
    #dictionary -> keys: the missing variable ('find') : list of all alternative equations
    #inside list is a list of the required variables for that alternative
    strrequires = {'vi': [[]], 
                   'vf': [[]], 
                   'theta': [[]], 
                   'xi': [[]], 
                   'xf':[['xi','vi','theta','t','fw','m', 6]],
                   'yi': [[]],
                   'yf':[['yi','vi','theta','t',4]], 
                   't': [['vi','theta','fw','m','xf','xi', 6],
                         ['vi','theta','yf','yi', 4]],
                   'fw':[['xf','xi','vi','theta','t','m', 6]],
                   'm':[['fw','t','xf','xi','vi','theta',6]]}
    #variable version of previous dictionary 
    #created so i can unpack the list
    #instead of a count, there is a unique marker for that alt equation so that
    #we can create an if statement with that marker to toggle between the variations in the function itself
    requires = {'vi': [[]], 
                'vf': [[]], 
                'theta': [[]], 
                'xi': [[]], 
                'xf':[[xi,vi,theta,t,fw,m]],
                'yi': [[]],
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
                 '', 
                 c.m_xf,
                 '',
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
                    if strallvar[i] in key1[alt] and v != '' and v!='find' and v!= 'expected':
                        count1 += 1
                    # #if the variable is in the nth equation but is unknown and also not the 
                    # #current one we are checking
                    # elif strallvar[i] in key1[alt] and v == 'find' and i!=ind1 : 
                    #     backtrack.append(i)
                    #     break
                    # #still have to thikn about how this is going to work j ignore for now 
                    # if count1 != key1[alt][-1] and backtrack != [] and fcount==2:
                    #     inputs[ind1] = 'expected'
                    #     continue 
                    #if there are 2 variables to solve for then this is moved off the to side 
                    if fcount == 2 and count1 == key1[alt][-1]:
                        #calculates the answer 
                        ans = functions[ind1](requires[strallvar[ind1]][alt])
                        #puts the answer in the input list for reference for next unknown 
                        inputs[ind1] = functions[ind1](requires[strallvar[ind1]][alt])
                        #displays the ans in the gui 
                        answer = tk.Label(g.window, text=strallvar[ind1] + ': ' + str(ans), 
                                          fg = 'blue')
                        answer.grid(row = 16, column = 1, sticky = 'w')
                        #changes f count so the display does not overlap  for next unknown
                        fcount = 1
                    elif fcount == 1 and count1==key1[alt][-1]:
                        ans = functions[ind1](requires[strallvar[ind1]][alt])
                        inputs[ind1] = functions[ind1](requires[strallvar[ind1]][alt])
                        answer = tk.Label(g.window, text=strallvar[ind1] + ': ' + str(ans), 
                                          fg = 'blue')
                        answer.grid(row = 16, column = 0, sticky = 'w')
                
    # # still have to think about the logic here 
    # if backtrack != [] :
    #     for place in backtrack :
    #         key2 = strrequires[strallvar[ind1]]
    #         count = 0
    #         for i1,v1 in enumerate(inputs):
    #             if strallvar[i1] in key2 and v1!= '' and v1!='find' and v1!= 'expected':
    #                 count +=1
    #         if count == key2[-1]:
    #             ans1 = functions[place](requires[strallvar[place]])
    #             inputs[place] = functions[place](requires[strallvar[place]])
    #             answer = tk.Label(g.window, text=strallvar[place] + ': ' + str(ans1), 
    #                               fg = 'blue')
    #             answer.grid(row = 16, column = 0, sticky = 'w')
