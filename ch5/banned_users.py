#! /bin/python3

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

# if not(user in banned_users): 
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

