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
window.geometry('400x300')

#instruction text placement
inst = tk.Label(window, text='Please enter the following values.')
inst.grid(row=0, column=1)

#inital x entry placement 
xientry = tk.Entry(window, width= 30)
xientry.grid(row=3, column=1)
xi = tk.Label(window, text='initial x position')
xi.grid(row=3, column=0)
u1 = tk.Label(window, text ='m')
u1.grid(row =3, column=2)


#final x entry placement 
xfentry = tk.Entry(window, width= 30)
xfentry.grid(row=4, column=1)
xf = tk.Label(window, text='final x position')
xf.grid(row=4, column=0)
u2 = tk.Label(window, text ='m')
u2.grid(row =4, column=2)

#velocity entry placement
ventry = tk.Entry(window, width= 30)
ventry.grid(row=1, column=1)
vel = tk.Label(window, text='velocity')
vel.grid(row=1, column=0)
u3 = tk.Label(window, text ='m/s')
u3.grid(row =1, column=2)

#angle of the velocity off of the horizon 
tentry = tk.Entry(window, width= 30)
tentry.grid(row=2, column=1)
theta = tk.Label(window, text='angle of the velocity')
theta.grid(row=2, column=0)
u4 = tk.Label(window, text ='°')
u4.grid(row =2, column=2)

#inital y entry placement 
yientry = tk.Entry(window, width= 30)
yientry.grid(row=5, column=1)
yi = tk.Label(window, text='initial y position')
yi.grid(row=5, column=0)
u5 = tk.Label(window, text ='m')
u5.grid(row =5, column=2)

#final y entry placement 
yfentry = tk.Entry(window, width= 30)
yfentry.grid(row=6, column=1)
yf = tk.Label(window, text='final y position')
yf.grid(row=6, column=0)
u6 = tk.Label(window, text ='m')
u6.grid(row =6, column=2)

#time entry 
tientry = tk.Entry(window, width= 30)
tientry.grid(row=7, column=1)
time = tk.Label(window, text='time')
time.grid(row=7, column=0)
u7 = tk.Label(window, text ='sec')
u7.grid(row =7, column=2)

#wind entry 
wentry = tk.Entry(window, width= 30)
wentry.grid(row=8, column=1)
wind = tk.Label(window, text='force due to wind')
wind.grid(row=8, column=0)
u8 = tk.Label(window, text ='N')
u8.grid(row =8, column=2)


note = tk.Label(window, text='use conventional signs for direction', fg= 'red')
note.grid(row=10, column=1)

#mass entry 
mentry = tk.Entry(window, width= 30)
mentry.grid(row=9, column=1)
mass = tk.Label(window, text='mass of object')
mass.grid(row=9, column=0)
u8 = tk.Label(window, text ='kg')
u8.grid(row =9, column=2)


#button to calulate answer
#need to create the funtion that would actually calculate everything and insert answer
calculate = tk.Button(window, text='Calculate')
calculate.grid(row=13, column=1)

#button to close the program
close = tk.Button(window, text='Close', command=rip)
close.grid(row=17, column=4)

window.mainloop()