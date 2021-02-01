from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from parse import parse
from time import sleep
import time
import json
import pyrebase
import firebase_admin
from firebase_admin import credentials, db


driver = webdriver.Chrome()
driver.get(
    'https://www.metrobus.com/html-default/bootstrap/pages/index.asp#collapseOne')


my_arr = []
complete_dict = {}


# Firebase DB connection


cred = credentials.Certificate(
    "./auth_key/realtime-route-info-firebase-adminsdk-7i9h5-1385f612ff.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://realtime-route-info-default-rtdb.firebaseio.com/'
})

ref = db.reference('routeinfo')

while True:

    buses_info = [my_elem.get_attribute("data-href")
                  for my_elem in driver.find_elements_by_class_name('clickable-row')]

    string_parse_data = '/html-default/avl_location.asp?{}&{}&{}&{}&p{}&{}&{}&{}'

    for bus_info in buses_info:
        my_dict = {}
        route_info = parse(string_parse_data, bus_info)
        # print(route_info)
        for info in route_info:
            new_info = info.split('=')
            # my_dict.append(info)
            my_dict[new_info[0]] = new_info[1]

        # my_dict[my_dict.get('current_route')] = my_dict.pop(1)

        complete_dict[my_dict.get('current_route')] = my_dict
        # my_arr.append({my_dict.get('current_route'): my_dict})

    ref.update(complete_dict)

    # with open('route.json', 'w') as json_file:
    #     json.dump(complete_dict, json_file)

    driver.execute_script("RefreshTimeTrack()")

    time.sleep(40)
