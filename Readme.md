# Capstone Project for the Meta Back-end Professional Certificate
This is the final project for the Meta-Back Professional Certificate, where we will show all the skills acquired through the certificate to create a final, comprehensive website for the Little Lemon restaurant using django.

# How to Setup your Testing Environment:
1. Install the virtual environment: `pip install virtualenv` (if necessary for the 1st time) and `python -m venv env-name` (*Replace with the name of your environment).

2. Move to the folder where you created the virtual environment, and use proceed to activate it: `.\Scripts\activate`

3. Once the virtual environment is activated, install Django using: `pip install django`. 

4. Install the remaining dependencies for this project: 
- `pip install djoser`
- `pip install djangorestframework`

5. Move to the littlelemon project folder and set up the MySQL database.

# How to Setup the MySQL Database:

### 1. MySQL Dependencies:
- Make sure you already have installed a MySQL server and the necessary credentials. Otherwise, download the server from https://dev.mysql.com/downloads/mysql/ and follow the instructions for the installation.

- Once you have the server and created your own credentials, use `pip install mysqlclient` to finish installing the dependencies.

### 2. Create MySQL Database:
- Login into the database client using your own credentials. If using a regular terminal instead of the client, you can type: `mysql -u your_name -p`, and then type your password to enter.

- Create the database that you will use for the project, and select it so that it can be used: `CREATE DATABASE your_database;` and `USE your_database`.

### 3. Final Steps
- You may need to login into MySQL as the root user first and use it to grant privileges to other users (assuming you don't want to use the root user). To do so, type this command as the root user in MySQL: `grant all privileges on mydb.* to myuser@'%' identified by 'mypasswd'`;

- Also, remember to include the nessesary information about your local MySQL databases in the project's `settings.py` file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon', # <-- update
        'HOST': '127.0.0.1',
        'PORT': '3306',        # <-- update
        'USER': 'root',        # <-- update
        'PASSWORD': '',        # <-- update
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

- Lasly... Start Testing! Proceed to run the usual commands and check that everything works as intended:
- `python manage.py createsuperuser`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver` 

# Static Content

The address for serving the rendered static content is `127.0.0.1:8000/restaurant/`.  Static assests are referenced and rendered through the template page `index.html`.

# Unit Testing

There are only two unit tests in this project.  They can be run using the following command: `python manage.py test tests\`.

# API Endpoints
Endpoints that require an authentication token have been indicated in the table below.

| Endpoint | Method | Token Required | Client Payload |  |
| --- | --- | --- | --- | --- |
| _user creation and authentication_ |  |  |  |  |
| `/auth/users/` | POST | --- | `username`, `email`, `password` |  |
| `/auth/token/login/` | POST | --- | `username`, `password` |  |
| _menu items_ |  |  |  |  |
| `/api/menu-items/` | POST | yes | `title`, `price`, `inventory` |  |
| `/api/menu-items/` | GET | yes | --- |  |
| `/api/menu-items/<int:pk>` | GET | yes | --- |  |
| `/api/menu-items/<int:pk>` | PUT, PATCH | yes | `title`, `price`, `inventory` |  |
| `/api/menu-items/<int:pk>` | DELETE | yes | --- |  |
| _booking_ |  |  |  |  |
| `/restaurant/bookings/tables/` | GET | yes | --- |  |
| `/restaurant/bookings/tables/` | POST | yes | `name`, `no_of_guests`, `booking_date` |  |
| _user creation and authentication` |  |  |  |  |
| `/auth/token/logout/` | GET | yes | --- |