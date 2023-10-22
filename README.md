# DALI Challenge 23F
Backend Challenge - Social Media Webserver
Challenge may be found [here](https://dalilab.notion.site/Social-Media-Challenge-72a37c4d33d44de194e66253e7efe7a0)

This is a web server built in Express. [Tutorial used](https://www.youtube.com/watch?v=GMppyAPbLYk)

Note: to create database, the following lines were used before the server was made stateless:
```python
with app.app_context():
    db.create_all()
```

## Install
`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

## Run
`python main.py`

## Update
`pip freeze > requirements.txt`

## Clean
`deactivate`