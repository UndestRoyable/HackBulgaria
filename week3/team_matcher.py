import requests
import json
from random import shuffle

api_data = requests.get("https://hackbulgaria.com/api/students/", verify = False)
api_data_json = api_data.json()

def menu_message():
    print("Hello, you can use one the the following commands:")
    print("list_courses - this lists all the courses that are available now.")
    print("match_teams <course_id>, <team_size>, <group_time>")
    print("-----------------------------------------")


def list_all_courses():
    
    courses = []
    for item in api_data_json:
        for course in item["courses"]:
            if course["name"] not in courses:
                courses.append(course["name"])

    print("HackBulgaria's courses:")
    counter = 0

    for course in courses:
        counter += 1 
        print("[{}]".format(counter) + course)


def match_teams(course_id, team_size, group_time):

    hack_courses = []
    for item in api_data_json:
        for course in item["courses"]:
            if course["name"] not in hack_courses:
                hack_courses.append(course["name"])

    course_wanted = hack_courses[course_id]
    persons = []

    for person in api_data_json:
        for course in person["courses"]:
            if course["name"] == course_wanted and course["group"] == group_time:
                persons.append(person["name"])
                break
    
    broq4 = 0 #KEEP CALM, IVO! =D
    shuffle(persons)
    for i in range(len(persons)):
        if broq4 == team_size:
            print("=========================")
            broq4 = 0
        print (persons[i])
        broq4 += 1

def command_parser():
    command = input("Enter command:")
    if command == "list":
        list_all_courses()
    else:
        raise ValueError("Invalid command! Available commands: [list] and [match_teams <course_id>, <team_size>, <group_time>] ")
    '''if "match" in command:
        command.split(" ")
        match_teams(command[1], command[2], command[3])'''

def main():
    print(menu_message())
    
    print(command_parser())
    
    print(match_teams(3, 2, 2)) # In command_parser implement user choosing for the function

if __name__ == '__main__':
    main()