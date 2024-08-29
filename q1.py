def mark_present(student_name: str):
    if student_name not in present_students:
        present_students.append(student_name)
        print(f"{student_name} has been marked as present.")
    else:
        print(f"{student_name} is already marked as present.")

def remove_student(student_name: str):
    if student_name in present_students:
        present_students.remove(student_name)
        print(f"{student_name} has been removed from the attendance list.")
    else:
        print(f"{student_name} is not in the attendance list.")

def is_present(student_name: str) -> bool:
    return student_name in present_students

def display_attendance():
    if present_students:
        print("Present Students:")
        for student in present_students:
            print(f"  {student}")
    else:
        print("No students are marked as present.")

def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        less_than_pivot=[x for x in arr[1:] if x<=pivot]
        greater_than_pivot=[x for x in arr[1:] if x>pivot]
        return quicksort(less_than_pivot)+[pivot]+quicksort(greater_than_pivot)

def sort_attendance():
    global present_students
    present_students=quicksort(present_students)
    print("Attendance list has been sorted.")

present_students=[]
mark_present("Rahul")
mark_present("David")
mark_present("Aryan")
mark_present("Devin")
mark_present("Debjit")
mark_present("Vaibhav")

ch=input("Enter student name to mark present:")
mark_present(f"{ch}")
display_attendance()

ch2=input("Enter student name to remove:")
remove_student(f"{ch2}")

display_attendance()

ch3=input("Enter student name to check attendance:")
print(f"Is {ch3} present?")
result=is_present(ch3)
print(result)


sort_attendance()
display_attendance()
