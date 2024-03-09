# Author:           Charles D. Maddux
# Date Created:     4 March 2024
# Description:      E6B Endurance Calculator

import tkinter as tk
from tkinter import ttk
from goHome import goHome


def runEndurance(test=0):

    time_box = tk.Tk()
    time_box.title("Endurance")
    width = 750
    height = 125

    # calculate page size and placement
    screen_width = time_box.winfo_screenwidth()
    screen_height = time_box.winfo_screenheight()
    x_coord = screen_width - (width + 20)
    y_coord = (screen_height / 2) + height
    time_box.geometry("%dx%d+%d+%d" % (width, height, x_coord, y_coord))

    # create the page menu
    menu = tk.Menu(time_box)
    time_box.config(menu=menu)
    filemenu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Home', command=lambda: goHome(time_box))

    # -----------------------------------------------------------------------------------------------------------------
    def calculateEndurance():
        print("FLAMINGOS")

        # erase previously calculated values
        fuel_hrs.delete(0, 100)
        fuel_mins.delete(0, 100)

        # perform calculations (if values are present)
        try:
            gas = float(usable_fuel.get())
            consumption = float(fuel_burn.get())
            total_time = gas / consumption
            hours = int(total_time)
            minutes = int(total_time % hours * 60)
            fuel_hrs.insert(1, hours)
            fuel_mins.insert(1, minutes)

        # handle condition in which inputs are not present or incorrect format
        except:
            fuel_hrs.insert(1, "???")
            fuel_mins.insert(1, "???")

    # -----------------------------------------------------------------------------------------------------------------
    # home button
    home_btn = ttk.Button(time_box, padding=4, text="Home", command=lambda: goHome(time_box))
    home_btn.grid(column=0, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # usable fuel entry
    # -----------------------------------------------------------------------------------------------------------------
    fuel = ttk.Label(time_box, text="Enter the amount of usable fuel: ", padding=3, font=10)
    fuel.grid(column=0, row=1)

    usable_fuel = ttk.Entry(time_box, width=8, font=10)
    usable_fuel.insert(1, "")
    usable_fuel.grid(column=1, row=1)

    f_units = ttk.Label(time_box, text=" gal    ", font=10)
    f_units.grid(column=2, row=1)
    # -----------------------------------------------------------------------------------------------------------------
    # fuel consumption entry
    # -----------------------------------------------------------------------------------------------------------------
    burn = ttk.Label(time_box, text="Enter the fuel consumption rate: ", padding=3, font=10)
    burn.grid(column=0, row=2)

    fuel_burn = ttk.Entry(time_box, width=8, font=10)
    fuel_burn.insert(1, "")
    fuel_burn.grid(column=1, row=2)

    b_units = ttk.Label(time_box, text=" gal/hr    ", font=10)
    b_units.grid(column=2, row=2)
    # -----------------------------------------------------------------------------------------------------------------
    # calculate button
    # -----------------------------------------------------------------------------------------------------------------
    btn = ttk.Button(time_box, padding=3, text="Calculate", command= lambda: calculateEndurance())
    btn.grid(column=1, row=3, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # return calculated value
    run_time = ttk.Label(time_box, text="Endurance at this rate is: ", font=10)
    run_time.grid(column=4, row=1)

    fuel_hrs = ttk.Entry(time_box, width=4, font=10)
    fuel_hrs.insert(1, "")
    fuel_hrs.grid(column=5, row=1)

    h_units = ttk.Label(time_box, text=" hrs ", font=10)
    h_units.grid(column=6, row=1)

    fuel_mins = ttk.Entry(time_box, width=5, font=10)
    fuel_mins.insert(1, "")
    fuel_mins.grid(column=7, row=1)

    m_units = ttk.Label(time_box, text=" mins ", font=10)
    m_units.grid(column=8, row=1)
    # -----------------------------------------------------------------------------------------------------------------
    # testing - if testing, open GUI window without function call
    if test == 1:
        print("In development - Endurance")
        time_box.mainloop()


def main():
    runEndurance(1)


if __name__ == "__main__":
    main()
