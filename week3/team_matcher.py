import requests
import json

def list_all_courses():
    api_data = requests.get("https://hackbulgaria.com/api/students/", verify = False)
    return api_data.status_code
    r.json()


def main():
    print(list_all_courses())

if __name__ == '__main__':
    main()