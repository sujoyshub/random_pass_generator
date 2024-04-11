# Random Password Generator
This project creates a Python based Flask web application that generates random passwords of length 10 characters, stores the password history and allows downloading the last generated passwords.

![Output](https://github.com/sujoyshub/sujoyshub.github.io/blob/main/images/rdm_pass_gen.jpg)


---

1.   Import necessary modules from the Flask framework. Flask is a web framework for Python.

2.   Import the `random` and `string` modules. These modules are used for generating random passwords.

3.   Create a Flask application instance named `app`.

4.   Initializing an empty list to store the history of generated passwords.

5.   Defining a function named `generate_password` that generates a random password of a specified length. The default length is set to 10 characters.

6.   Defining a route for the root URL ('/'). This route handles both GET and POST requests.

7.   Defining a function named `index` to handle requests to the root URL.

8.   Declaring `password_history` as a global variable within the function scope.

9. Inside the  
    - Checking the request method. If it's a POST request:
        - Generating a new password if the 'action' parameter in the form data is 'regenerate'.
        - Clearing the password history if the 'action' parameter is 'clear'.
        - Generating a password of custom length if the 'action' parameter is 'custom_length'.
    - If it's a GET request, generating a default password.
    - Rendering the 'index.html' template with the generated password, password history, and an optional warning message.

10.   Defining a route for '/download'.

11.   Defining a function to handle the '/download' route.

12. Inside the  
    - Checking if there is a password in the history.
    - If a password exists, creating a link to download the last generated password as a text file.
    - If no password exists, returning a message indicating that no password has been generated yet.

13.   Checking if the script is being executed directly.
    - If it is, running the Flask application in debug mode.
