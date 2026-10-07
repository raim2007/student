# main.py
students = ["Алексей", "Дильназ", "Максим", "Айгерим"]

def print_students():
    print("Список студентов:")
    for student in students:
        print(f"- {student}")

if __name__ == "__main__":
    print_students()