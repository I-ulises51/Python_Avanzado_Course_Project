from flask import Flask
from flask_cors import CORS
from app.routes.ocr.controller import ocr_blueprint as ocr_class
from app.routes.status.controller import status_blueprint
from app.routes.Customer_classify.controller import Customer_classify_blueprint
from app.routes.job_roles.controller import roles_blueprint 
from dotenv import dotenv_values,load_dotenv

app = Flask(__name__)
CORS(app)

app.register_blueprint(ocr_class)
app.register_blueprint(status_blueprint)
app.register_blueprint(roles_blueprint)
app.register_blueprint(Customer_classify_blueprint)

#declarar variable de entorno
ENV = dotenv_values(".env")
load_dotenv(override=False)
#print("Env: ",ENV)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return "Hello the Service is Working - Irving"
