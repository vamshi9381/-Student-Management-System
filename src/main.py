from src.services.student_service import StudentService


def main():

    service = StudentService()

    while True:

        print("\n================================")
        print("    STUDENT MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            service.add_student()

        elif choice == "2":
            service.view_students()

        elif choice == "3":
            service.search_student()

        elif choice == "4":
            service.update_student()

        elif choice == "5":
            service.delete_student()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
