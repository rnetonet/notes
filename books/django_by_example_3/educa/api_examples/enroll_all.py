import requests

base_url = r"http://127.0.0.1:8000/api/"

r = requests.get(f"{base_url}courses/")
courses = r.json()

avaiable_courses = ', '.join([course["title"] for course in courses])

username = input("username: ")
password = input("password: ")

for course in courses:
    course_id = course["id"]
    course_title = course["title"]

    r = requests.post(f"{base_url}courses/{course_id}/enroll/", auth=(username, password))

    print(r.json())

    if r.status_code == 200:
        print(f"Enrolled in {course_title}")