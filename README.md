# my-first-blog
Requirements
---------------------
Operation system - GNU/LINUX.

Language - Python > 3.0

Python packages from PyPi (pip):
  1. django==1.8
  2. django-suit==0.2.18
  3. django-disqus
  4. django-import-export
  5. tablib
  6. django-suit-locale

Installation
---------------------
Open the GNU/LINUX terminal and ENTER THIS:
```
~$sudo pip3 install -r requirements.txt
~$sudo python3 manage.py makemigrations
~$sudo python3 manage.py migrate
~$sudo python3 manage.py syncdb
```


RUN
------------------
```
~$ sudo python3 manage.py runserver
```
To access the application go to the URL http://localhost:8000/ or http://127.0.0.1:8000/
