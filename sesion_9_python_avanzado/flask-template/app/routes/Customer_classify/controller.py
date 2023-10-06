from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.Customer_classify.Customer_classify import Customer_classify

Customer_classify_blueprint = Blueprint("Customer_classify", 
                                        __name__, url_prefix="/Customer_classify")


@Customer_classify_blueprint.route("/Classifier/<file_name>", methods=["GET", "POST"])
def customer_classify_csv(file_name):
    print("Inside Controller Customer Classify")
    obj_ocr = Customer_classify()
    obj_ocr.svm_classifier(file_name)
    return "CSV to classify: " + str(file_name)
