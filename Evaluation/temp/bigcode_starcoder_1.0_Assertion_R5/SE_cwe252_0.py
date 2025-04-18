import json
def parse(data):
    '''
    Parse the data by splitting it by comma.
    Return the parsed data or None if data = none.
    @param data: The string to parse.
    @return: A list of strings.
    '''
    if data is None:
        return None
    return data.split(',')

def total_names(str_json: str):
    '''
    Get the list of names from the json_data.
    Parse it by invoking the parse() method.
    @param str_json: A dictionary serialized into json to be parsed.
    @return: the number of names in the json_data dictionary.
    '''
#  Check if str_json is a valid python string, if not, return 0.
    if not isinstance(str_json, str):
        return 0
    
#  Check if str_json is a valid json string, if not, return 0.
    try:
        json.loads(str_json)
    except:
        return 0

#  Convert from json to python dict.
    my_dict = json.loads(str_json)

#  Check if my_dict is a dict, if not return 