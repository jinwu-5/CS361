# Author: Jin Wu
# Date: 11-10-2021
# Description: Forest Population microservice

import csv
import os

STATE_PLANT_DICTIONARY = {
    # The value array contains: Forest Coverage Percentage, Red Maple Percentage, 
    # Loblolly pine Percentage, Maple Suger Percentage, Flowering Dogwood Percentage
    "Alabama": ["70.57%", 5, 15, 25, 8], 
    "Alaska": ["35.16%", 10, 8, 25, 42],
    "Arizona": ["25.64%", 12, 21, 6, 36], 
    "Arkansas": ["56.31%", 11, 18, 21, 10],
    "California": ["32.71%", 7, 20, 14, 10],
    "Colorado": ["34.42%", 4, 29, 15, 34],
    "Connecticut": ["55.24%", 17, 19, 42, 5],
    "Delaware": ["27.26%", 30, 0, 0, 2],
    "Florida": ["50.68%", 3, 24, 19, 3],
    "Georgia": ["67.28%", 16, 17, 22, 12],
    "Hawaii": ["42.53%", 12, 8, 3, 21],
    "Idaho": ["40.55%", 20, 22, 22, 23],
    "Illinois": ["13.64%", 29, 18, 20, 15],
    "Indiana": ["21.06%", 28, 9, 11, 24],
    "Iowa": ["8.43%", 1, 7, 5, 2],
    "Kansas": ["4.78%", 27, 24, 2, 7],
    "Kentucky": ["49.35%", 16, 8, 21, 14],
    "Louisiana": ["53.20%", 15, 9, 21, 20],
    "Maine": ["89.46%", 13, 5, 25, 16],
    "Maryland": ["39.36%", 19, 13, 9, 13],
    "Massachusetts": ["60.57%", 28, 27, 23, 2],
    "Michigan": ["55.62%", 27, 24, 2, 7],
    "Minnesota": ["34.08%", 16, 23, 20, 25],
    "Mississippi": ["65.07%", 16, 8, 21, 14],
    "Missouri": ["35.16%", 15, 9, 21, 20],
    "Montana": ["27.45%", 13, 5, 25, 16],
    "Nebraska": ["3.20%", 13, 23, 7, 22],
    "Nevada": ["15.89%", 13, 3, 17, 20],
    "New Hampshire": ["84.32%", 12, 8, 24, 7],
    "New Jersey": ["41.72%", 3, 8, 13, 24],
    "New Mexico": ["31.99%", 28, 16, 5, 9],
    "New York": ["62.88%", 29, 2, 16, 23],
    "North Carolina": ["59.73%", 17, 18, 10, 11],
    "North Dakota": ["1.72%", 28, 25, 27, 18],
    "Ohio": ["30.92%", 20, 9, 0, 12],
    "Oklahoma": ["28.80%", 6, 7, 0, 24],
    "Oregon": ["48.51%", 16, 25, 18, 29],
    "Pennsylvania": ["58.60%", 1, 29, 26, 16],
    "Rhode Island": ["54.38%", 21, 11, 7, 5],
    "South Carolina": ["68.19%", 6, 16, 1, 2],
    "South Dakota": ["3.93%", 5, 23, 22, 8],
    "Tennessee": ["52.83%", 25, 0, 19, 8],
    "Texas": ["37.33%", 3, 3, 17, 7],
    "Utah": ["34.48%", 19, 7, 12, 11],
    "Vermont": ["77.811%", 7, 21, 1, 0],
    "Virginia": ["62.93%", 18, 27, 17, 9],
    "Washington": ["52.74%", 24, 8, 15, 7],
    "Washington DC": ["33.90%", 0, 7, 18, 4],
    "West Virginia": ["79.01%", 23, 24, 17, 13],
    "Wisconsin": ["48.98%", 12, 22, 20, 21],
    "Wyoming": ["18.42%", 0, 21, 7, 29
 ],}


def check_valid_input_state(input_state):
    """
    takes a string as a input and check if the given state is in the state_directory and returns false
    """

    for state in STATE_PLANT_DICTIONARY.keys():
        if input_state.lower().strip() == state.lower():
            return True
    return False


def get_request():
    """
    reads forest_request.csv file and verify the input. Return the response based on the
    legitimacy of the input
    """

    try:
        with open("forest_request.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                input_state = line
    except FileNotFoundError as err:
        print(err)
        return

    if len(input_state) != 2 or not check_valid_input_state(input_state[1]):
        write_invalid()
        return

    return input_state[1]


def write_invalid():
    """
    Writes invalid request response
    """

    with open("forest_response.csv", 'w') as outfile:
        outfile.write("Invalid Request. Please check if the file name matches `forest_request.csv`"
                      " and if the data parameters match `State, <your requested state>`. "
                      "For example: State, Washington")


def write_valid(state, forest_percent):
    """
    Writes valid request response
    """
    with open("forest_response.csv", 'w') as outfile:
        outfile.write(state + ", " + str(forest_percent))


def delete_request_file():
    """
    Deletes the request file
    """
    try:
        os.remove("forest_request.csv")
    except FileNotFoundError:
        pass


# get State from request
if get_request():
    requested_state = get_request().strip()

    if check_valid_input_state(requested_state):
        forest_percentage = STATE_PLANT_DICTIONARY[requested_state]
        write_valid(requested_state, forest_percentage)

# remove request file
delete_request_file()


