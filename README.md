# Random Password Generator
This project creates a Python based Flask web application that generates random passwords of length 10 characters, stores the password history and allows downloading the last generated passwords.

You can run this Flask application by executing python `rdm_pass_gen.py` in your terminal. 
This will start a local server. You can open your browser and navigate to `http://localhost:5000` to see the password generator interface.

![Output](https://github.com/sujoyshub/random_pass_generator/blob/main/templates/rdm_pass_gen.jpg)


---
The logic of the code is explained below.

1.   Import necessary modules from the Flask framework. Flask is a web framework for Python.

2.   Import the `random` and `string` modules. These modules are used for generating random passwords.

3.   Create a Flask application instance named `app`.

4.   Initializ an empty list to store the history of generated passwords.

5.   Define a function named `generate_password` that generates a random password of a specified length. The default length is set to 10 characters.

6.   Define a route for the root URL ('/'). This route handles both GET and POST requests.

7.   Define a function named `index` to handle requests to the root URL.

8.   Declare `password_history` as a global variable within the function scope.

9. Inside the function
    - Check the request method. If it's a POST request:
        - Generate a new password if the 'action' parameter in the form data is 'regenerate'.
        - Clear the password history if the 'action' parameter is 'clear'.
        - Generate a password of custom length if the 'action' parameter is 'custom_length'.
    - If it's a GET request, generate a default password.
    - Render the 'index.html' template with the generated password, password history, and an optional warning message.

10.   Defining a route for '/download'.

11. Finally, 
    - Checking if there is a password in the history.
    - If a password exists, creating a link to download the last generated password as a text file.
    - If no password exists, returning a message indicating that no password has been generated yet.

## Limitations:
1. Currently, this code can only generate fixed length of passwords which is of 10 characters
2. To enable the Python code to handle copying the last generated password to the clipboard, we modified the Flask route accordingly.
   - Since clipboard access is typically done through JavaScript, we handled this operation on the client side by providing a download link for the password
