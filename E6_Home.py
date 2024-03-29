# Author:           Charles D. Maddux
# Date Created:     27 January 2024
# Description:      E6B Home Page

import tkinter as tk
import DataExchange as svc
from tkinter import ttk
from PIL import ImageTk
from LegTime import runLegTime
from FuelRequired import runFuelReq
from getWinds import getWindData
from WindCorrectionAngle import runWindCorrection
from Endurance import runEndurance
from Altitudes import runAltitudes
from displayResults import runDisplay

# constants
TEXT_BOX_WIDTH      = 75
MENU_BUTTON_WIDTH   = 30
MAIN_BUTTON_WIDTH   = 20
TEXT_BOX_PADDING    = 10
MENU_BUTTON_PADDING = 10
MAIN_BUTTON_PADDING = 3


def main():
    """
    E6B Flight Computer. For manual cross country flight planning.  Home screen.
        - House and format buttons that lead to other screens.
        - Display menu of instruction for how to use the tool
        - Call other functions to perform calculations
        - Retrieve, display, and reset summary of results
        - (future) track leg profiles
        - (future) build a trip
    :return: none
    """

    # declare & initialize window
    e6b = tk.Tk()
    e6b.title("E6B")
    width = 950
    height = 575
    screen_height = e6b.winfo_screenheight()
    x_coord = 50
    y_coord = (screen_height / 2) - 0.75 * (height)
    e6b.geometry("%dx%d+%d+%d" % (width, height, x_coord, y_coord))

    # -----------------------------------------------------------------------------------------------------------------
    def killE6b():
        e6b.quit()

    # -----------------------------------------------------------------------------------------------------------------
    # command to print instructions to a textbox
    def homeScreen():
        """
        populate text box to provide instructions for use of tool
        :return: none
        """

        # declare and initialize variables
        instructions = "\n                                        Welcome to the Desktop E6B Flight Computer.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Wind Correction Angle: determine the effect different winds will have on your flight " \
                       "path and\n   ground speed at different airspeeds.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Heading Correction: determine the flight path correction due to winds in flight.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Leg Time:  determine the time it will take to travel your leg distance at a " \
                       "given groundspeed.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Fuel Required: determine the amount of fuel for a given distance at a specified " \
                       "fuel burn.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Endurance: calculate your time aloft for a specific amount of fuel and a set " \
                       "rate of consumption.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Altitude: determine density altitude and pressure altitude for a specific elevation, " \
                       "temperature,\n   and barometer setting.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Winds Aloft: retrieve wind and temperature data from aviationweather.gov for a " \
                       "specific region\n   and altitude.\n\n"
        text_box.config(width=TEXT_BOX_WIDTH, padding=TEXT_BOX_PADDING, text=instructions, font=9)

    # -----------------------------------------------------------------------------------------------------------------
    # create the file menu
    menu = tk.Menu(e6b)
    e6b.config(menu=menu)
    file_menu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='Exit', command=e6b.quit)

    # create the page menu
    page_menu = tk.Menu(menu)
    menu.add_cascade(label='Tools', menu=page_menu)
    page_menu.add_command(label='Wind Correction', command=runWindCorrection)
    page_menu.add_separator()
    page_menu.add_command(label='Winds Aloft', command=getWindData)
    page_menu.add_separator()
    page_menu.add_command(label='Leg Time', command=runLegTime)
    page_menu.add_separator()
    page_menu.add_command(label='Fuel Required', command=runFuelReq)
    page_menu.add_separator()
    page_menu.add_command(label='Endurance', command=runEndurance)
    page_menu.add_separator()
    page_menu.add_command(label='Altitudes', command=runAltitudes)

    # create the summary menu
    results_menu = tk.Menu(menu)
    menu.add_cascade(label='Results', menu=results_menu)
    results_menu.add_command(label='Summary', command=runDisplay)
    results_menu.add_separator()
    results_menu.add_command(label='Reset', command=svc.clearData)

    # populate the splash/image at the top of the tool
    try:
        img = ImageTk.PhotoImage(file='images/engines.jpg')
    # handle exceptions if image not found
    except:
        img = "engines image"

    # initialize the text box
    text_box = ttk.Label(e6b)
    homeScreen()

    quit_btn    = ttk.Button(e6b, width=MAIN_BUTTON_WIDTH, padding=MAIN_BUTTON_PADDING,
                             text="Quit", command=killE6b)
    reset_btn   = ttk.Button(e6b, width=MAIN_BUTTON_WIDTH, padding=MAIN_BUTTON_PADDING,
                             text="Reset", command=svc.clearData)
    summary_btn = ttk.Button(e6b, width=MAIN_BUTTON_WIDTH, padding=MAIN_BUTTON_PADDING,
                             text="View Summary", command=runDisplay)
    picture_window = ttk.Label(e6b, width=TEXT_BOX_WIDTH, padding=TEXT_BOX_PADDING, image=img)
    # -----------------------------------------------------------------------------------------------------------------
    wind_corr       = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING,
                                 text="Wind Correction Angle", command=runWindCorrection)
    heading_corr    = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING,
                                 text="Heading Correction")
    leg_time        = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING,
                                 text="Leg Time", command=runLegTime)
    fuel_required   = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING,
                                 text="Fuel Requirements", command=runFuelReq)
    endurance       = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING,
                                 text="Endurance", command=runEndurance)
    altitude        = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING,
                                 text="Altitude", command=runAltitudes)
    get_winds       = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING,
                                 text="Get Winds Aloft", command=getWindData)
    conversions     = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING,
                                 text="Conversions")

    # position the buttons
    e6b.grid()
    quit_btn.grid(column=0, row=0)
    reset_btn.grid(column=0, row=1)
    picture_window.grid(column=1, row=0, rowspan=3)
    text_box.grid(column=0, row=3, rowspan=6, columnspan=4)
    summary_btn.grid(column=3, row=0)
    wind_corr.grid(column=4, row=0)
    heading_corr.grid(column=4, row=1)
    leg_time.grid(column=4, row=2)
    fuel_required.grid(column=4, row=3)
    endurance.grid(column=4, row=4)
    altitude.grid(column=4, row=5)
    get_winds.grid(column=4, row=6)
    conversions.grid(column=4, row=7)

    # button state
    heading_corr.state([ 'disabled' ])
    conversions.state([ 'disabled' ])

    # print(leg_time.configure().keys())
    e6b.mainloop()


if __name__ == "__main__":
    main()
