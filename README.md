# Flask SQLAlchemy template
**Getting started** <br>
Clone project by the following 

```
git clone git@github.com:Micheledebruyn/flask-sqlalchemy-template.git
```

After cloning initialize venv by running
```
python3 -m venv venv
```

To **activate** this environment run:
```
source venv/bin/activate
```

After this there is a local environment running.


With this environment ready you can run all the packages to install with the following:
```
pip3 install -r requirements.txt
```

This will install all the necessary packages in this project. You can view them in requirements.txt

**Get Flask started** <br>
To get the Flask server up and running run the following commands:
```
export FLASK_APP=run.py    #this file could be named differently, in this project it's run.py
export FLASK_ENV=development
```

**Database connection**  <br>
In `config.py` add the correct postgresql url which should be formatted like this:
```
postgresql://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DATABASE>
```

**Finalize**  <br>
In `app/__init__.py` add your own url_prefix. In the case of building an api it could potentially be `/api/v1`

Then the last thing to do is to run:
```
flask run
```

And go visit `http://localhost:5000` !
