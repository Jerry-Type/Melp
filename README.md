# Melp RESTful API

This API provides useful information about some restaurants :notebook_with_decorative_cover: .

## Install guide


##### Clone this repo

```bash
$ git clone https://github.com/Jerry-Type/Melp.git
$ cd Melp
```

##### Creates the virtualenv in the Melp directory
```bash
$ python3 -m venv env
```

##### Activate the virtual environment
```bash
$ source env/bin/activate
```

##### Install the dependencies
```bash
$ pip3 install -r requirements.txt
```

##### Configure the DB
```bash
$ pip3 migrate.py db init
$ pip3 migrate.py db migrate
$ pip3 migrate.py db upgrade
```

##### Execute the App
```bash
$ pip3 run.py
```

## Deploy on Heroku
The API deploy can be found at [link](https://app-melp.herokuapp.com/) 

## Test
In the following [link](https://documenter.getpostman.com/view/5474037/RWgjY1vT) you can find a Postman collection to test the API.


