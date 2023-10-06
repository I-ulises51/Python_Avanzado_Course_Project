from app.db.mongodb import MongoDB as mongo
import json
from bson import json_util

class Job_Roles(mongo):
    
    def __init__(self):
        print("Welcome to Job Roles")
        
        
    def get_all_job_roles(self):
        student_dict = self.find_all_job_roles()
        student_dict = self.convert_to_json(student_dict)
        
        return student_dict
    
    def convert_to_json(self,mongo_reponse):
        ##Dump loaded Binary to valid JSON string and reload it as dict
        mongo_dict = json.loads(json_util.dumps(mongo_reponse))
        
        return mongo_dict
        