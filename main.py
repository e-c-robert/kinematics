# Emma
import guiWindow as g
import functions as f
import tkinter as tk

#button to calulate answer
#need to create the funtion that would actually calculate everything and insert answer
calculate = tk.Button(g.window, text='Calculate', command = f.check)
calculate.grid(row=13, column=4, sticky = 'e', pady = 10)

g.window.mainloop()