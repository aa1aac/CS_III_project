from PyInquirer import prompt
from examples import  custom_style_3
from prompt_toolkit.validation import Validator, ValidationError
import re

from models.Models import signUp, signIn, viewPlaylists, viewSongsPerPlaylist, createPlaylist, deletePlaylist, addSong, deleteSong, searchByArtiste, searchBySong

def views():
    starter_prompt()
    return

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
        return

def exit():
    return

def logged_in_prompts():
    '''
        function that shows the prompts to the user.

        args: none
    '''
    questions = [{
        'type' : 'list',
        'name' : 'user_input',
        'message': 'Please choose what you want to do',
        'choices': ['view playlist', 'add playlist', 'remove playlist', 'add music', 'delete music', 'view song', "search music", "logout"]
        }]
    
    answers = prompt(questions=questions, style=custom_style_3)
    user_input = answers.get('user_input')

    if user_input == 'view playlist':
        viewPlaylists()
        logged_in_prompts()
    elif user_input == 'logout':
        starter_prompt()
    elif user_input == 'add playlist':
        questions = [{
        'type': "input",
        "name": "name",
        "message": "Please enter the name of the playlist",
        "validate": NameValidator,
        }
        ]
        answers = prompt(questions=questions, style=custom_style_3)
        name = answers.get('name')
        res = createPlaylist(name)

        if not res:
            print("it was unsuccessful ")
            print('Please try again')
        else:
            print('it was successful')
        
        logged_in_prompts()

    elif user_input == 'remove playlist':
        questions = [{
        'type': "input",
        "name": "name",
        "message": "Please enter the name of the playlist",
        "validate": NameValidator,
        }
        ]

        answers = prompt(questions)
        name = answers.get('name')

        res = deletePlaylist(name)

        if res:
            print("deletion successful")
        else:
            print("deletion unsuccessful")
            print("Let's try one more time")
        
        logged_in_prompts()

    elif user_input == 'add music':
        questions = [{
        'type': "input",
        "name": "playlist",
        "message": "Please enter the name of the playlist",
        "validate": NameValidator,
        },
        {
            'type': "input",
            "name": "song",
            "message" : "Please enter the name of the song",
            "validate": NameValidator
        },
        {
            'type': "input",
            "name": "artist",
            "message" : "Please enter the artist",
            "validate": NameValidator
        }
        ]
        
        answers = prompt(questions)

        playlist = answers.get('playlist')
        song = answers.get('song')
        artist = answers.get('artist')
        res = addSong(song, playlist, artist)

        if res:
            print("addition of song successful")
        else:
            print("addition of the song was not successful")
            print("let's try again")
        
        logged_in_prompts()

    elif user_input == 'delete music':
        # TODO: remove the music form the database
        questions = [{
        'type': "input",
        "name": "playlist",
        "message": "Please enter the name of the playlist",
        "validate": NameValidator,
        }, 
        {
            "type": "input",
            "name" : "music",
            "message": "Please enter the song name",
            "validate": NameValidator,
        },

        {
            "type": "input",
            "name" : "artist",
            "message": "Please enter the artist name",
            "validate": NameValidator,
        }
        ]
        
        answers = prompt(questions)
        song_name = answers.get("music")
        playlist_name = answers.get("playlist")
        artist_name = answers.get("artist")

        res = deleteSong(song_name, playlist_name, artist_name)
        if not res:
            print("Deletion unsuccessful")
            print("Please try again later")

        else:
            print("deletion successful")
        
        logged_in_prompts()
    elif user_input == 'search music':
        questions = [{
        'type': "list",
        "name": "user_input",
        "message": "Please enter the search type",
        "choices" : ['search by artist', 'search by song name']
        }]
        
        answers = prompt(questions)

        user_input = answers.get('user_input')
        
        if user_input == 'search by artist':
            questions = [{
                'type': "input",
                "name": "artist",
                "message": "Please enter the artist name",
                "validate" : NameValidator
             },
            {
                'type': "input",
                "name": "playlist",
                "message": "Please enter the playlist name",
                "validate" : NameValidator
            },
                ]

            answers = prompt(questions)

            artist = answers.get('artist')
            playlist = answers.get('playlist')

            searchByArtiste(artist, playlist)
        if user_input == 'search by song name':
            questions = [{
                'type': "input",
                "name": "song",
                "message": "Please enter the song name",
                "validate" : NameValidator
             },
            {
                'type': "input",
                "name": "playlist",
                "message": "Please enter the playlist name",
                "validate" : NameValidator
            }]
            
            answers = prompt(questions)

            playlist = answers.get('playlist')
            song = answers.get('song')

            searchBySong(song, playlist)



        logged_in_prompts()


    elif user_input == 'view song':
        questions = [{
        'type': "input",
        "name": "name",
        "message": "Please enter the name of the playlist",
        "validate": NameValidator,
        }
        ]

        answers = prompt(questions)
        playListName = answers.get('name')
        viewSongsPerPlaylist(playListName)
        logged_in_prompts()




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
    email = answers.get('email')
    password = answers.get('password')

    res = signIn(username=email, password=password)

    # if login successful, for now passed as true
    if res:
        logged_in_prompts()
    else:
        print("*****   Invalid credentials  ******* ")
        print("*****   Let's restart        ******* ")
        login()
        


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
        print("The password is not the same")
        print(" let's start again ")
        sign_up()
    else:
        res = signUp(email, password=password)
        if res:
            print("The user has been created! ")
            starter_prompt()
        else:
            print("signup unsuccessful")
            sign_up()

        

        
    

