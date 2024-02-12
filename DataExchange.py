# Author:           Charles D. Maddux
# Date Created:     11 February 20224
# Description:      Handle calls from E6B to save and retrieve data

import json

# constants
SAVE_FILE = "eb6_data.json"


def saveData(key, pair, test=False):
    """
    Takes in key: value pairs of data, reads existing .json file, appends the dictionary, and overwrites the file
    :param key:     (str)           - parameter value for the .json/dictionary
    :param pair:    (int or float)  - calculated vaule for the parameter
    :param test:    (bool)          - used for testing. Set to True to print .json values in the terminal
    :return: none
    """

    # open the .json file
    try:
        with open(SAVE_FILE, "r+") as data_file:
            # populate the dictionary
            data = json.load(data_file)

    # handle a missing or inaccessible file
    except FileNotFoundError:
            print("File cannot be opened.")

    # add or overwrite the value in the dictionary
    data[key] = pair

    # test only
    if test:
        print(data)

    # open the .json file
    try:
        with open("eb6_data.json", "w") as data_file:
            # write dictionary to .json
            d_val = json.dumps(data)
            data_file.write(d_val)

            data_file.close()

    # handle a missing or inaccessible file
    except FileNotFoundError:
        print("File cannot be opened.")


def getData():
    # future development
    pass


def main():
    """
    Test file to verify output of the function
    :return: none
    """
    saveData("testKey1", 999, True)

    saveData("testKey2", 42, True)

    saveData("testKey3", 2319, True)

    saveData("testKey1", 0, True)


if __name__ == "__main__":
    main()
