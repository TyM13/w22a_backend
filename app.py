from apihelper import check_endpoint_info
import dbhelper
from flask import Flask, request, make_response
import json
import dbcreds


app = Flask(__name__)
# get request for the api /api/candy
@app.get('/api/candy')
def get_all_candy():
# runs the run_statment from dbhelper, calls the procedure show_candy.
    results = dbhelper.run_statment('CALL show_candy')
# checks to see if all items are == to a list
    if(type(results) == list):
# takes results and puts it in the format of json and if it can't convert, it will default to a string.
# if the make_respone fails it will send the error code 201 else it will return error code 500
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)

#-----------------------------------------------------------------------#


@app.post('/api/candy')
def post_candy():
#checks the endpoint for json and stores info as variable invalid, if invalid is not equal to none it will return an error
    invalid = check_endpoint_info(request.json, ['candy_name', 'candy_image', 'candy_description'])
    if(invalid != None):
        return make_response(json.dumps(invalid, default=str), 400)

# calls the procedure insert_candy and takes in 3 arguements from the user, candy_name and candy_image candy_description
    results = dbhelper.run_statment('CALL insert_candy(?,?,?)',
    [request.json.get('candy_name'), request.json.get('candy_image'), request.json.get('candy_description')])
# checks to see if all items are == to a list
    if(type(results) == list):
# takes results and puts it in the format of json and if it can't convert, it will default to a string.
# if the make_respone fails it will send the error code 201 else it will return error code 500
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


#-----------------------------------------------------------------------#


@app.delete('/api/candy')
def delete_candy():
# checks the endpoint for json and stores info as variable invalid, if invalid is not equal to none it will return an error
    invalid = check_endpoint_info(request.json, ['candy_id'])
    if(invalid != None):
        return make_response(json.dumps(invalid, default=str), 400)

# calls the procedure delete_candy and takes in 1 arguement from the user, candy_id
    results = dbhelper.run_statment('CALL delete_candy(?)',
     [request.json.get('candy_id')])
# checks to see if all items are == to a list
    if(type(results) == list):
# takes results and puts it in the format of json and if it can't convert, it will default to a string.
# if the make_respone fails it will send the error code 201 else it will return error code 500
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


#-----------------------------------------------------------------------#



if(dbcreds.production_mode == True):
    print("Running in Production Mode")
    import bjoern # type: ignore
    bjoern.run(app, "0.0.0.0", 5000)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode!")
    app.run(debug=True)