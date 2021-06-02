from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
from pymongo import MongoClient
import os
import logging # Debug using


app = Flask(__name__)
client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
ourdb =  client.tododb

api = Api(app)


class listAll(Resource):
    def csv_form(self):
        output = ""
        # The first line
        data = list(ourdb.tododb.find({},{"_id":0, "open_time_field":1, "close_time_field":1}))
        firstline = list(data[0].keys())
        output = ",".join(firstline)
        output += "\n"
        #Rest of lines
        for d in data:
            output += ",".join(list(d.values()))
            output += "\n"
        return output
    
    def json_form(self):
        return list(ourdb.tododb.find({},{"_id":0, "open_time_field":1, "close_time_field":1}))
   
    def get(self, dataType="json"):
        if dataType == "csv":
            return self.csv_form()
        return self.json_form()
        

class listOpenOnly(Resource):
    
    def csv_form(self, qty):
        temp = []
        output = ""
        # The first line
        data = list(ourdb.tododb.find({},{"_id":0, "open_time_field":1}))
        firstline = list(data[0].keys())
        output = ",".join(firstline)
        output += "\n"

        #Rest of lines
        if qty > 0 and qty <= len(data):
            for i in range(qty):
                temp.append(dict(data[i]))
            for d in temp:
                output += ",".join(list(d.values()))
                output += "\n"
        else:
            temp = data
            for d in temp:
                output += ",".join(list(d.values()))
                output += "\n"

        return output
    
    def json_form(self, qty):
        temp = []
        data = list(ourdb.tododb.find({},{"_id":0, "open_time_field":1}))
        if qty > 0 and qty <= len(data):
            for i in range(qty):
                temp.append(dict(data[i]))
        else:
            temp = data
        return temp
            
    def get(self, dataType="json"):
        qty = int(request.args.get("top", default=0, type=int))
        if dataType == "csv":
            return self.csv_form(qty)
        return self.json_form(qty)


# Handling close time, similar to the logic where used in handling open time
class listCloseOnly(Resource):

    def csv_form(self, qty):
        temp = []
        output = ""
        # The first line
        data = list(ourdb.tododb.find({},{"_id":0, "close_time_field":1}))
        firstline = list(data[0].keys())
        output = ",".join(firstline)
        output += "\n"

        #Rest of lines
        if qty > 0 and qty <= len(data):
            for i in range(qty):
                temp.append(dict(data[i]))
            for d in temp:
                output += ",".join(list(d.values()))
                output += "\n"
        else:
            temp = data
            for d in temp:
                output += ",".join(list(d.values()))
                output += "\n"
        return output
    
    def json_form(self, qty):
        temp = []
        data = list(ourdb.tododb.find({},{"_id":0, "close_time_field":1}))
        if qty > 0 and qty <= len(data):
            for i in range(qty):
                temp.append(dict(data[i]))
        else:
            temp = data
        return temp
            
    def get(self, dataType="json"):
        qty = int(request.args.get("top", default=0, type=int))
        if dataType == "csv":
            return self.csv_form(qty)
        return self.json_form(qty)




api.add_resource(listAll, '/listAll', '/listAll/<string:dataType>')
# api.add_resource(listAll, '/listAll/<str:dataType>')

api.add_resource(listOpenOnly, '/listOpenOnly', '/listOpenOnly/<string:dataType>')
# api.add_resource(listOpenOnly, '/listOpenOnly/<str:dataType>')

api.add_resource(listCloseOnly, '/listCloseOnly', '/listCloseOnly/<string:dataType>')
# api.add_resource(listCloseOnly, '/listCloseOnly/<str:dataType>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)