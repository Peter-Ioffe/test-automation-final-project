import csv
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET


###########################################################################
# Function Name: get_data
# Function Description: This function reads data from an external XML file
# Function Parameters: node_name - string - node (tag) name
# Function Return: string - node (tag) value
###########################################################################
def get_data(node_name):
    root = ET.parse("C:/Automation/test_automation_final_project/configuration/data.xml").getroot()
    return root.find(".//" + node_name).text


###########################################################################
# Function Name: wait
# Function Description: This function waits for a specific condition to be
#                       met for a web element, such as its presence or visibility.
# Function Parameters:
#   - for_element: string - The condition to wait for ("element_exists" or "element_displayed").
#   - elem: tuple - A tuple containing the locator strategy and locator value of the element.
# Function Return: None
###########################################################################
def wait(for_element, elem):
    if for_element == "element_exists":
        WebDriverWait(conf.driver, int(get_data("WaitTime"))).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == "element_displayed":
        WebDriverWait(conf.driver, int(get_data("WaitTime"))).until(EC.visibility_of_element_located((elem[0], elem[1])))


###########################################################################
# Function Name: read_csv
# Function Description: This function reads data from a CSV file and returns it as a list of rows.
# Function Parameters:
#   - file_name: string - The file path of the CSV file to read.
# Function Return: list - The 'data' list containing rows, where each row is a list of strings.
###########################################################################
def read_csv(file_name):
    data = []
    with open(file_name, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data), row)
        return data


###########################################################################
# Function Name: get_timestamp
# Function Description: This function returns the current timestamp in seconds
#                       since the epoch (January 1, 1970).
# Function Parameters: None
# Function Return: float - The current timestamp.
###########################################################################
def get_timestamp():
    return time.time()


# Enum for selecting between displayed element or existing element, wait method uses this enum
class For:
    ELEMENT_EXISTS = "element_exists"
    ELEMENT_DISPLAYED = "element_displayed"
