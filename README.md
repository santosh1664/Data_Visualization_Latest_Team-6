- Create an virtual env 
    1. Check if you have a virtual env ``virtualenv --version``
    2. (Not Installed) Dont see a version number? run ``sudo pip install virtualenv``
    3. (Installed) Make a folder within the highest file of the project ``mkdir ~/env``
    4. run ``virtualenv ~/env/my_new_app``
    5. cd into the bin folder ``cd ~/env/my_new_app/bin``
    6. activate the env ``source activate``

- ``pip install -r requirements.txt``

- Create a Postgres Database & connect it within the plotly_django_tutorial.py settings

- ``python manage.py makemigrations``

- ``python manage.py migrate``

- ``python manage.py runserver``
