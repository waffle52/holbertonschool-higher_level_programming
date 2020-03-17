#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """ func to """
    return json.dumps(my_obj, sort_keys=True)
