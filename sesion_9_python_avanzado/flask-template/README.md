# Flask-API-Template - with Customer Classify

API template made with Flask for reusable assets

Before running the application, please install the requirements using this command:

`pip install -r requirements.txt`

Add a .env file with the following environment variables[^note]:

```
OUTPUT_RESULTS_PATH=
FILES_INPUT_PATH=
ENVIRONMENT=
GENERAL_PATH=
MONGO_CONNECTION=
```

Run the server with:

`sh gunicorn.sh`

The application will be listening on port 5001

The available routes are:

[/](http://0.0.0.0:5001) -> It returns a welcome message <br />
[/users](http://0.0.0.0:5001/status) -> It returns a list of dummy users <br />
[/ocr](http://0.0.0.0:5001/Customer_classify/Classifier/<file_name>) -> file used: marketing_campaign <br />


Customer Classify Changes: 

  - ./app/routes/Customer_classify
  - ./app/services/Customer_classify
  - ./app/__init__.py

For stopping the server, please press **Ctrl** + **C**

[^note]: Fill with the credentials of your Cloudant instance and put the name of the database you want to try in `CLOUDANT_DB` variable
