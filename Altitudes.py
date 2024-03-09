# Author:           Charles D. Maddux
# Date Created:     4 March 2024
# Description:      E6B Altitude Calculator
import math
import tkinter as tk
from tkinter import ttk
from goHome import goHome


def runAltitudes(test=0):
    """
    Function to calculate the pressure altitude and density altitude of a location (typically an airport).
    Pressure Altitude: the altitude above sea level based on standard atmospheric conditions (temperature and pressure)
    Density altitude: the altitude above sea level adjusted for non-standard temperature, assuming dry air (humidity = 0)
    Field Elevation:    float   [feet]      - user input
    Altimeter Setting:  float   [in-hg]     - user input
    Temperature:        float   [deg C]     - user input
    Pressure Altitude:  float   [feet]      - output
    Density Altitude:   float   [feet]      - output
    :return: none
    """

    alt_box = tk.Tk()
    alt_box.title("Endurance")

    width = 600
    height = 150

    # calculate page size and placement
    screen_width = alt_box.winfo_screenwidth()
    screen_height = alt_box.winfo_screenheight()
    x_coord = screen_width - (width + 20)
    y_coord = (screen_height / 2) + 1.2 * height
    alt_box.geometry("%dx%d+%d+%d" % (width, height, x_coord, y_coord))

    # create the page menu
    menu = tk.Menu(alt_box)
    alt_box.config(menu=menu)
    filemenu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Home', command=lambda: goHome(alt_box))

    def calculateAltitudes():
        """
        Command to pressure and density altitude values after inputs are collected
        :return: none
        """

        # declare & initialize variables
        Rd = 287.05             # [J/(kg K] dry air gas constant
        Tk = 273.15             # [K]       temperature in Kelvins at 0 deg C
        To = 288.15             # [K]       standard temperature at Sea Level
        g = 9.80665             # [m/s^2]   gravitational acceleration
        M = 0.028964            # [kg/mol]  molar mass of dry air
        R =8.31432              # [J/mol K] universal gas constant
        Gamma = 0.0065          # [K/m]     environmental lapse rate
        Po = 101325             # [Pa]      standard pressure at Sea Level
        meters = 3.28084        # [ft]      conversion

        # erase previously calculated values
        pressure_alt.delete(0, 100)
        density_alt.delete(0, 100)

        # perform calculations (if values are present)
        try:
            # gather information from user
            el = int(elevation.get())
            alt_stg = float(altitude.get())

            # calculate pressure altitude & output results
            p_alt = el + 145442.2 * (1 - (math.pow((alt_stg / 29.92126), 0.190261)))
            pressure_alt.insert(1, int(p_alt))
            try:
                # gather information from user
                tmp = float(temperature.get())

                # find standard temperature at altitude
                std_tmp = 15.0 - (2.0 * float(el) / 1000.0)

                # convert to metric
                tmp_K = Tk + tmp
                Pascals = alt_stg * 3386.389

                # find pressure & density at pressure altitude
                pressure = Pascals * math.pow(1 - 0.0000225577 * el / meters, 5.25588)
                density = pressure / (Rd * tmp_K)

                # find density altitude & output results
                exp = (Gamma * R) / (g * M - Gamma * R)
                d_alt = meters * (To / Gamma) * (1 - ((R * To * density) / (M * Po))**exp)
                density_alt.insert(1, int(d_alt))
            except:
                density_alt.insert(1, " - ")

        except:
            pressure_alt.insert(1, " - ")

    # -----------------------------------------------------------------------------------------------------------------
    # home button
    home_btn = ttk.Button(alt_box, padding=4, text="Home", command=lambda: goHome(alt_box))
    home_btn.grid(column=0, row=0, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # elevation entry
    # -----------------------------------------------------------------------------------------------------------------
    elev = ttk.Label(alt_box, text="Enter the field elevation: ", padding=3, font=10)
    elev.grid(column=0, row=1)

    elevation = ttk.Entry(alt_box, width=8, font=10)
    elevation.insert(1, "")
    elevation.grid(column=1, row=1)

    e_units = ttk.Label(alt_box, text=" ft    ", font=10)
    e_units.grid(column=2, row=1)
    # -----------------------------------------------------------------------------------------------------------------
    # altimeter entry
    # -----------------------------------------------------------------------------------------------------------------
    alt = ttk.Label(alt_box, text="Enter the altimeter setting: ", padding=3, font=10)
    alt.grid(column=0, row=2)

    altitude = ttk.Entry(alt_box, width=8, font=10)
    altitude.insert(1, "")
    altitude.grid(column=1, row=2)

    a_units = ttk.Label(alt_box, text=" in-hg ", font=10)
    a_units.grid(column=2, row=2)
    # -----------------------------------------------------------------------------------------------------------------
    # temperature entry
    # -----------------------------------------------------------------------------------------------------------------
    temp = ttk.Label(alt_box, text="Enter the temperature: ", padding=3, font=10)
    temp.grid(column=0, row=3)

    temperature = ttk.Entry(alt_box, width=8, font=10)
    temperature.insert(1, "")
    temperature.grid(column=1, row=3)

    t_units = ttk.Label(alt_box, text=" deg C ", font=10)
    t_units.grid(column=2, row=3)
    # -----------------------------------------------------------------------------------------------------------------
    # calculate button
    # -----------------------------------------------------------------------------------------------------------------
    btn = ttk.Button(alt_box, padding=3, text="Calculate", command= lambda: calculateAltitudes())
    btn.grid(column=1, row=4, columnspan=2)
    # -----------------------------------------------------------------------------------------------------------------
    # return calculated value - Pressure Altitude
    pAlt = ttk.Label(alt_box, text="Pressure Altitude: ", font=10)
    pAlt.grid(column=4, row=1)

    pressure_alt = ttk.Entry(alt_box, width=8, font=10)
    pressure_alt.insert(1, "")
    pressure_alt.grid(column=5, row=1)

    pa_units = ttk.Label(alt_box, text=" ft ", font=10)
    pa_units.grid(column=6, row=1)
    # -----------------------------------------------------------------------------------------------------------------
    # return calculated value - Pressure Altitude
    dAlt = ttk.Label(alt_box, text="Density Altitude: ", font=10)
    dAlt.grid(column=4, row=2)

    density_alt = ttk.Entry(alt_box, width=8, font=10)
    density_alt.insert(1, "")
    density_alt.grid(column=5, row=2)

    da_units = ttk.Label(alt_box, text=" ft ", font=10)
    da_units.grid(column=6, row=2)
    # -----------------------------------------------------------------------------------------------------------------
    # testing - if testing, open GUI window without function call
    if test == 1:
        print("In development - Altitudes")
        alt_box.mainloop()


def main():
    """
    testing
    :return: nine
    """
    runAltitudes(1)


if __name__ == "__main__":
    main()
