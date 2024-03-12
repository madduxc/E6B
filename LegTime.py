# Author:           Charles D. Maddux
# Date Created:     10 February 2024
# Description:      E6B Calculator
#                   Leg Time page

import tkinter as tk
import DataExchange as svc
from tkinter import ttk
from Utilities import goHome


def runLegTime(test=0):
    """
    Function to calculate the time required to fly a set distance at a given speed over the ground
    conversion from airspeed to ground speed is required prior to this step
    Distance:       float   [nautical miles]       - user input
    Ground Speed:   float   [nautical miles/hour]  - user input (or saved data)
    Time Required:  float   [minutes]               - output
    :return: none
    """

    # store the results in a list to make them more portable and to add undo functionality in the future
    time = []

    # declare & initialize window
    leg = tk.Tk()
    leg.title("Leg Time")
    width = 770
    height = 125

    # calculate page size and placement
    screen_width = leg.winfo_screenwidth()
    screen_height = leg.winfo_screenheight()
    x_coord = screen_width - (width + 20)
    y_coord = (screen_height / 2) - 2 * height
    leg.geometry("%dx%d+%d+%d" % (width, height, x_coord, y_coord))

    # -----------------------------------------------------------------------------------------------------------------
    def saveData(time):
        """
        Call DataExchange to save the data just calculated
        :param time: (list) - array to store calculated data
        :return: none
        """
        # declare and initialize variables
        key = "Leg Time"
        index = len(time) - 1
        pair = time[index]

        # send data to be written
        svc.saveData(key, pair)
    # -----------------------------------------------------------------------------------------------------------------
    def getData(tk):
        """
        retrieve data from storage to pre-populate input values
        :param tk: tkinter page
        :return: none
        """

        key = "Ground Speed"
        speed_value = svc.getData(key)
        speed.delete(0, 100)
        speed.insert(1, round(float(speed_value), 1))
    # -----------------------------------------------------------------------------------------------------------------

    def calculateLegTime(time):
        """
        Command to calculate time required value after inputs are collected
        :param time: (list) - array to store calculated data
        :return: none
        """

        # erase previously calculated values
        leg_time.delete(0, 100)

        # perform calculations (if values are present)
        try:
            miles = float(distance.get())
            knots = float(speed.get())
            times = miles / knots * 60
            leg_time.insert(1, round(times, 1))
            # add value to list
            time.append(times)

        # handle condition in which inputs are not present or incorrect format
        except:
            leg_time.insert(1, "???")

    # create the page menu
    menu = tk.Menu(leg)
    leg.config(menu=menu)
    file_menu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='Home', command=lambda: goHome(leg))
    file_menu.add_separator()
    file_menu.add_command(label='Save', command=lambda: saveData(time))
    file_menu.add_separator()
    file_menu.add_command(label='Get Data', command=lambda: getData(leg))
    # -----------------------------------------------------------------------------------------------------------------
    # home button
    home_btn = ttk.Button(leg, padding=4, text="Home", command=lambda: goHome(leg))
    home_btn.grid(column=0, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # get data button
    data_btn = ttk.Button(leg, padding=4, text="Get Data", command=lambda: getData(leg))
    data_btn.grid(column=2, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # save button
    save_btn = ttk.Button(leg, padding=4, text="Save", command= lambda: saveData(time))
    save_btn.grid(column=4, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # distance entry
    # -----------------------------------------------------------------------------------------------------------------
    dist = ttk.Label(leg, text="Enter the distance of the Leg: ", padding=3, font=10)
    dist.grid(column=0, row=1)

    distance = ttk.Entry(leg, width=8, font=10)
    distance.insert(1, "")
    distance.grid(column=1, row=1)

    d_units = ttk.Label(leg, text=" nm    ", font=10)
    d_units.grid(column=2, row=1)
    # -----------------------------------------------------------------------------------------------------------------

    # ground speed entry
    # -----------------------------------------------------------------------------------------------------------------
    spd = ttk.Label(leg, text="Enter the ground speed on the Leg: ", padding=3, font=10)
    spd.grid(column=0, row=2)

    speed = ttk.Entry(leg, width=8, font=10)
    speed.insert(1, "")
    speed.grid(column=1, row=2)

    s_units = ttk.Label(leg, text=" kts   ", font=10)
    s_units.grid(column=2, row=2)
    # -----------------------------------------------------------------------------------------------------------------
    # calculate button
    # -----------------------------------------------------------------------------------------------------------------
    btn = ttk.Button(leg, padding=3, text="Calculate", command= lambda: calculateLegTime(time))
    btn.grid(column=1, row=3, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # return calculated value
    leg_val = ttk.Label(leg, text="The time required for the Leg is: ", font=10)
    leg_val.grid(column=4, row=1)

    leg_time = ttk.Entry(leg, width=8, font=10)
    leg_time.insert(1, "")
    leg_time.grid(column=5, row=1)

    t_units = ttk.Label(leg, text=" mins ", font=10)
    t_units.grid(column=6, row=1)
    # -----------------------------------------------------------------------------------------------------------------
    # testing - if testing, open GUI window without function call
    if test == 1:
        print("In development - Leg Time")
        leg.mainloop()


def main():
    """
    testing
    :return: none
    """
    runLegTime(1)


if __name__ == "__main__":
    main()
