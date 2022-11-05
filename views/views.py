from PyInquirer import prompt
from examples import  custom_style_3
from prompt_toolkit.validation import Validator, ValidationError
import re

def views():
    starter_prompt()

class NameValidator(Validator):
    def validate(self, document):
        '''
            Funcation that validates whether the name entered is valid or not

            arguments:
            document -- contains the information about the input

            returns:
            raises validationerror if email is invalid
        '''

        if len(document.text) < 2:
            raise ValidationError(message="please enter name with length greater than 2", cursor_position=len(document.text))


class EmailValidator(Validator):
     
    
    def validate(self, document):
        '''
            function validates whether the input is a valid email or not

            arguments:
            document -- contains the information about the input

            returns:
            raises validationerror if the email is invalid
        '''
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, document.text):
            raise ValidationError(message='please enter a valid email address', cursor_position=len(document.text))

class PasswordValidator(Validator):
    def validate(self, document):
        ''' 
            function validates the password

            arguments:
            document -- contains the information about teh input

            returns:
            raises validationerror if the password is invalid
        '''
        if len(document.text) < 0:
            raise ValidationError(message='Please enter a valid password',cursor_position=len(document.text))


def starter_prompt():
    ''' 
        args: None
        Function to start the program
    '''
    questions = [{
        'type': 'list',
        'name': 'user_input',
        'message': "HI! Choose what you want to do",
        'choices': ['login', 'sign up', 'exit']
    }]

    answers = prompt(questions=questions, style=custom_style_3)
    user_input = answers.get('user_input')
    
    if user_input == 'login':
        login()
    elif user_input == 'sign up':
        sign_up()
    elif user_input == 'exit':
        exit()

def exit():
    return

def login():
    questions = [{
        'type': "input",
        "name": "email",
        "message": "Please enter your email",
        "validate": EmailValidator,
        },
        {
        'type': "password",
        "name": "password",
        "message": "Please enter your password",
        "validate": PasswordValidator,
        },]
    
    answers = prompt(questions=questions, style=custom_style_3)
    user_input = answers.get('user_input')


def sign_up():
    questions = [
        {
            'type' : "input",
            "name": "name",
            "message" : "Please enter your name",
            "validate": NameValidator
        },
        {
        'type': "input",
        "name": "email",
        "message": "Please enter your email",
        "validate": EmailValidator,
        },
        {
        'type': "password",
        "name": "password",
        "message": "Please enter your password",
        "validate": PasswordValidator,
        },
        {
        'type': "password",
        "name": "password2",
        "message": "Please confirm your password",
        "validate": PasswordValidator,
        }
        ]
    
    answers = prompt(questions=questions, style=custom_style_3)
    email = answers.get('email')
    name = answers.get('name')
    password = answers.get('password')
    password2 = answers.get('password2')
    if password != password2:
        print('The password is not the same')
        sign_up()
    else:
        # signup the user
        pass
        
    

