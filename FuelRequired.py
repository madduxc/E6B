# Author:           Charles D. Maddux
# Date Created:     10 February 2024
# Description:      E6B Calculator
#                   Fuel Required page

import tkinter as tk
import DataExchange as svc
from tkinter import ttk
from Utilities import goHome


def runFuelReq(test=0):
    """
    Function to calculate the minimum fuel required to fly a set period of time at a given fuel consumption rate
    Time Flown:             float   [minutes]       - user input (or saved data)
    Fuel Consumption Rate:  float   [gallons/hour]  - user input
    Fuel Required:          float   [gallons]       - output
    :return: none
    """

    # store the results in a list to make them more portable and to add undo functionality in the future
    gas = []

    # declare & initialize window
    fuel = tk.Tk()
    fuel.title("Fuel Required")
    width = 650
    height = 125

    # calculate page size and placement
    screen_width = fuel.winfo_screenwidth()
    screen_height = fuel.winfo_screenheight()
    x_coord = screen_width - (width + 20)
    y_coord = (screen_height / 2) - (height / 2)
    fuel.geometry("%dx%d+%d+%d" % (width, height, x_coord, y_coord))

    # -----------------------------------------------------------------------------------------------------------------
    def saveData(gas):
        """
        Call DataExchange to save the data just calculated
        :param gas: (list) - array to store calculated data
        :return: none
        """
        # declare and initialize variables
        key1 = "Fuel Required"
        key2 = "Fuel Flow"
        index = len(gas) - 1
        val1 = gas[index]
        val2 = float(fuel_flow.get())

        # send data to be written
        svc.saveData(key1, val1)
        svc.saveData(key2, val2)

    # -----------------------------------------------------------------------------------------------------------------
    def getData(tk):
        key = "Leg Time"
        time_value = svc.getData(key)
        time_flown.delete(0, 100)
        time_flown.insert(1, round(float(time_value), 1))

    # create the page menu
    menu = tk.Menu(fuel)
    fuel.config(menu=menu)
    file_menu = tk.Menu(menu)
    file_menu.add_separator()
    file_menu.add_command(label='Home', command=lambda: goHome(fuel))
    menu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='Save', command= lambda: saveData(gas))

    # -----------------------------------------------------------------------------------------------------------------
    def calculateFuelReq(gas):
        """
        Command to calculate fuel required value after inputs are collected
        :param gas: (list) - array to store calculated data
        :return: none
        """
        # erase previously calculated values
        fuel_used.delete(0, 100)

        # perform calculations (if values are present)
        try:
            minutes = float(time_flown.get())
            consumption = float(fuel_flow.get())
            gallons = consumption * minutes / 60
            fuel_used.insert(1, round(gallons, 1))
            # add value to list
            gas.append(gallons)

        # handle condition in which inputs are not present or incorrect format
        except:
            fuel_used.insert(1, "???")

    # create the page menu
    menu = tk.Menu(fuel)
    fuel.config(menu=menu)
    file_menu = tk.Menu(menu)
    file_menu.add_separator()
    file_menu.add_command(label='Home', command=lambda: goHome(fuel))
    menu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='Save', command= lambda: saveData(gas))
    file_menu.add_separator()
    file_menu.add_command(label='Get Data', command=lambda: getData(fuel))
    # -----------------------------------------------------------------------------------------------------------------
    # home button
    home_btn = ttk.Button(fuel, padding=4, text="Home", command=lambda: goHome(fuel))
    home_btn.grid(column=0, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # get data button
    data_btn = ttk.Button(fuel, padding=4, text="Get Data", command=lambda: getData(fuel))
    data_btn.grid(column=2, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # save button
    save_btn = ttk.Button(fuel, padding=4, text="Save", command= lambda: saveData(gas))
    save_btn.grid(column=4, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # time entry
    # -----------------------------------------------------------------------------------------------------------------
    time = ttk.Label(fuel, text="Enter the time flown: ", padding=3, font=10)
    time.grid(column=0, row=1)

    time_flown = ttk.Entry(fuel, width=12, font=10)
    time_flown.insert(1, "")
    time_flown.grid(column=1, row=1)

    t_units = ttk.Label(fuel, text=" mins ", font=10)
    t_units.grid(column=2, row=1)
    # -----------------------------------------------------------------------------------------------------------------
    # fuel consumption entry
    # -----------------------------------------------------------------------------------------------------------------
    flow = ttk.Label(fuel, text="Enter the fuel flow: ", padding=3, font=10)
    flow.grid(column=0, row=2)

    fuel_flow = ttk.Entry(fuel, width=12, font=10)
    fuel_flow.insert(1, "")
    fuel_flow.grid(column=1, row=2)

    f_units = ttk.Label(fuel, text=" gal/hr ", font=10)
    f_units.grid(column=2, row=2)
    # -----------------------------------------------------------------------------------------------------------------
    # calculate button
    # -----------------------------------------------------------------------------------------------------------------
    btn = ttk.Button(fuel, padding=3, text="Calculate", command=lambda: calculateFuelReq(gas))
    btn.grid(column=1, row=3, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # return calculated value
    # -----------------------------------------------------------------------------------------------------------------
    fuel_val = ttk.Label(fuel, text="Fuel used on this leg: ", font=10)
    fuel_val.grid(column=4, row=1)

    fuel_used = ttk.Entry(fuel, width=12, font=10)
    fuel_used.insert(1, "")
    fuel_used.grid(column=5, row=1)

    fuel_units = ttk.Label(fuel, text=" gal ", font=10)
    fuel_units.grid(column=6, row=1)
    # -----------------------------------------------------------------------------------------------------------------
    # testing - if testing, open GUI window without function call
    if test == 1:
        print("In development - Fuel Required")
        fuel.mainloop()


def main():
    """
    testing
    :return: none
    """
    runFuelReq(1)


if __name__ == "__main__":
    main()
