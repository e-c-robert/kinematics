# naming conventions:
    # (blank)entry creates the text box, (blank) is either the first or first two
    # letters of the variable name in the equation  
    # the xi, xf, time, etc are the descriptors for the variables in the equation and 
    # are the variables in python for the label that states that in the gui
    # u# are the units that go for each text box 


import tkinter as tk

def rip():
    window.destroy()

#creates the window and its title
window= tk.Tk()
window.title('Projectile Motion')
window.geometry('455x400')

#instruction text placement
inst = tk.Label(window, text='Please enter the following values.', 
                font = (None, 12))
inst.grid(row=0, column=1)

fi = tk.Label(window, text = "type 'find' to solve for that variable", 
              font = (None, 7))
fi.grid(row =1 , column = 1, sticky = 'news')

#inital x entry placement 
xientry = tk.Entry(window, width= 30)
xientry.grid(row=5, column=1)
xi = tk.Label(window, text='initial x position')
xi.grid(row=5, column=0, sticky = 'e')
u1 = tk.Label(window, text ='m')
u1.grid(row =5, column=2, sticky = 'w')


#final x entry placement 
xfentry = tk.Entry(window, width= 30)
xfentry.grid(row=6, column=1)
xf = tk.Label(window, text='final x position')
xf.grid(row=6, column=0, sticky = 'e')
u2 = tk.Label(window, text ='m')
u2.grid(row =6, column=2, sticky = 'w')

#initial velocity entry placement
vientry = tk.Entry(window, width= 30)
vientry.grid(row=2, column=1)
vi = tk.Label(window, text='inital velocity')
vi.grid(row=2, column=0, sticky = 'e')
u3 = tk.Label(window, text ='m/s')
u3.grid(row =2, column=2, sticky = 'w')

#final velocity entry placement
vfentry = tk.Entry(window, width= 30)
vfentry.grid(row=3, column=1)
vf = tk.Label(window, text='final velocity')
vf.grid(row=3, column=0, sticky = 'e')
u9 = tk.Label(window, text ='m/s')
u9.grid(row =3, column=2, sticky = 'w')


#angle of the velocity off of the horizon 
tentry = tk.Entry(window, width= 30)
tentry.grid(row=4, column=1)
theta = tk.Label(window, text='angle of initial velocity')
theta.grid(row=4, column=0, sticky = 'e')
u4 = tk.Label(window, text ='°')
u4.grid(row =4, column=2, sticky = 'w', padx = 5)

#inital y entry placement 
yientry = tk.Entry(window, width= 30)
yientry.grid(row=7, column=1)
yi = tk.Label(window, text='initial y position')
yi.grid(row=7, column=0, sticky = 'e')
u5 = tk.Label(window, text ='m')
u5.grid(row =7, column=2, sticky = 'w')

#final y entry placement 
yfentry = tk.Entry(window, width= 30)
yfentry.grid(row=8, column=1)
yf = tk.Label(window, text='final y position')
yf.grid(row=8, column=0, sticky = 'e')
u6 = tk.Label(window, text ='m')
u6.grid(row =8, column=2, sticky = 'w')

#time entry 
tientry = tk.Entry(window, width= 30)
tientry.grid(row=9, column=1)
time = tk.Label(window, text='time')
time.grid(row=9, column=0, sticky = 'e')
u7 = tk.Label(window, text ='sec')
u7.grid(row =9, column=2, sticky = 'w')

#wind entry (x-comp only)
wentry = tk.Entry(window, width= 30)
wentry.grid(row=10, column=1)
wind = tk.Label(window, text='force due to wind')
wind.grid(row=10, column=0, sticky = 'e')
u8 = tk.Label(window, text ='N')
u8.grid(row =10, column=2, sticky = 'w')


note = tk.Label(window, text='use conventional signs for direction', fg= 'red',
                font = (None, 8))
note.grid(row=12, column=1)

#mass entry 
mentry = tk.Entry(window, width= 30)
mentry.grid(row=11, column=1)
mass = tk.Label(window, text='mass of object')
mass.grid(row=11, column=0, sticky = 'e')
u8 = tk.Label(window, text ='kg')
u8.grid(row =11, column=2, sticky = 'w')

#notes 
note2 = tk.Label(window, text = 'Note: Force due to wind is always in the x-direction.\nCalculator works only with a max of 2 unknowns',
                 font = (None, 8))
note2.grid(row=13, column = 0, columnspan = 2,rowspan = 2, sticky = 'w')


#button to close the program
close = tk.Button(window, text='Close', command=rip)
close.grid(row=15, column=4, sticky = 'e')
