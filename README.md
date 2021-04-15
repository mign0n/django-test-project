# Test project.

This is a web service that allow you to find out which projects a particular
Github user has made pull requests, and it was merged.

## Steps to run server on Linux

1. Open a terminal, create a directory and navigate to it.  
```
~$ mkdir ghuseract && cd ghuseract
```
2. Clone the repository and navigate to `django-test-project` directory.  
```
~$ git clone https://github.com/mign0n/django-test-project.git
```
```
~$ cd django-test-project
```
3. Create virtual environment and activate it.  
```
~$ python -m venv env && source env/bin/activate
```
4. Install requirements.  
```
(env) ~$ pip install -r requirements.txt
```
5. Set the required environment variables.
```
(env) ~$ export SECRET_KEY=$(gpg --gen-random --armor 1 37)
```
```
(env) ~$ export GITHUB_TOKEN=<your-personal-access-token>
```
6. Start server and go to http://127.0.0.1:8000/
```
(env) ~$ python manage.py runserver
```
