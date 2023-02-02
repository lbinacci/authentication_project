# authentication_project


This is a Flask Python web application code that provides user registration and login functionalities. It uses the Flask LoginManager library to manage user sessions, and the flask_utils and login_utils modules to perform various actions such as sending emails with OTPs and checking passwords. The application uses a MySQL database to store user information.

####################### API FRONT-END ############################

http://127.0.0.1:5000/registration:

This endpoint returns the registration form for creating a new user account.

http://127.0.0.1:5000/login:

This endpoint returns the login form for an existing user.

http://127.0.0.1:5000/logout:

This endpoint in needed to logout the user

http://127.0.0.1:5000/logged_in:

This endpoint returns a html page when the user perform a succesful login. Access to this endpoint requires a valid login.

http://127.0.0.1:5000/two_fa_login_template:

This endpoint returns the template for two-factor authentication, which is triggered when the user has enabled 2FA for their account. If the user is not logged in or if their account does not exist, they will be redirected to the login page.

######################## API BACK-END #############################

http://127.0.0.1:5000/login_user:
{ 
"username": str,
"password": str 
}

This endpoint logs in a user. If the user's account exists and their password is correct, they will either be logged in directly if 2FA is not enabled, or they will be redirected to the 2FA template if it is enabled.

http://127.0.0.1:5000/register_user:
{            
"username": str,
"password": str,
"email": str,
"birthdate": str,
"first_name": str,
"last_name": str,
"otp": boolean
}
This endpoint creates a new user account. The API takes in the following parameters: username, password, email, birthdate, first_name, last_name, and otp (a flag for enabling 2FA). If the provided username or email already exists, the API will return an error. If the provided email is in an invalid format, the API will return an error. If the account is created successfully, the API will return a success message.

http://127.0.0.1:5000/two_fa_login:
{ 
"otp": str 
}
This endpoint logs in a user with 2FA. The API takes in the following parameter: otp. If the user is not logged in, they will be redirected to the login page. If the user's account does not exist, the API will flash an error message. If the provided otp matches the one stored for the user, the user will be logged in.

##########################################################################

to start the project you just need to download the docker-image "docker pull mrbeena/auth_project".
Next you can do "docker-compose up". Now the project should be running.

Now you can start register, login, login with OTP and login using the front-end api
