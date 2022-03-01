# <p align="center">Happy birthday script</p>
<p align="center"><img alt="GitHub Madeby" src="https://img.shields.io/badge/made%20by-AlienFoun-blue"> <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/AlienFoun/happy_birthday-script"> <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Alienfoun/happy_birthday-script?style=social"> <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/AlienFoun/happy_birthday-script"> </p>

# About
**The program allows you to congratulate your friends on the Vkontakte social network on their birthday**


# Project structure
The project is structured for better scaling. In general, files names reflect their essence
* main - contains the main script code
* config - contains the data necessary for the program to work

# Selected libraries
* LiteVkApi
* Datetime
* Random

# Installation
Download Python 3.8 or higher

```
git clone https://github.com/AlienFoun/happy_birthday-script
cd happy_birthday-script
pip install -r requirements.txt
```

Fill in the data to connect to the Vkontakte social network in the file `config.py`

# Usage

Open the terminal and go to the folder with the project, then start the script using the command `python main.py`.

# How it works?

After enabling, the script will send a request to the Vkontakte social network API to get a list of friends with their specified dates of birth in the form:

```Python
{'count': *Number of friends*, 'items': [{'id': *id*, 'first_name': '*first_name*', 'last_name': '*last_name*', 'can_access_closed': True/False, 'is_closed': True/False, 'bdate': '*bdate*', 'track_code': '*code*'}, {...}]}
```

After that we will get the value by the key 'items':

```Python
[{'id': *id*, 'first_name': '*first_name*', 'last_name': '*last_name*', 'can_access_closed': True/False, 'is_closed': True/False, 'bdate': '*bdate*', 'track_code': '*code*'}, {...}]
```

Then we get information about the current date to compare it with the dates of birth of users:

```Python
date = datetime.datetime.today()
current_date = str(date.day)+'.'+str(date.month)
```

After that, using a loop, we go through all the elements from the list, highlighting and formatting the information we need (we remove the year and process the situation if the year is not specified). Then we check whether the current date coincides with the date of birth of the user and if so, we send a random greeting from the list:

```Python
if current_person_bdate == current_date:
  Vk.msg(vk_session, text=choice(congrats_list), userid=person_id)
```
After all this, information is displayed in the terminal, the name and surname of the user to whom the message was sent:

```Python
print(f'Congratulations sent to the user {person["first_name"]} {person["last_name"]}.')
```

### Example

```Python
{'count': 1, 'items': [{'id': 1, 'first_name': 'Pavel', 'last_name': 'Durov', 'can_access_closed': False, 'is_closed': False, 'bdate': '10.10.1984', 'track_code': '*code*'}]

[{'id': 1, 'first_name': 'Pavel', 'last_name': 'Durov', 'can_access_closed': False, 'is_closed': False, 'bdate': '10.10.1984', 'track_code': '*code*'}]

current_date = 10.10

current_person_bdate = 10.10

Congratulations sent to the user Pavel Durov.
```

# Contributions

You can contribute to project in the following ways:

* [Submit new feature ideas](https://github.com/AlienFoun/happy_birthday-script/issues)
* [Report bugs as issues](https://github.com/AlienFoun/happy_birthday-script/issues)
* Star ⭐ this repository
* Spread the word about this project

Do you have an idea for an amazing new feature? Did you find a bug you want to fix? Great! Please submit an issue for discussion before making a pull request.
