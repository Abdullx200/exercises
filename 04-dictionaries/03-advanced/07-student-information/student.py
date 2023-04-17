# Write your code here


def process_data(string_data = []):
    new_dict = {}
    for i in string_data:
        name, age, *courses = i.split(',')
        new_dict[name] = {
            'age':int(age),
            'courses': courses
        }
    return new_dict

def average_age(data):
    leeftijd = 0
    keren = 0
    for i in data.values():
        leeftijd += i['age']
        keren +=1

    return leeftijd/keren

def courses(data):
    genomen = set()
    for student in data.values():
        genomen.update(student['courses'])
    return genomen

def most_common_courses(data):
    course_counts = {}
    for student in data.values():
        for course in student['courses']:
            if course not in course_counts:
                course_counts[course] = 0
            course_counts[course] += 1
    max_count = max(course_counts.values())
    return {
        course
        for course in course_counts.keys()
        if course_counts[course] == max_count
    }

    