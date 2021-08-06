# Script Created By : Latifat Abdulkareem
# Date Created : 06/08/2021
# Language : Python
# Biostack : Data Science / Vaccine Informatics


import time
import sys
import re
import datetime


regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
regex_slack = '[@]\w+[a-z0-9]+[\._]?[a-z0-9]$'


class Register:

    '''  This Is Anita! The Program Instructor For This Process
         kindly Enter Your Details Accordingly As Anita Will Walk You Through.
         Note To Enter Your Name, Email, Slack and Biostack Respectively in The Correct 'General' Format,
         If Not Anita Will Reject Your Answer Prompt You To Enter The Correct Value!
    '''

    def __init__(self):
        self.hour = datetime.datetime.now().hour
        self.anita_greet = f"Good morning!" if 5 <= self.hour < 12 else "Good Afternoon!" if self.hour < 18 else "Good Evening!" 
        self.anita_intro = '''My Name\'s Anita, I\'ll Be Your Persoanl Assistant Throughout Your Profile Creation!
        We Will Get To Know Each Other As You Proceed With Your Profile Creation...\n
        Kindly Fill In Your Profile Details As Shown Below!\n'''     
        message(f'{self.anita_greet} {self.anita_intro}')
        
    def first_name(self):
        self.first_name = input('First Name : ').title()
        while not self.first_name.isalpha():
            message(f"{'Null' if not self.first_name else self.first_name} Is Not A Name! Kindly Enter Your First Name Only")
            self.first_name = input('Name: ').title()
        message(f'Great! Nice To Meet You {self.first_name}\n'.title())

        return self.first_name

    def last_name(self):
        self.last_name = input('Last Name : ').title()
        while not self.last_name.isalpha():
            message(f"{'Null' if not self.last_name else self.last_name} Is Not A Name! Kindly Enter Your Last Name Only")
            self.last_name = input('Last Name: ').title()
        message(f'Welcome! {self.first_name} {self.last_name}!!!\n'.title())

        return self.last_name

    def user_email(self):
        self.email = input('Email :').lower()
        while not re.search(regex_email, self.email):
            message(f"{'Null' if not self.email else self.email} Is Not A Valid Mail! Kindly Enter A Correct Email")
            self.email = input('email:').lower()
        message(f'You\'re Doing Great! Your Email Is {self.email}!!!\n')

        return self.email

    def slack_channel(self):
        self.slack = input('Slack Username :')
        while not re.search(regex_slack, self.slack):
            message(f"""{'Null' if not self.slack else self.slack} Is Not A Valid Slack Username! Kindly Enter A Correct Slack User Account! 
            Startng with @Username e.g @testuser4""")
            self.slack = input('Slack Account:')
        message(f'Smart One! What a Cute Username --- {self.slack}\n')

        return self.slack

    def user_biostack(self):
        self.biostack = input('BioStack :').title()
        while not self.biostack.isascii:
            message(f"{'Null' if not self.biostack else self.biostack} is not a registered biostack! Kindly Enter your stack")
            self.biostack = input('Name: ').title()
        message(f'Guess What! You Guessed It Right... I also studied {self.biostack} during my College days in 1985\n')

        return self.biostack.title()

class Profile(Register):
    def __init__(self):
        super().__init__()

    def display_profile(self):
        message(f'''Creating Profile...............................
        ************* {self.first_name}'s Profile **************
        <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>
        *Full Name : {self.first_name} {self.last_name} 
        *Email : {self.email} 
        *Slack Username: {self.slack}
        *BioStack: {self.biostack}
        <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>\n
        Profile Created Successfully!\n
        ''')

    def close(self):
        end = '''It\'s been a great time with you.
            See you some other time. 
            Yours sincerely, Anita!
            The program will exit now!'''
        message(end)
        
    

if __name__=='__main__':

    def message(string):
        for i in string:
            sys.stdout.write(i)
            sys.stdout.flush()
            # adding time delay of half second
            time.sleep(0.05)
        print()

    user = Profile()
    user.first_name()
    user.last_name()
    user.user_email()
    user.slack_channel()
    user.user_biostack()
    user.display_profile()
    user.close()

    