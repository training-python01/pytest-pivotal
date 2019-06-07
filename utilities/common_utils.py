import json
import os

from jsonschema import validate
from jsonschema import ValidationError


def validate_data(actual_result, expected_result):
    print("Actual Result: ", actual_result)
    print("Expected Result: ", expected_result)
    for key in expected_result:
        if actual_result[key] != expected_result[key]:
            raise AssertionError(
                "Failed data validation - Actual result:{}, expected_result: {}".format(actual_result[key],
                                                                                        expected_result[key]))
    return True


def schema_validation(json_schema_name, instance):
    schema = load_schema(json_schema_name)
    try:
        validate(instance=instance, schema=schema)
        return True
    except:
        raise ValidationError("It was validation error with schema")


def load_schema(json_schema_name):
    current_path = os.getcwd()
    path = "{}/json_schema/{}".format(current_path, json_schema_name)
    with open(path) as json_schema:
        schema = json.load(json_schema)
    return schema
