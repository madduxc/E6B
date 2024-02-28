# Author:           Charles D. Maddux
# Date Created:     27 January 20224
# Description:      E6B Home Page

import tkinter as tk
import subprocess, threading, os, sys, json, signal

from tkinter import ttk
from PIL import ImageTk
from LegTime import runLegTime
from FuelRequired import runFuelReq
from getWinds import getWindData

# constants
SAVE_FILE = "eb6_data.json"
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
        - (future) retrieve and display summary of results
        - (future) track leg profiles
        - (future) build a trip
    :return: none
    """

    # declare & initialize window
    e6b = tk.Tk()
    e6b.title("E6B")

    def killE6b():
        e6b.quit()

    # command to print instructions to a textbox
    def homeScreen():
        """
        populate text box to provide instructions for use of tool
        :return: none
        """

        # declare and initialize variables
        instructions = "\n                                        Welcome to the Desktop E6B Flight Computer.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Wind Correction Angle: determine the effect different winds will have on your flight path and\n" \
                       "    ground speed at different airspeeds.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Heading Correction: determine the flight path correction due to winds in flight.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Leg Time:  determine the time it will take to travel your leg distance at a given groundspeed.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Fuel Required: determine the amount of fuel for a given distance at a specified fuel burn.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Endurance: calculate your time aloft for a specific amount of fuel and a set rate of consumption.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Altitude: determine density altitude and pressure altitude for a specific elevation, temperature,\n" \
                       "   and barometer setting.\n" \
                       "         ------------------------------------------------------------------------------------------------------------------\n" \
                       " - Conversions: perform useful conversions, like gallons to pounds for Avgas and Jet A.\n\n"

        text_box.config(width=TEXT_BOX_WIDTH, padding=TEXT_BOX_PADDING, text=instructions, font=9)

    # populate the splash/image at the top of the tool
    try:
        img = ImageTk.PhotoImage(file='images/engines.jpg')
    # handle exceptions if image not found
    except:
        img = "engines image"

    # initialize the text box
    text_box = ttk.Label(e6b)
    homeScreen()

    quit_btn    = ttk.Button(e6b, width=MAIN_BUTTON_WIDTH, padding=MAIN_BUTTON_PADDING, text="Quit", command=killE6b)
    reset_btn   = ttk.Button(e6b, width=MAIN_BUTTON_WIDTH, padding=MAIN_BUTTON_PADDING, text="Reset")
    summary_btn = ttk.Button(e6b, width=MAIN_BUTTON_WIDTH, padding=MAIN_BUTTON_PADDING, text="View Summary")
    picture_window  = ttk.Label(e6b, width=TEXT_BOX_WIDTH, padding=TEXT_BOX_PADDING, image=img)
    wind_corr       = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Wind Correction Angle")

    heading_corr    = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Heading Correction")
    legtime         = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Leg Time", command=runLegTime)
    fuel_req        = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Fuel Requirements", command=runFuelReq)
    endurance       = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Endurance")
    altitude        = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Altitude")
    get_winds       = ttk.Button(e6b, width=MENU_BUTTON_WIDTH, padding=MENU_BUTTON_PADDING, text="Get Winds Aloft", command=getWindData)

    # position the buttons
    e6b.grid()
    quit_btn.grid(column=0, row=0)
    reset_btn.grid(column=0, row=1)
    picture_window.grid(column=1, row=0, rowspan=3)
    text_box.grid(column=0, row=3, rowspan=5, columnspan=4)
    summary_btn.grid(column=3, row=0)
    wind_corr.grid(column=4, row=0)
    heading_corr.grid(column=4, row=1)
    legtime.grid(column=4, row=2)
    fuel_req.grid(column=4, row=3)
    endurance.grid(column=4, row=4)
    altitude.grid(column=4, row=5)
    get_winds.grid(column=4, row=6)

    # create the page menu
    menu = tk.Menu(e6b)
    e6b.config(menu=menu)
    filemenu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Save')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=e6b.quit)

    # button state
    reset_btn.state([ 'disabled' ])
    summary_btn.state([ 'disabled' ])
    wind_corr.state([ 'disabled' ])
    heading_corr.state([ 'disabled' ])
    endurance.state([ 'disabled' ])
    altitude.state([ 'disabled' ])
    # get_winds.state([ 'disabled' ])

    print(legtime.configure().keys())
    e6b.mainloop()

if __name__ == "__main__":
    main()
