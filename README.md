# Pizzeria project

### Pizzeria project is created to solve business needs and realize online sales. The project has a function of user authorization, adding goods to cart and its payment using Stripe service. The site administrator can add, delete and edit products. To interact with Stripe service, its API key and product ID are used.
### If desired, the theme of the site can be changed thanks to built-in templates and scaled thanks to PostgreSQL database.


## Technology

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
4. Install packages:

     1. Go to pizzeria app: ```cd pizzeria```
   
     2. Install requirements.txt: ``` pip install -r requirements.txt ```
  
5. Create a ```.env``` file in the root directory of the project with the following content:
```
STRIPE_PUBLIC_KEY=pk_test_51NW4KMC55Xf8DWWegIk3sL1xVMjGddmR7lUyvtsd7La6TG13BHhdr6d69L8W4UreYfULseQ0q1LIi8mKhCGNEK9i00nXSzW3F8
STRIPE_SECRET_KEY=sk_test_51NW4KMC55Xf8DWWelMYwfegyfiPp7XOfBHSm3bEnE60XTf59IHiaGFGGrVYH4b7zHGJZM7Rpsz96C0BtimeKJtq500M1CbL8kX

success_url=http://127.0.0.1:8000/success/
cancel_url=http://127.0.0.1:8000/cancel/

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=pizza
SQL_USER=postgres
SQL_PASSWORD=test
SQL_HOST=localhost
SQL_PORT=5432
 ```
4. Run server: ```python manage.py runserver```




