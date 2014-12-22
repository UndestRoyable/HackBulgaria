import requests
import json


all_courses = {}


def list_courses():
    r = requests.get('https://hackbulgaria.com/api/students/', verify=False)
    print(r.status_code)
    courses_list = []
    final_list_course = []

    for students in r.json():
        for courses in students["courses"]:
            courses_list.append(courses["name"])
    for item in set(courses_list):
        final_list_course.append(item)

    for i in range(0, len(final_list_course)):
        all_courses[i] = final_list_course[i]

    for courses in all_courses:
        print("[{}]-{}".format(courses, all_courses[courses]))

    return all_courses


def match_teams(course_id, team_size, group_time):
    r = requests.get('https://hackbulgaria.com/api/students/', verify=False)
    course_name = all_courses[course_id]
    list_student = []
    group_list = []

    for student in r.json():
        for course in student["courses"]:
            if course['group'] == group_time and course['name'] == course_name:
                list_student.append(student['name'])

    for students in list_student:
        group_list.append(students)
        if len(group_list) == team_size:
            for i in group_list:
                print("\n{} \n".format(i))
            print("@@@@@@@")
            group_list = []


def main():
    print("Welcome to HackFMI Team Matcher!")
    print("There are some useful commands which you can use: ")
    print("list_courses - lists all available courses.")
    print("match_teams <course_id> <team_size> <group_time>")
    print("exit - to get the hell out of here!")
    while True:
        command = input("Enter some data, son > ")
        if command == "list_courses":
            list_courses()
        elif command.find("match_teams") != -1:
                args = command.split(" ")
                if len(args) != 4:
                    print("Invalid arguments! Enter some valid args, son!")
                list_courses()
                match_teams(int(args[1]), int(args[2]), int(args[3]))
        elif command == "exit":
            break

if __name__ == '__main__':
    main()
