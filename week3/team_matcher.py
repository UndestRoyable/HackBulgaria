import requests
import json

def list_all_courses():
    api_data = requests.get("https://hackbulgaria.com/api/students/", verify = False)
    #return api_data.status_code
    api_data_json = api_data.json()
    courses = set()
    for dictionary in api_data_json:
        for course in dictionary["courses"]:
            courses.add(course["name"])

    return courses



def main():
    print(list_all_courses())

if __name__ == '__main__':
    main()