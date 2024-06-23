import requests
import time
import re


HOST = "127.0.0.1"
PORT = 8090


url = f"http://{HOST}:{PORT}/api"


def get_status_objects():
    response = requests.get(f"{url}/main/status")

    if response.status_code == 200:
        return response.json()
    else:
        print("Cant get the status from Stellarium!")
        return None


def get_info_about_object(name):
    response = requests.get(f"{url}/objects/info?name={name}&format=json")

    if response.status_code == 200:
        return response.json()
    else:
        print("Cant find the given object!")
        return None


if "__main__" == __name__:
    # status  = get_status_objects()
    # content = get_info_about_object("moon")

    # print(status["selectioninfo"])

    while True:
        status = get_status_objects()

        list_of_info = status["selectioninfo"].split("<br/>")

        object_name = re.findall(r'\[.*?\]', list_of_info[0])
        object_name = object_name[0].replace("[", "").replace("]", "")

        if len(object_name) > 0:
            content = get_info_about_object(object_name)

            print(content)
        time.sleep(1)
    # print(content)
