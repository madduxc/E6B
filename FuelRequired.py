# Author:           Charles D. Maddux
# Date Created:     10 February 20224
# Description:      E6B Fuel Required Calculator

import tkinter as tk
import DataExchange as svc
from tkinter import ttk


def runFuelReq():
    """
    Function to calculate the minimum fuel required to fly a set period of time at a given fuel consumption rate
    Time Flown:             float   [minutes]       - user input (or retrieve saved value)
    Fuel Consumption Rate:  float   [gallons/hour]  - user input
    Fuel Required:          float   [gallons]       - output
    :return: none
    """

    # store the results in a list to make them more portable and to add undo functionality in the future
    gas = []

    # declare & initialize window
    fuel_box = tk.Tk()
    fuel_box.title("Fuel Required")

    # -----------------------------------------------------------------------------------------------------------------
    def goHome():
        """
        Command to close window and return to Home screen
        :return: none
        """
        # close the window
        fuel_box.destroy()

    # -----------------------------------------------------------------------------------------------------------------
    # call DataExchange to save the data just calculated
    def saveData(gas):
        """
        Call DataExchange to save the data just calculated
        :param gas: (list) - array to store calculated data
        :return: none
        """
        # declare and initialize variables
        key = "Fuel Required"
        index = len(gas) - 1
        pair = gas[index]

        # send data to be written
        svc.saveData(key, pair)

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
            minutes = int(time_flown.get())
            consumption = float(fuel_flow.get())
            gallons = consumption * minutes / 60
            fuel_used.insert(1, round(gallons, 1))

        # handle condition in which inputs are not present or incorrect format
        except:
            fuel_used.insert(1, "???")

        # add value to list
        gas.append(gallons)

    # -----------------------------------------------------------------------------------------------------------------
    # home button
    home_btn = ttk.Button(fuel_box, padding=4, text="Home", command=goHome)
    home_btn.grid(column=0, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # save button
    save_btn = ttk.Button(fuel_box, padding=4, text="Save", command= lambda: saveData(gas))
    save_btn.grid(column=4, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------

    # time entry
    # -----------------------------------------------------------------------------------------------------------------
    time = ttk.Label(fuel_box, text="Enter the time flown: ", padding=3, font=10)
    time.grid(column=0, row=1)

    time_flown = ttk.Entry(fuel_box, width=12, font=10)
    time_flown.insert(1, "")
    time_flown.grid(column=1, row=1)

    t_units = ttk.Label(fuel_box, text=" mins ", font=10)
    t_units.grid(column=2, row=1)
    # -----------------------------------------------------------------------------------------------------------------

    # fuel consumption entry
    # -----------------------------------------------------------------------------------------------------------------
    flow = ttk.Label(fuel_box, text="Enter the fuel flow: ", padding=3, font=10)
    flow.grid(column=0, row=2)

    fuel_flow = ttk.Entry(fuel_box, width=12, font=10)
    fuel_flow.insert(1, "")
    fuel_flow.grid(column=1, row=2)

    f_units = ttk.Label(fuel_box, text=" gal/hr ", font=10)
    f_units.grid(column=2, row=2)
    # -----------------------------------------------------------------------------------------------------------------

    # calculate button
    # -----------------------------------------------------------------------------------------------------------------
    btn = ttk.Button(fuel_box, padding=3, text="Calculate", command=lambda: calculateFuelReq(gas))
    btn.grid(column=1, row=3, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # return calculated value
    # -----------------------------------------------------------------------------------------------------------------
    fuel = ttk.Label(fuel_box, text="Fuel used on this leg: ", font=10)
    fuel.grid(column=4, row=1)

    fuel_used = ttk.Entry(fuel_box, width=12, font=10)
    fuel_used.insert(1, "")
    fuel_used.grid(column=5, row=1)

    fuel_units = ttk.Label(fuel_box, text=" gal ", font=10)
    fuel_units.grid(column=6, row=1)
    # -----------------------------------------------------------------------------------------------------------------


def main():
    runFuelReq()


if __name__ == "__main__":
    main()
