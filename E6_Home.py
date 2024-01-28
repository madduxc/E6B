# Author:           Charles D. Maddux
# Date Created:     27 January 20224
# Description:      E6B Home Page
import tkinter as tk
from tkinter import ttk

def legTime():
    print("ducks")

def main():

    # declare & initialize variables
    e6b = tk.Tk()
    e6b.title("E6B")

    home = ttk.Frame(e6b, padding=10)
    home.grid()
    quit_btn = ttk.Button(home, text="Quit", command=e6b.destroy)
    reset_btn = ttk.Button(home, text="Reset", padding=2)
    wind_corr       = ttk.Button(home, width=30, padding=5, text="Wind Correction Angle")
    heading_corr    = ttk.Button(home, width=30, padding=5, text="Heading Correction")
    legtime         = ttk.Button(home, width=30, padding=5, text="Leg Time")
    fuel_req        = ttk.Button(home, width=30, padding=5, text="Fuel Requirements")
    endurance       = ttk.Button(home, width=30, padding=5, text="Endurance")
    altitude        = ttk.Button(home, width=30, padding=5, text="Altitude")
    convert         = ttk.Button(home, width=30, padding=5, text="Conversions")

    # position the buttons
    quit_btn.grid(column=0, row=0)
    reset_btn.grid(column=0, row=1)
    wind_corr.grid(column=4, row=0)
    heading_corr.grid(column=4, row=1)
    legtime.grid(column=4, row=2)
    fuel_req.grid(column=4, row=3)
    endurance.grid(column=4, row=4)
    altitude.grid(column=4, row=5)
    convert.grid(column=4, row=6)

    # create the page menu
    menu = tk.Menu(e6b)
    e6b.config(menu=menu)
    filemenu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Save')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=e6b.quit)

    print(legtime.configure().keys())
    e6b.mainloop()

if __name__ == "__main__":
    main()
