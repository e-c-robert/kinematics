#import guiWindow so that you can get the entry box inputs from the window wihtout having the 
#code in this file directly 

# Emma
import guiWindow as g
import calculations as c

#verifies the key to ensure that it all have integers 
def verify(keyi, ans1, anskey,strvar, keystr):
    #loops through the key 
    if isinstance(ans1, float) == False and isinstance(ans1,int)==False:
        g.answer['text'] = 'Error: not enough information.'
    else: 
        for inde, valu in enumerate(keyi):
            #if the value in the key is 'find' and the previously found answer is the one missing here 
            if valu == 'find' and strvar[anskey] == keystr[inde]: 
                #replace missing vlaue in the key wiht the answer 
                keyi[inde] = ans1
                return keyi
            
            #if the value in teh key is find but the previously found answer is not the one required 
            elif valu == 'find' and strvar[anskey] != keystr[inde]: 
                #there is not enough infomration and that statement willbe displayed 
                g.answer['text'] = 'Error: not enough information.'
        

#label placement         
def inwindow(fcount, text):
    #different f count so the display does not overlap for next unknown
    # Sammy
    if fcount == 2:
        g.answer2['text'] = text
    elif fcount == 1:
        g.answer1['text'] = text
            
#answer (Emma)
def an(fcount, inputs1, strallvar1, strrequires1, requires1, functions1, ans3, anskey):
    #for loop : goes through the inputs once
    for ind1, value1, in enumerate(inputs1):
        #if there is a variable to find 
        if value1 == 'find':
            #find key from dictionary and all the alt equations 
            key1 = strrequires1[strallvar1[ind1]]#loop through alternate equations 
            for alt in range(len(key1)):
                #count for found variables 
                count1 = 0
                #loops through the inputs again to check if needed variables are filled 
                for i, v in enumerate(inputs1):
                    #if the varible is in the nth (alt) equation and it is not unknown and it is not empty 
                    if strallvar1[i] in key1[alt] and v != '' and v!= 'find':
                        count1 += 1 #count plus one to keep track of what we have and what we dont have 
                    if count1 == key1[alt][-1]: #if we have the correct number of variables inputted 
                        #key2 = variable version of key1
                        key2 = requires1[strallvar1[ind1]][alt]
                        #this is if an unknown was solved before as the keys dont change w the input list
                        if 'find' in key2:
                            key2 = verify(key2, ans3, anskey, strallvar1, key1[alt])
                        #inputs key into correct function and zero() checks to see if the answer is less than epsilon
                        ans3 = c.zero(functions1[ind1](key2))  
                        #chnages input list so the for loops dont have a time 
                        inputs1[ind1] = ans3
                        #save the index for this answer so that I can use it for verification later 
                        anskey = ind1
                        #answer display 
                        ansText = strallvar1[ind1] + ': ' + str(ans3)
                        inwindow(fcount, ansText)
                        fcount -= 1
                        return ans3, anskey
        #for one value to find, and there is not enough information,
        #error statement 
        if ind1 == 9 and ans3 == '':
            g.answer['text'] = 'Error: not enough information.'
            return ans3, anskey

#main function (Emma)
def check():
    g.answer1['text'] = ''
    g.answer2['text'] = ''
    g.answer['text'] = ''
    
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
    strallvar = ['vi', 'vf', 'theta', 'xi', 'xf', 'yi', 'yf', 't', 'fw', 'm']

    #string version of all the required variables and the number of required inputs 
    #dictionary -> keys: the missing variable ('find') : list of all alternative equations
    #inside list is a list of the required variables for that alternative
    strrequires = {'vi': [['xf','xi','t','theta','fw','m',6],
                          ['yf','yi','t','theta',4]], 
                   'vf': [['vi','fw','m','xi','xf','yi','yf','theta',8]], 
                   'theta': [['xf','xi','vi','fw','m','t',6],
                             ['yf','yi','vi','t',4]], 
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
    

    requires = {'vi': [[xf, xi, t, theta, fw, m, '2'],
                       [yf, yi, t, theta, '3']], 
                'vf': [[vi, fw, m, xi, xf, yi, yf, theta]], 
                'theta': [[xf, xi, vi, fw, m, t, '1'],
                          [yf, yi, vi, t, '2']], 
                'xi': [[vi, theta, t, fw, m, xf]], 
                'xf':[[xi, vi, theta, t, fw, m]],
                'yi': [[vi, theta, t, yf]],
                'yf':[[yi, vi, theta, t]], 
                't': [[vi, theta, fw, m, xf, xi, 'x'],
                      [vi, theta, yf, yi, 'y']],
                'fw':[[xf, xi, vi, theta, t, m]],
                'm':[[fw, t, xf, xi, vi, theta]]}

    #functions, alternative equations for each variable will be found and done within 
    #the function 
    functions = [c.m_vi, c.m_vf, c.m_th, c.m_xi, c.m_xf, c.m_yi, c.m_yf, c.m_t, 
                 c.m_fw, c.m_m]
    
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
    
    #empty ans variable so it can be an imput for the functions
    ans = ''
    anskey = ''
    ans,anskey = an(fcount, inputs, strallvar, strrequires, requires, functions, ans, anskey)
    if 'find' in inputs : # still?!?!?!??!?!
       ans,anskey = an(1, inputs, strallvar, strrequires, requires, functions, ans, anskey)
