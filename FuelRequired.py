# Author:           Charles D. Maddux
# Date Created:     10 February 20224
# Description:      E6B Fuel Required Calculator

import tkinter as tk
from tkinter import ttk


def runFuelReq():

    # declare & initialize variables
    fuel_box = tk.Tk()
    fuel_box.title("Fuel Required")

    def goHome():
        fuel_box.destroy()

    def calculateFuelReq():
        fuel_used.delete(0, 100)
        try:
            minutes = int(time_flown.get())
            consumption = float(fuel_flow.get())
            gallons = consumption * minutes / 60
            fuel_used.insert(1, round(gallons, 1))
        except:
            fuel_used.insert(1, "???")

    home_btn = ttk.Button(fuel_box, padding=4, text="Home", command=goHome)
    home_btn.grid(column=0, row=0, columnspan=2)

    save_btn = ttk.Button(fuel_box, padding=4, text="Save")
    save_btn.grid(column=4, row=0, columnspan=2)

    time = ttk.Label(fuel_box, text="Enter the time flown: ", padding=3, font=10)
    time.grid(column=0, row=1)

    time_flown = ttk.Entry(fuel_box, width=12, font=10)
    time_flown.insert(1, "")
    time_flown.grid(column=1, row=1)

    t_units = ttk.Label(fuel_box, text=" mins ", font=10)
    t_units.grid(column=2, row=1)

    flow = ttk.Label(fuel_box, text="Enter the fuel flow: ", padding=3, font=10)
    flow.grid(column=0, row=2)

    fuel_flow = ttk.Entry(fuel_box, width=12, font=10)
    fuel_flow.insert(1, "")
    fuel_flow.grid(column=1, row=2)

    f_units = ttk.Label(fuel_box, text=" gal/hr ", font=10)
    f_units.grid(column=2, row=2)

    btn = ttk.Button(fuel_box, padding=3, text="Calculate", command=calculateFuelReq)
    btn.grid(column=1, row=3, columnspan=2)

    fuel = ttk.Label(fuel_box, text="Fuel used on this leg: ", font=10)
    fuel.grid(column=4, row=1)

    fuel_used = ttk.Entry(fuel_box, width=12, font=10)
    fuel_used.insert(1, "")
    fuel_used.grid(column=5, row=1)

    fuel_units = ttk.Label(fuel_box, text=" gal ", font=10)
    fuel_units.grid(column=6, row=1)
