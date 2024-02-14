# pack() organizes widgets in horizontal and vertical boxes that are limited 
# to left, right, top, bottom positions. 
# Each box is offset and relative to each other.

# place() places widgets in a two dimensional grid using x and y absolute 
# coordinates. 

# grid() locates widgets in a two dimensional grid using row and column 
# absolute coordinates. 



# pack() has four padding options: 

# Internal padding 
# External padding 
# Padx, which pads along the x axis
# Pady, which pads along the y axis

# Vertical Positioning with Pack 

# import tkinter as tk

# root = tk.Tk()

# test = tk.Label(root, text="Red", bg="red", fg="white")
# test.pack(side=tk.RIGHT)
# test1 = tk.Label(root, text="Green", bg="green", fg="white")
# test1.pack(side=tk.LEFT)
# test = tk.Label(root, text="Purple", bg="purple", fg="white")
# test.pack(side=tk.BOTTOM)

# tk.mainloop()

# Side-by-Side Positioning with Pack

# import tkinter as tk

# root = tk.Tk()

# test = tk.Label(root, text="red", bg="red", fg="white")
# test.pack(padx=25, pady=15, side=tk.LEFT)
# test = tk.Label(root, text="green", bg="green", fg="white")
# test.pack(padx=5, pady=20, side=tk.LEFT)
# test = tk.Label(root, text="purple", bg="purple", fg="white")
# test.pack(padx=5, pady=20, side=tk.LEFT)

# tk.Label(root, text="purple", bg="purple", fg="white").pack(padx=5, pady=20, side=tk.LEFT)

# root.mainloop()



# Positioning Widgets With Place Layout Manager 


from tkinter import *
root = Tk()

root.geometry('250x200+550+50')
Label(root, text="aaaaa", bg="#FFFF00",
      fg="red").place(x=45, y=10)
Label(root, text="Position 2 : x=50, y=40", bg="#3300CC", fg="white").place(x=50, y=40)
Label(root, text="Position 3 : x=75, y=80", bg="#FF0099", fg="white").place(x=75, y=80)

root.mainloop()