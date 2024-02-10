# Author:           Charles D. Maddux
# Date Created:     10 February 20224
# Description:      E6B Leg Time Calculator

import tkinter as tk
from tkinter import ttk


def runLegTime():
    # declare & initialize variables
    leg_box = tk.Tk()
    leg_box.title("Leg Time")

    # create the page menu
    menu = tk.Menu(leg_box)
    leg_box.config(menu=menu)
    filemenu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Save')
    filemenu.add_separator()
    filemenu.add_command(label='Home', command=leg_box.destroy)

    def goHome():
        leg_box.destroy()

    def calculateLegTime():
        leg_time.delete(0 ,100)
        try:
            miles = int(distance.get())
            knots = int(speed.get())
            times = miles / knots * 60
            leg_time.insert(1, round(times, 1))
        except:
            leg_time.insert(1, "???")

    home_btn = ttk.Button(leg_box, padding=4, text="Home", command=goHome)
    home_btn.grid(column=0, row=0, columnspan=2)

    save_btn = ttk.Button(leg_box, padding=4, text="Save")
    save_btn.grid(column=4, row=0, columnspan=2)

    dist = ttk.Label(leg_box, text="Enter the distance of the Leg: ", padding=3, font=10)
    dist.grid(column=0, row=1)

    distance = ttk.Entry(leg_box, width=12, font=10)
    distance.insert(1, "")
    distance.grid(column=1, row=1)

    d_units = ttk.Label(leg_box, text=" nm    ", font=10)
    d_units.grid(column=2, row=1)

    spd = ttk.Label(leg_box, text="Enter the airspeed on the Leg: ", padding=3, font=10)
    spd.grid(column=0, row=2)

    speed = ttk.Entry(leg_box, width=12, font=10)
    speed.insert(1, "")
    speed.grid(column=1, row=2)

    s_units = ttk.Label(leg_box, text=" kts   ", font=10)
    s_units.grid(column=2, row=2)

    btn = ttk.Button(leg_box, padding=3, text="Calculate", command=calculateLegTime)
    btn.grid(column=1, row=3, columnspan=2)

    leg = ttk.Label(leg_box, text="The time required the Leg is: ", font=10)
    leg.grid(column=4, row=1)

    leg_time = ttk.Entry(leg_box, width=12, font=10)
    leg_time.insert(1, "")
    leg_time.grid(column=5, row=1)

    t_units = ttk.Label(leg_box, text=" mins ", font=10)
    t_units.grid(column=6, row=1)
