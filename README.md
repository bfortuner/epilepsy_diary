## Hapi Bot API

Python API for handling user requests from Hapi Facebook Messenger Bot


### Key Links

HapiBot Facebook Page: [View Page](https://www.facebook.com/hapibot)
Message HapiBot: [Message Me](http://l.facebook.com/l.php?u=http%3A%2F%2Fm.me%2Fhapibot&h=1AQFFtodm)
Frontend Repo: [Github](https://github.com/bfortuner/hapibot)
Hapi FB Developer Page: [Developers](https://developers.facebook.com/apps/1062967727132759/dashboard)


### Setup

Clone github repository:

```
$ git clone https://github.com/bfortuner/epilepsy_diary.git
```

Setup virtualenv:
```
$ sudo easy_install pip
$ sudo pip install virtualenv
$ virtualenv epilepsyenv
$ . epilepsyenv/bin/activate
```

Now install the required modules:
```
$ cd epilepsy_diary
$ pip install -r requirements.txt
```

Create required ENV variables (add to ~/.bash_profile or ~/.zshrc)
```
export EPILEPSY_APP_SECRET_KEY=''
export EPILEPSY_CONFIG='TestConfig'
export EPILEPSY_DATABASE_URI=''
export EPILEPSY_FB_VERIFICATION_TOKEN=''
export EPILEPSY_FB_PAGE_ACCESS_TOKEN=''
export EPILEPSY_PLOTLY_USERNAME=''
export EPILEPSY_PLOTLY_PASSWORD=''
export EPILEPSY_CLIENT_AUTH_KEY=''
```
*Email admins for keys

Create or Reset the Shared Devo Database
```
$ python create_db.py
```

Now you can launch the app:
```
$ python application.py
```
And point your browser to http://0.0.0.0:5000


### Deployment

Deploy to Heroku:
```
$ git add --all
$ git commit -m 'My Commit Message'
$ git push heroku master
```

Helpful Heroku Commands
```
$ git push -f heroku master  #Override everything in the Heroku Repo with your local changes
$ git push heroku mydevbranch:master  #Deploy your development branch changes to Heroku
$ heroku run bash  #ssh into dyno
$ heroku pg:psql --app hapibackend DATABASE  #login to postgres db
```


### Other Commands

```
ngrok http 8000  # Host the Node Frontend locally (update the FB developer page webhook)
```

