from flask import Blueprint, jsonify
from app.services.job_roles.employees import Job_Roles as Job_Roles

roles_blueprint = Blueprint('users', __name__)

@roles_blueprint.route('/roles', methods=["GET", "POST"])
def get_all_roles():
    obj_roles = Job_Roles()
    roles_response = obj_roles.get_all_job_roles()
    
    return roles_response