import sys
from pathlib import Path

# Đường dẫn thư mục hiện tại của file task4.py
BASE_DIR = Path(__file__).resolve().parent

sys.stdout.reconfigure(encoding='utf-8')
#module (là file/thư viện Python chứa code có sẵn)
import math
print(math.sqrt(25))


print("Hello AI Pioneer")


print("===== 1. VARIABLES =====")
name = "Thuong"
age = 20
score = 8.5
is_student = True

print("Name:", name)
print("Age:", age)
print("Score:", score)
print("Is student:", is_student)


print("\n===== 2. DATA TYPES =====") 
print(type(name))
print(type(age))
print(type(score))
print(type(is_student))


print("\n===== 3. IF ELSE =====")
score = 8.5

if score >= 8:
    print("Hoc luc: Gioi")
elif score >= 6.5:
    print("Hoc luc: Kha")
elif score >= 5:
    print("Hoc luc: Trung binh")
else:
    print("Hoc luc: Yeu")


print("\n===== 4. LIST =====")
scores = [7.5, 8.0, 9.0, 6.5, 10.0]

print("Danh sach diem:", scores)
print("Diem dau tien:", scores[0])
print("Diem thu hai:", scores[1])
print("So luong diem:", len(scores))

scores.append(8.8)
print("Sau khi them:", scores)

total = sum(scores)
print("Tong diem:", total)

average = sum(scores) / len(scores)
print("Diem trung binh:", average)


print("\n===== 5. FOR LOOP =====")
scores = [7.5, 8.0, 9.0, 6.5, 10.0]

for score in scores:
    print(score)

print("/nCac diem >= 8:")
for score in scores:
    if score >= 8:
        print(score)

print("\nĐếm số sinh viên đạt điểm cao") 
count = 0
for score in scores:
    if score >= 8:
        count = count + 1

print("So diem >= 8:", count)


print("\n===== 6. TUPLE =====")
student_info = ("Thuong", 20, "AI")

print(student_info)
print(student_info[0])
print(student_info[1])
print(student_info[2])


print("\n===== 7. DICTIONARY =====")
student = {
    "name": "Tien",
    "age": 20,
    "score": 8.5
}

print(student)
print("Name:", student["name"])
print("Age:", student["age"])
print("Score:", student["score"])

#Thay doi gia tri
student["score"] = 9.0
print(student)

#them phan tu
student["major"] = "Information Technology"
print(student)

#List chứa nhiều Dictionary
students = [
    {
        "name": "An",
        "score": 8.0
    },
    {
        "name": "Binh",
        "score": 6.5
    },
    {
        "name": "Cuong",
        "score": 9.0
    }
]
print(students)
#Duyệt dữ liệu
for student in students:
    print(student["name"], student["score"])


print("\n===== 8. FUNCTION =====")
def calculate_average(scores):
    average = sum(scores) / len(scores)
    return average

scores = [7, 8, 9, 10]
result = calculate_average(scores)
print("Diem trung binh:", result)

#Function tìm điểm lớn nhất
def find_max_score(scores):
    return max(scores)
scores = [7, 8, 9.5, 6, 10]
highest = find_max_score(scores)
print("Diem cao nhat:", highest)


print("\n===== 9. EXCEPTION =====")
# Lưu ý: Khi chạy script này trực tiếp từ terminal, hãy nhập một số nguyên khi được hỏi
try:
    number = int(input("Nhap mot so: "))
    print("Ban da nhap:", number)
except ValueError:
    print("Loi: ban phai nhap mot so!")


#Đọc/ghi file TXT
print("\n===== 10. FILE =====")
with open(BASE_DIR / "result.txt", "w", encoding="utf-8") as file:
    file.write("Hello AI Pioneer\n")
    file.write("Python Task 4")
#Đọc file
with open(BASE_DIR / "result.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)


print("\n===== 11. READ CSV =====")
#Đọc CSV bằng Python
import csv
with open(BASE_DIR / "student.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

#Chuyển dữ liệu CSV thành số
with open(BASE_DIR / "student.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["name"]
        age = int(row["age"])
        score = float(row["score"])

        print(name, age, score)


#BÀI HOÀN CHỈNH TASK 4
# 1. Đọc toàn bộ sinh viên
# 2. In danh sách
# 3. Tính điểm trung bình
# 4. Tìm sinh viên điểm cao nhất
# 5. Đếm số sinh viên có điểm >= 8

import csv


students = []


# Đọc file CSV (sử dụng student.csv trong cùng thư mục)
with open(BASE_DIR / "student.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        student = {
            "name": row["name"],
            "age": int(row["age"]),
            "score": float(row["score"])
        }

        students.append(student)


print("===== DANH SACH SINH VIEN =====")

for student in students:

    print(
        student["name"],
        student["age"],
        student["score"]
    )


# Tính tổng điểm
total_score = 0

for student in students:

    total_score += student["score"]


# Tính trung bình
average_score = total_score / len(students)

print("\nDiem trung binh:", average_score)


# Tìm sinh viên điểm cao nhất
best_student = students[0]

for student in students:

    if student["score"] > best_student["score"]:

        best_student = student


print(
    "Sinh vien diem cao nhat:",
    best_student["name"],
    best_student["score"]
)


# Đếm số sinh viên >= 8
count = 0

for student in students:

    if student["score"] >= 8:

        count += 1

print("So sinh vien co diem >= 8:", count)
