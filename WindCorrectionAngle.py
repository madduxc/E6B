# Author:           Charles D. Maddux
# Date Created:     1 March 2024
# Description:      E6B Fuel Required Calculator
#                   Wind Correction Angle Page

import math
import DataExchange as svc
import tkinter as tk
from tkinter import ttk
from goHome import goHome


def runWindCorrection(test=0):
    """
    Function to calculate the wind correction angle, true heading, and ground speed on a straight-line leg of a trip
    Determines the effect of wind on a given flight path, and the corrections in heading and speed to compensate
    True Course:            float   [degrees]   - user input
    True Airspeed:          float   [knots]     - user input
    Wind Direction:         float   [degrees]   - user input
    Wind Speed:             float   [knots]     - user input
    Wind Correction Angle:  float   [degrees]   - output
    True Heading:           float   [degrees]   - output
    Ground Speed:           float   [knots]     - output
    :return: none
    """

    # store the results in a list to make them more portable and to add undo functionality in the future
    wca = []
    th = []
    gs = []

    # declare & initialize window
    wind_corr_box = tk.Tk()
    wind_corr_box.title("Wind Correction")
    width = 800
    height = 180

    # calculate page size and placement
    screen_width = wind_corr_box.winfo_screenwidth()
    screen_height = wind_corr_box.winfo_screenheight()
    x_coord = screen_width - (width + 20)
    y_coord = (screen_height / 2) - 2.35 * height
    wind_corr_box.geometry("%dx%d+%d+%d" % (width, height, x_coord, y_coord))

    # create the page menu
    menu = tk.Menu(wind_corr_box)
    wind_corr_box.config(menu=menu)
    # -----------------------------------------------------------------------------------------------------------------
    # 'File' menu
    filemenu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Save', command= lambda: saveData(th, gs))
    filemenu.add_separator()
    filemenu.add_command(label='Home', command=lambda: goHome(wind_corr_box))
    # -----------------------------------------------------------------------------------------------------------------

    # call DataExchange to save the data just calculated
    def saveData(th, gs):
        """
        Call DataExchange to save the data just calculated
        :param th: (list)   set of calculated true heading values
        :param gs:  (list)   set of calculated ground speed values
        :return: none
        """

        # set up heading entry
        th_key = "True Heading"
        th_index = len(th) - 1
        th_val = th[th_index]

        # set up ground speed entry
        gs_key = "Ground Speed"
        gs_index = len(th) - 1
        gs_val = gs[gs_index]

        # send data to be written
        svc.saveData(th_key, th_val)
        svc.saveData(gs_key, gs_val)

    # -----------------------------------------------------------------------------------------------------------------

    def calculateWindCorrection(wcang, gspd, thdg):
        """
        Command to calculate wind correction angle, true heading, and groundspeed values after inputs are collected
        :param wcang: (list) collection of calculated wca values
        :param gspd:  (list) collection of calculated gs values
        :param thdg:  (list) collection of calculated th values
        :return: none
        """

        # erase previously calculated values
        wind_angle.delete(0, 100)
        true_heading.delete(0, 100)
        ground_speed.delete(0, 100)

        # perform calculations (if values are present)
        try:
            # calculate wind correction angle
            true_crs = int(true_course.get())
            true_as = float(true_airspeed.get())
            wnd_dir = float(wind_dir.get())
            wnd_spd = float(wind_speed.get())
            delta = math.radians(true_crs - (180 + wnd_dir))
            delta2 = wnd_spd * math.sin(delta) / true_as
            wnd_corr = math.degrees(math.asin(delta2))
            wind_angle.insert(1, round(wnd_corr, 1))

            # calculate true heading
            tru_hdg = true_crs + wnd_corr
            true_heading.insert(1, round(tru_hdg, 1))

            # calculate ground speed
            gnd_spd = true_as * math.cos(math.radians(wnd_corr)) + wnd_spd * math.cos(delta)
            ground_speed.insert(1, round(gnd_spd, 1))
        except:
            wind_angle.insert(1, "???")
            true_heading.insert(1, "???")
            ground_speed.insert(1, "???")

        # add values to lists
        wcang.append(wnd_corr)
        thdg.append(tru_hdg)
        gspd.append(gnd_spd)

    # -----------------------------------------------------------------------------------------------------------------
    # home button
    home_btn = ttk.Button(wind_corr_box, padding=4, text="Home", command=lambda: goHome(wind_corr_box))
    home_btn.grid(column=0, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # save button
    save_btn = ttk.Button(wind_corr_box, padding=4, text="Save", command= lambda: saveData(th, gs))
    save_btn.grid(column=4, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # true course entry
    # -----------------------------------------------------------------------------------------------------------------
    tc = ttk.Label(wind_corr_box, text="Enter the aircraft's True Course: ", padding=3, font=10)
    tc.grid(column=0, row=1)

    true_course = ttk.Entry(wind_corr_box, width=6, font=10)
    true_course.insert(1, "")
    true_course.grid(column=1, row=1)

    tc_units = ttk.Label(wind_corr_box, text=" deg ", font=10)
    tc_units.grid(column=2, row=1)
    # -----------------------------------------------------------------------------------------------------------------
    # true airspeed entry
    # -----------------------------------------------------------------------------------------------------------------
    tas = ttk.Label(wind_corr_box, text="Enter the aircraft's True Airspeed: ", padding=3, font=10)
    tas.grid(column=0, row=2)

    true_airspeed = ttk.Entry(wind_corr_box, width=8, font=10)
    true_airspeed.insert(1, "")
    true_airspeed.grid(column=1, row=2)

    tas_units = ttk.Label(wind_corr_box, text=" kts ", font=10)
    tas_units.grid(column=2, row=2)
    # -----------------------------------------------------------------------------------------------------------------
    # wind direction entry
    # -----------------------------------------------------------------------------------------------------------------
    wd = ttk.Label(wind_corr_box, text="Enter the Wind Direction: ", padding=3, font=10)
    wd.grid(column=0, row=3)

    wind_dir = ttk.Entry(wind_corr_box, width=6, font=10)
    wind_dir.insert(1, "")
    wind_dir.grid(column=1, row=3)

    tas_units = ttk.Label(wind_corr_box, text=" deg ", font=10)
    tas_units.grid(column=2, row=3)
    # -----------------------------------------------------------------------------------------------------------------
    # wind speed entry
    # -----------------------------------------------------------------------------------------------------------------
    ws = ttk.Label(wind_corr_box, text="Enter the Wind Speed: ", padding=3, font=10)
    ws.grid(column=0, row=4)

    wind_speed = ttk.Entry(wind_corr_box, width=8, font=10)
    wind_speed.insert(1, "")
    wind_speed.grid(column=1, row=4)

    ws_units = ttk.Label(wind_corr_box, text=" kts ", font=10)
    ws_units.grid(column=2, row=4)
    # -----------------------------------------------------------------------------------------------------------------
    # calculate button
    # -----------------------------------------------------------------------------------------------------------------
    btn = ttk.Button(wind_corr_box, padding=3, text="Calculate", command=lambda: calculateWindCorrection(wca, gs, th))
    btn.grid(column=1, row=5, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # return calculated value - wind correction angle
    # -----------------------------------------------------------------------------------------------------------------
    winds = ttk.Label(wind_corr_box, text=" | Wind Correction Angle: ", font=10)
    winds.grid(column=4, row=1)

    wind_angle = ttk.Entry(wind_corr_box, width=6, font=10)
    wind_angle.insert(1, "")
    wind_angle.grid(column=5, row=1)

    wca_units = ttk.Label(wind_corr_box, text=" deg ", font=10)
    wca_units.grid(column=6, row=1)
    # -----------------------------------------------------------------------------------------------------------------
    # return calculated value - true heading
    # -----------------------------------------------------------------------------------------------------------------
    heading = ttk.Label(wind_corr_box, text=" |               True Heading: ", font=10)
    heading.grid(column=4, row=2)

    true_heading = ttk.Entry(wind_corr_box, width=6, font=10)
    true_heading.insert(1, "")
    true_heading.grid(column=5, row=2)

    th_units = ttk.Label(wind_corr_box, text=" deg ", font=10)
    th_units.grid(column=6, row=2)
    # calculate button
    # -----------------------------------------------------------------------------------------------------------------
    # return calculated value - ground speed
    # -----------------------------------------------------------------------------------------------------------------
    speed = ttk.Label(wind_corr_box, text=" |             Ground Speed: ", font=10)
    speed.grid(column=4, row=3)

    ground_speed = ttk.Entry(wind_corr_box, width=8, font=10)
    ground_speed.insert(1, "")
    ground_speed.grid(column=5, row=3)

    gs_units = ttk.Label(wind_corr_box, text=" kts ", font=10)
    gs_units.grid(column=6, row=3)
    # -----------------------------------------------------------------------------------------------------------------
    if test == 1:
        print("In development - WCA")
        wind_corr_box.mainloop()


def main():
    runWindCorrection(1)


if __name__ == "__main__":
    main()
