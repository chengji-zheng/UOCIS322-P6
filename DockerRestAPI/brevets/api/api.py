from flask import Flask, render_template
from flask_restful import Resource, Api
import requests
import pandas

app = Flask(__name__)
api = Api(app)


class listAll(Resource):
    def csv_form(self):
        # Iterate through each line of ourdb
        for i in ourdb.find():
            d = pandas.read_json(i)
        return d.to_csv()
    
    def json_form(self):
        for i in in ourdb.find():
            return i
            
    def get(self, dataType):
        if dataType == "csv":
            return csv_form()
        return json_form()
        

class listOpenOnly(Resource):
    def csv_form(self):
        # Find by key name
        top_k = request.args.get("top", default=-1)
        if top_k == None:
            for i in ourdb.find({},{"open_time_field":1}):
                d = pandas.read_json(i)
            return d.to_csv()
        else:
            # Get the number x where comes with top=x
            num = top_k.value()
            for i in range(num):
                d = pandas.read_json(ourdb.find({},{"open_time_field":1}))
            return d.to_csv()
    
    def json_form(self):
        top_k = request.args.get("top", default=-1)
        #Checking the route see if it contains top=x or not
        if top_k == None:
            for i in ourdb.find({},{"open_time_field":1}):
            return i
        else:
            num = top_k.value()
            for i in range(num):
                ourdb.find({},{"open_time_field":1})
            
    def get(self, dataType):
        if dataType == "csv":
            return csv_form()
        return json_form()


# Handling close time, similar to the logic where used in handling open time
class listCloseOnly(Resource):
    def csv_form(self):
        # Find by key name
        top_k = request.args.get("top", default=-1)
        if top_k == None:
            for i in ourdb.find({},{"close_time_field":1}):
                d = pandas.read_json(i)
            return d.to_csv()
        else:
            # Get the number x where comes with top=x
            num = top_k.value()
            for i in range(num):
                d = pandas.read_json(ourdb.find({},{"close_time_field":1}))
            return d.to_csv()
    
    def json_form(self):
        top_k = request.args.get("top", default=-1)
        #Checking the route see if it contains top=x or not
        if top_k == None:
            for i in ourdb.find({},{"close_time_field":1}):
            return i
        else:
            num = top_k.value()
            for i in range(num):
                ourdb.find({},{"close_time_field":1})
            
    def get(self, dataType):
        if dataType == "csv":
            return csv_form()
        return json_form()




api.add_resource(listAll, '/listAll/<str:dataType>')
api.add_resource(listAll, '/listAll/csv/<str:dataType>')
api.add_resource(listAll, '/listAll/json/<str:dataType>')

api.add_resource(listOpenOnly, '/listOpenOnly/<str:dataType>')
api.add_resource(listOpenOnly, '/listOpenOnly/csv<str:dataType>')
api.add_resource(listOpenOnly, '/listOpenOnly/csv/<str:dataType>')
api.add_resource(listOpenOnly, '/listOpenOnly/json?top=/<str:dataType>')
api.add_resource(listOpenOnly, '/listOpenOnly/csv?top=/<str:dataType>')

api.add_resource(listCloseOnly, '/listCloseOnly/<str:dataType>')
api.add_resource(listCloseOnly, '/listCloseOnly/csv<str:dataType>')
api.add_resource(listCloseOnly, '/listCloseOnly/csv/<str:dataType>')
api.add_resource(listCloseOnly, '/listCloseOnly/json?top=/<str:dataType>')
api.add_resource(listCloseOnly, '/listCloseOnly/csv?top=/<str:dataType>')