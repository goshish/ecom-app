# Pizzeria project

### Pizzeria project is created to solve business needs and realize online sales. The project has a function of user authorization, adding goods to cart and its payment using Stripe service. The site administrator can add, delete and edit products. To interact with Stripe service, its API key and product ID are used.
### If desired, the theme of the site can be changed thanks to built-in templates and scaled thanks to PostgreSQL database.


## Stack

* Django
* PostgreSQL
* GIT
* HTML
* CSS

## Instalation

1. Install Python on your device (Python 3.11.1)
2. Clone repository:  ```git clone https://github.com/goshish/pizzeria.git ```
3. To create a virtual environment, navigate to your project directory and execute:
   ``` python -m venv venv ```
4. Activate your 
```venv\Scripts\activate.bat```- for Windows;
```source venv/bin/activate```- for Linux and MacOS.
5. Install packages:

     1. Go to pizzeria app: ```cd pizzeria```
   
     2. Install requirements.txt: ``` pip install -r requirements.txt ```
  
6. Create a ```.env``` file in the root directory of the project with the following content:
```
STRIPE_PUBLIC_KEY=your_public_key
STRIPE_SECRET_KEY=your_secret_key

success_url=your_success_url
cancel_url=your_cancel_url

SQL_ENGINE=your_db_engine
SQL_DATABASE=your_db_name
SQL_USER=your_db_user
SQL_PASSWORD=your_db_password
SQL_HOST=your_host
SQL_PORT=your_port
 ```
7. Make migrations
   ```python manage.py makemigrations```
   ```python manage.py migrate```
10. Run server: ```python manage.py runserver```




