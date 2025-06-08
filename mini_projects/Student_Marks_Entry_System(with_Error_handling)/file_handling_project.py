std_name=input("Enter name of the student : ")

#checking the marking Conditon here
std_marks=int(input("Enter Mark of student : "))






class customException(Exception):
        pass
if (std_marks>100) or (std_marks<0):
    raise customException("Marks must be between 0 and 100")

try:
    with open("student.txt",'w') as file:

        file.write(std_name)
        file.write(std_marks)
        print("Document is saved successfully !")
except FileNotFoundError:
    print("file not found !")
finally:
    print("File is closed !")



# correct code
# Define custom exception
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    # Take input
    std_name = input("Enter name of the student: ")
    std_marks = int(input("Enter marks of the student: "))

    # Raise custom exception for invalid range
    if std_marks < 0 or std_marks > 100:
        raise CustomException("Marks must be between 0 and 100")

    # Save to file
    try:
        with open("student.txt", 'w') as file:
            file.write(f"{std_name}: {std_marks}\n")
            print("Document is saved successfully!")

    except FileNotFoundError:
        print("File not found!")

    finally:
        print("File is closed!")

except ValueError:
    print("Invalid input! Please enter numeric marks.")
except CustomException as e:
    print("Error:", e)




##
class InvalidMarkError(Exception):
    """Custom exception for invalid marks."""
    pass

students = {}

while True:
    try:
        name = input("Enter student name (or type 'exit' to stop): ")
        if name.lower() == 'exit':
            break

        marks = input(f"Enter marks for {name}: ")
        marks = int(marks)

        if marks < 0 or marks > 100:
            raise InvalidMarkError("Marks must be between 0 and 100.")

        students[name] = marks
        print("Entry recorded successfully!")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")
    except InvalidMarkError as e:
        print("Error:", e)

# Save data to file
try:
    with open("students.txt", "w") as file:
        for name, mark in students.items():
            file.write(f"{name}: {mark}\n")
    print("Data saved to students.txt")
except IOError:
    print("Error saving the file.")
finally:
    print("Program ended.")





    




