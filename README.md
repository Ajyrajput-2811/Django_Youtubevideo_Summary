# Django_Youtubevideo_Summary
Implemented YouTube Data API integration to fetch video details, including metadata, captions, and transcripts, enabling efficient data retrieval for summarization using Django.

## Installing
Step by step commands on how to run this project on your computer.

1)- Install Virtualenv
```
pip install virtualenv
```
2)- Create Virtualenv
```
virtualenv venv
```
3)- Activate virtual env
```
source env/bin/activate
```
4)- Install requirements
```
pip install -r requirements.txt
```
Note: Above lines are required for first time installation.

5)- Execute below commands
```
python manage.py makemigrations
python manage.py migrate
```
Note: Above commands should be executed if there is any db level changes

6)- Create superuser for admin access and follow instruction, if not created one
```
python manage.py createsuperuser
```
## Running the server
```
python manage.py runserver
```
And the project is ready for use on your computer!.
