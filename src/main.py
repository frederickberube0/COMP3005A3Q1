import psycopg2
from psycopg2 import sql

# Database connection parameters
dbname = input("database name (default=assignment_three): ")
user = input("user name (default=postgres): ")
password = input("password (default=postgres): ")
host = input("host (default=localhost): ")
port = input("port (default=5432): ")

if dbname == "": dbname = "assignment_three"
if user == "": user = "postgres"
if password == "": password = "postgres"
if host == "": host = "localhost"
if port == "": port = "5432"

print("")
# Create a connection to the database
try: 
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
except psycopg2.Error as e:
                print(f"Error running sql command: {e}")
                exit()
                
# Create a cursor object to execute SQL queries
cursor = conn.cursor()

def main():
    with open("./sql/students.sql", 'r') as file:
        # Read the contents of the file into a string
        initial_query = file.read()

    # Execute the query to create the table
    cursor.execute(initial_query)

    # Commit the changes to the database
    conn.commit()


    #Decision loop
    decision = ""
    while decision != "-1":
        decision = ""
        print("""The choices are:
-1: quit
1: getAllStudents()
2: addStudent(first_name, last_name, email, enrollment_date)
3: updateStudentEmail(student_id, new_email)
4: deleteStudent(student_id)
What is your decision?: """)
        while decision != "-1" and decision != "1" and decision != "2" and decision != "3" and decision != "4": 
            decision = input()
            if decision != "-1" and decision != "1" and decision != "2" and decision != "3" and decision != "4": print("Invalid choice, try again: ")

        if decision == "-1":   
            cursor.close()
            conn.close()
            
        elif decision == "1":
            try: 
                getAllStudents()
            except psycopg2.Error as e:
                print(f"Error running sql command: {e}")
                conn.rollback()


        elif decision == "2": 
            first_name = input("What is the first name: ")
            last_name = input("What is the last name: ")
            email = input("What is the email: ")
            enrollment_date = input("What is the enrollment date in format 'yyyy-mm-dd': ")
            try:
                addStudent(first_name, last_name, email, enrollment_date)
            except psycopg2.Error as e:
                print(f"Error running sql command: {e}")
                conn.rollback()

        elif decision == "3":
            student_id = input("What is the student id: ")
            new_email = input("What is the new email: ")
            try:
                updateStudentEmail(student_id, new_email)
            except psycopg2.Error as e:
                print(f"Error running sql command: {e}")
                conn.rollback()

        else:
            student_id = input("What is the student id: ")
            try:
                deleteStudent(student_id)
            except psycopg2.Error as e:
                print(f"Error running sql command: {e}")
                conn.rollback()
        print()


def getAllStudents() -> None:
    """This function gets all the tuples from the student table and prints them to the console."""
    # Execute the query to select all from the table
    cursor.execute("SELECT * FROM students;")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    conn.commit()

def addStudent(first_name, last_name, email, enrollment_date) -> None:
    """This function adds the specified value to the students table."""
    cursor.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}');")
    conn.commit()

def updateStudentEmail(student_id, new_email) -> None:
    """This function updates the tuple with the specified student_id with a new email."""
    cursor.execute(f"UPDATE students SET email = '{new_email}' WHERE student_id = {student_id};")
    conn.commit()

def deleteStudent(student_id) -> None:
    """This function deletes the tuple with the specified student_id from the students table."""
    cursor.execute(f"DELETE FROM students WHERE student_id = '{student_id}';")
    conn.commit()


if __name__ == "__main__": main()

    