import requests
import time
import re


HOST = "127.0.0.1"
PORT = 8090


url = f"http://{HOST}:{PORT}/api"


longitude           = 0
latitude            = 0
parallactic_angle   = 0
on                  = ""
angle_hour           = ""


# Function to get the information about the celestial object
def get_status_objects():
    response = requests.get(f"{url}/main/status")

    if response.status_code == 200:
        return response.json()
    else:
        print("Cant get the status from Stellarium!")
        return None


#
def get_info_about_object(name):
    response = requests.get(f"{url}/objects/info?name={name}&format=json")

    if response.status_code == 200:
        return response.json()
    else:
        print("Cant find the given object!")
        return None


if "__main__" == __name__:

    start = time.time()

    while True:
        current = time.time()
        elapsed = current - start

        status = get_status_objects()

        list_of_info = status["selectioninfo"].split("<br/>")

        object_name = list_of_info[0].split(">")[1].replace("</h2", "")
    
        # object_name = re.findall(r'\[.*?\]', list_of_info[0])
        
        if elapsed >= 1:
            if len(object_name) > 0:
                # object_name = object_name[0].replace("[", "").replace("]", "")
                content = get_info_about_object(object_name)
                # print(content)

                longitude           = content["glong"]
                latitude            = content["glat"]
                parallactic_angle   = content["parallacticAngle"]
                on                  = content["name"]
                angle_hour          = content["meanSidTm"]
    
                print(on)
                print(f"Coordinates are: [ glat: {latitude}, glong: {longitude}, pa: {parallactic_angle}] for: {on}")

                start = current
