user_login
Created by :- Chandan Sharma

Date :- 27-03-2025

Description :- This is a simple login system that allows users to register and login to their accounts and allowing them to create, manage and deleted tasks.

Version :- 1.0

For Set-up the same system follow the below steps :-
1. Clone the repository
2. Create a virtual environment
3. Install the requirements
4. Create a .env file and add the following variables
      1. SECRET_KEY = 'your_secret_key'
      2. RUN_ENV = 'your_run_environment' (i.e. DEV, UAT, LOCAL)
      3. ALGORITHM = 'your_algorithm' (i.e. HS256)
   I am using sqlite DB but you can use any other database like MySQL, PostgreSQL, etc. If  you are changing the DB then you have to change the DATABASES variable in settings.py file.

5. Run the migrations
6. Run the server
7. Open the Postman and go to http://localhost:8000/user/register/ and register a new user
8. Now go to http://localhost:8000/user/login/ and login with the user you just created and you will get the token
9. Use that token for creation of tasks on http://localhost:8000/tasks/ (POST method)
10. You can also use the token for updating and deleting the tasks


Happy Coding :)
