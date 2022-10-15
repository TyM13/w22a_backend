# sent_data – This is going to be either request.args or request.json, depending on the endpoint
# expected_data – This is going to be the list of keys the endpoint requires to work
def check_endpoint_info(sent_data, expected_data):
    for data in expected_data:
        if(sent_data.get(data) == None):
# function will return a string in case of error, an None otherwise
            return f"The {data} parameter is required!"