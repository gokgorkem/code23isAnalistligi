from pymongo import MongoClient

# MongoDB'ye bağlan
client = MongoClient("mongodb+srv://gorkemgok:Gorkem33@code23.pmipjub.mongodb.net/")
db = client["schoolDB"]

# Koleksiyonlar
students_col = db["students"]
courses_col = db["courses"]
instructors_col = db["instructors"]
enrollments_col = db["enrollments"]
departments_col = db["departments"]
classrooms_col = db["classrooms"]
schedules_col = db["schedules"]
random_number = "S202"
"""
# Öğrenci ekleme (insert_one)
student = [
    {
        "student_id": "S001",
        "name": "Ali Altaş",
        "age": 21,
        "department_id": "D001",
        "email": "ali@example.com",
        "address": {
            "street": "123 Main St",
            "city": "Istanbul",
            "postal_code": "34000"
        }
    },
    {
        "student_id": random_number,
        "name": "Ayşe Topçu",
        "age": 24,
        "department_id": "D002",
        "email": "aysetopcu@example.com",
        "address": {
            "street": "456 Street",
            "city": "Ankara",
            "postal_code": "06000"
        }
    }
]
students_col.insert_many(student)

# Eğitmen ekleme (insert_many)
instructors = [
    {
        "instructor_id": "I001",
        "name": "Dr. Ahmet Yılmaz",
        "department_id": "D001",
        "email": "ahmet@example.com"
    },
    {
        "instructor_id": "I002",
        "name": "Dr. Ayşe Kaya",
        "department_id": "D002",
        "email": "ayse@example.com"
    }
]
instructors_col.insert_many(instructors)

# Ders ekleme (insert_one)
course = {
    "course_id": "C001",
    "course_name": "Database Systems",
    "credits": 4,
    "department_id": "D001",
    "instructor_id": "I001",
}
courses_col.insert_one(course)

# Bölüm ekleme (insert_many)
departments = [
    {
        "department_id": "D001",
        "department_name": "Computer Science",
        "building": "Engineering Block",
        "head_of_department": "Dr. Ahmet Yılmaz"
    },
    {
        "department_id": "D002",
        "department_name": "Physics",
        "building": "Science Block",
        "head_of_department": "Dr. Ayşe Kaya"
    }
]
departments_col.insert_many(departments)

# Kayıt ekleme (insert_one)
enrollment = {
    "enrollment_id": "E001",
    "student_id": "S001",
    "course_id": "C001",
    "enrollment_date": "2024-01-10",
    "grade": "AA"
}
enrollments_col.insert_one(enrollment)

# Sınıf ekleme (insert_one)
classroom = {
    "classroom_id": "CR001",
    "building": "Engineering Block",
    "room_number": "101",
    "capacity": 30
}
classrooms_col.insert_one(classroom)

# Program ekleme (insert_one)
schedule = {
    "schedule_id": "SC001",
    "course_id": "C001",
    "classroom_id": "CR001",
    "day": "Monday",
    "time": "09:00-11:00"
}
schedules_col.insert_one(schedule)

# Tüm öğrencileri listeleme
print("Tüm Öğrenciler:")
for student in students_col.find():
    print(student)


# Belirli bir öğrenciyi bulma
print("\nBelirli Öğrenci:")
print(students_col.find_one({"student_id": "S202"}))


# Tüm dersleri listeleme
print("\nTüm Dersler:")
for course in courses_col.find():
    print(course)
    

# Tüm eğitmenleri listeleme
print("\nTüm Eğitmenler:")
for instructor in instructors_col.find():
    print(instructor)

# Öğrencinin kayıtlı olduğu dersleri listeleme


print("\nAli'nin Kayıtlı Olduğu Dersler:")
for enrollment in enrollments_col.find({"student_id": "S001"}):
    print(enrollment)
    course = courses_col.find_one({"course_id": enrollment["course_id"]})
    print(course)

# Dersi veren eğitmeni bulma
print("\nDatabase Systems Dersini Veren Eğitmen:")
course = courses_col.find_one({"course_id": "C001"})
instructor = instructors_col.find_one({"instructor_id": course["instructor_id"]})
print(instructor)
# Tüm bölümleri listeleme
print("\nTüm Bölümler:")
for department in departments_col.find():
    print(department)
"""
"""

# Tüm sınıfları listeleme
print("\nTüm Sınıflar:")
for classroom in classrooms_col.find():
    print(classroom)
"""

# Belirli bir dersin programını bulma
print("\nDatabase Systems Dersinin Programı:")
for schedule in schedules_col.find({"course_id": "C001"}):
    print(schedule)