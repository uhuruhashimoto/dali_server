# DALI Challenge 23F
Backend Challenge - Social Media Webserver
Challenge may be found [here](https://dalilab.notion.site/Social-Media-Challenge-72a37c4d33d44de194e66253e7efe7a0)

This is a RESTful web server built in Express, using an SQLite db to store data. [Tutorial used](https://www.youtube.com/watch?v=GMppyAPbLYk)

## Endpoints
- "/dalimember"
    - The core endpoint is "/dalimember". This will return a list of all the members in the db.
- "/dalimember/[id]"
    - POST and GET endpoints are supported by numeric ID.
- "/dalimember/[full_name]"
    - This returns info on a single DALI member.
- "/dalimember/search/[search_field]/[search_criteria]"
    - First/last name wildcard search
        - First name: "/dalimember/search/firstname/[name]"
        - Last name: "/dalimember/search/lastname/[lastname]"
    - Year search
        - "/dalimember/search/year/[year]"
    - des/dev/pm/core/mentor search
        - "/dalimember/search/[des/dev/pm/core/mentor]/[True/true/1/False/false/0]"
- Union
    - "/dalimember/union/[group1]/[True/true/1/False/false/0]/[group2]/[True/true/1/False/false/0]"
- Intersection
    - "/dalimember/intersection/[group1]/[True/true/1/False/false/0]/[group2]/[True/true/1/False/false/0]"

## Database Creation
To create database, the following lines were used before the server was made stateless:
```python
with app.app_context():
    db.create_all()
```

Then `python load_db.py` was used to load the database from "dali_social_media.json"

## Install
`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

## Run
`flask run`

Navigate in browser to "http://127.0.0.1:5000/dalimember"

## Update
`pip freeze > requirements.txt`

## Clean
`deactivate`