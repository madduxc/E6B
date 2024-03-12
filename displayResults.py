# Author:           Charles D. Maddux
# Date Created:     7 March 2024
# Description:      E6B Calculator
#                   Display Results page

import tkinter as tk
from tkinter import ttk
from Utilities import goHome
import DataExchange as svc


def runDisplay(test=0):
    """
    Function to display all results that were saved to a file during a session
    :return: none
    """

    # declare & initialize window
    results = tk.Tk()
    results.title("Display Results")
    results.config(pady=3, padx=5)

    # calculate page size and placement
    x_coord = 500
    y_coord = 50
    results.geometry("+%d+%d" % (x_coord, y_coord))

    # create the page menu
    menu = tk.Menu(results)
    results.config(menu=menu)
    # -----------------------------------------------------------------------------------------------------------------
    # home button
    home_btn = ttk.Button(results, padding=4, text="Home", command=lambda: goHome(results))
    home_btn.grid(column=0, row=0, columnspan=2, padx=100)
    # -----------------------------------------------------------------------------------------------------------------
    results_vals = svc.getResultSummary()
    # add values to cells
    i = 1
    for key in results_vals:
        if key != 'a':
            tk.Label(results, text=key, font=10).grid(column=0, row=i, padx=5)
            ttk.Button(results, padding=1, text=round(results_vals[key], 1)).grid(column=1, row=i, padx=2)
            i += 1

    # -----------------------------------------------------------------------------------------------------------------
    # testing - if testing, open GUI window without function call
    if test == 1:
        print("In development - Display Results")
        results.mainloop()


def main():
    """
    testing
    :return: none
    """
    runDisplay(1)


if __name__ == "__main__":
    main()
