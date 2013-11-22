"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot on Google Maps.

Part II: Take the data we just parsed and visualize it using popular
Python math libraries.
"""

from collections import Counter

import csv
import matplotlib.pyplot as plt  #as is a handy way to rename
import numpy.numarray as na
#from parse import parse

MY_FILE = "../data/sample_sfpd_incident_all.csv"


def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""
    # Open CSV file, and safely close it when we're done
    opened_file = open(raw_file)
    # Read the CSV data
    csv_data = csv.reader(opened_file, delimiter=delimiter)
    # Setup an empty list
    parsed_data = []
    # Skip over the first line of the file for the headers
    fields = csv_data.next()
    # Iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))
    # Close the CSV file
    opened_file.close()
    return parsed_data


def visualize_days():
    """Visualize data by day of week"""
    data_file = parse(MY_FILE, ",")
    # Returns a dict where it sums the total values for each key.
    # In this case, the keys are the DaysOfWeek, and the values are
    # a count of incidents.     #item in data_file each is a json_dict,so item["DayOfWeek"] == "Tuesday" or a given day
    counter = Counter(item["DayOfWeek"] for item in data_file)
    '''how you'd do it in a for-loop'''
    '''
    counter2 = {}
    for small_dict in data_file:
        if small_dict["DayOfWeek"] in counter2:
            counter2["DayOfWeek"] +=1
        else:
            counter2["DayOfWeek"] = 1
    '''
#Counter({'Tuesday': 37, 'Wednesday': 20, 'Monday': 14,
#         'Thursday': 12, 'Saturday': 7, 'Sunday': 5,
#          'Friday': 4})
    # Separate out the counter into x-axis data(days of week)
    #from y-axis data(number of incdents for each day) to order it correctly when plotting.
    data_list = [
            counter["Monday"], counter["Tuesday"],counter["Wednesday"],
            counter["Thursday"],counter["Friday"],counter["Saturday"],
            counter["Sunday"]
    ]
    day_tuple = tuple(["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"])
    # Assign the data to a plot--we're only giving y coords so x cords will just be 0...N-1 index
    plt.plot(data_list)

    # Assign labels to the plot from day_list-plt.xticks() accepts tuples for labeling x-acis
    plt.xticks(range(len(day_tuple)), day_tuple)
    # Render the plot!
    plt.show()


def visualize_type():
    """Visualize data by category in a bar graph"""
    data_file = parse(MY_FILE, ",")
    # Same as before, this returns a dict where it sums the total
    # incidents per Category.
    counter = Counter((item["DayOfWeek"] for item in data_file ))

    # Set the labels which are based on the keys of our counter.
    labels = tuple(counter.keys())

    # Set where the labels hit the x-axis
    xlocations = na.array(range(len(labels))) + 0.5  #add 0.5 to each tick

    # Width of each bar
    width = 0.5

    # Assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)
    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # Give some more room so the labels aren't cut off in the graph
    plt.subplots_adjust(bottom=0.4)
    # Make the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12,8
    # Render the graph!
    plt.show()


def main():
    visualize_days()  # once this window is closed, the next graph shows
    visualize_type()


if __name__ == "__main__":
    main()
