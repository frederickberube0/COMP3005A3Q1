Instructions to run:

1. In command prompt, run `pip install psycopg2`
2. On postgres, create an empty database.
3. While in the COMP3005A3Q1-MAIN folder, run the python file in command prompt, `python3 src/main.py`
4. Answer the prompts
5. Run the commands

Video: youtube

Explanation of functions

The main() function has the main loop and asks the user for their decisions, and if required, asks for the additional variables.

1: getAllStudents() This function gets all the tuples from the student table and prints them to the console.
2: addStudent(first_name, last_name, email, enrollment_date) This function adds the specified value to the students table.
3: updateStudentEmail(student_id, new_email) This function updates the tuple with the specified student_id with a new email.
4: deleteStudent(student_id) This function deletes the tuple with the specified student_id from the students table.
