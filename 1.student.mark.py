
students = []           
courses = []           
marks = {}     

def add_student():
    sid = input("Enter Student ID: ").strip()
    for s in students:
        if s[0] == sid:
            print("Student ID already exists!\n")
            return
    name = input("Enter Student Name: ").strip()
    students.append((sid, name))
    print("Student added successfully!\n")

def add_course():
    cid = input("Enter Course ID: ").strip()
    for c in courses:
        if c[0] == cid:
            print("Course ID already exists!\n")
            return
    name = input("Enter Course Name: ").strip()
    courses.append((cid, name))
    print("Course added successfully!\n")

def record_mark():
    if not students:
        print("No students available. Add students first!\n")
        return
    if not courses:
        print("No courses available. Add courses first!\n")
        return

    print("Available Students:")
    for s in students:
        print(f"  {s[0]} - {s[1]}")
    
    sid = input("\nEnter Student ID: ").strip()
    if not any(s[0] == sid for s in students):
        print("Student not found!\n")
        return

    print("Available Courses:")
    for c in courses:
        print(f"  {c[0]} - {c[1]}")

    cid = input("\nEnter Course ID: ").strip()
    if not any(c[0] == cid for c in courses):
        print("Course not found!\n")
        return

    try:
        score = float(input("Enter Mark (0-100): "))
        if not 0 <= score <= 100:
            print("Mark must be between 0 and 100!\n")
            return
    except ValueError:
        print("Invalid mark! Please enter a number.\n")
        return

    marks[(sid, cid)] = score
    print("Mark recorded successfully!\n")

def show_marks_by_course():
    if not courses:
        print("No courses available!\n")
        return

    print("Available Courses:")
    for c in courses:
        print(f"  {c[0]} - {c[1]}")

    cid = input("\nEnter Course ID to view marks: ").strip()
    if not any(c[0] == cid for c in courses):
        print("Course not found!\n")
        return

    course_name = next(c[1] for c in courses if c[0] == cid)
    print(f"\n=== Marks for {course_name} ({cid}) ===")
    
    found = False
    for (sid, cid_key), score in marks.items():
        if cid_key == cid:
            student_name = next(s[1] for s in students if s[0] == sid)
            print(f"Student: {student_name} (ID: {sid}) → {score}/100")
            found = True
    
    if not found:
        print("No marks recorded for this course yet.\n")
    else:
        print()  

def list_students():
    if not students:
        print("No students added yet.\n")
    else:
        print("=== List of Students ===")
        for sid, name in students:
            print(f"ID: {sid} | Name: {name}")
        print()

def list_courses():
    if not courses:
        print("No courses added yet.\n")
    else:
        print("=== List of Courses ===")
        for cid, name in courses:
            print(f"ID: {cid} | Name: {name}")
        print()


while True:
  
    print("    Student Mark Management System ")
    print("1. Add New Student")
    print("2. Add New Course")
    print("3. Record Mark")
    print("4. Show Marks by Course")
    print("5. List All Students")
    print("6. List All Courses")
    print("0. Exit")
    print("-" * 42)

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        add_course()
    elif choice == "3":
        record_mark()
    elif choice == "4":
        show_marks_by_course()
    elif choice == "5":
        list_students()
    elif choice == "6":
        list_courses()
    elif choice == "0":
        print("Thank you! Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")




    
    


