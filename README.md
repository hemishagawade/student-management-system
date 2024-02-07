# Student Management System
This is a simple web application project. The project facilitates the management of student details, allowing users to perform CRUD operations (Create, Read, Update, Delete) on student records.

# Features
--Dashboard: Displays a list of all student records from the database. Users can view, update, and delete existing records. It also includes a button to add a new student.

--Add Student: Provides a form to input new student details and store them in the database.

--Update Student: Allows users to modify existing student details using a form.

# Technologies Used
--Frontend:
HTML
CSS
JavaScript
Bootstrap

--Backend:
Python
Django

# Project Structure:
/student_management_system: Django project directory.

/student_app: Django application directory containing the main logic.

/templates: HTML templates for rendering views.

/static: Static files such as CSS, JavaScript, and images.

models.py: Defines the database models for student records.

views.py: Contains logic for rendering views and handling CRUD operations.

urls.py: Defines URL patterns for routing requests to appropriate views.

# Functionality:
Dashboard:

--Displays a list of all student records fetched from the database.
--Provides options to add, update, and delete student records.
--Clicking on the "Add Student" button redirects to the 'Add Student' page.
--Each student record displayed includes details like name, ID, etc.

Add Student:

--Presents a form for users to input new student details.
--Upon submission, validates the input and adds the student record to the database.
--Redirects back to the dashboard after successful addition.

Update Student:

--Allows users to modify existing student details.
--Fetches the current details of the selected student from the database and pre-fills the form.
--After submission, updates the corresponding record in the database.

