# Schema Validation in Python using jsonschema
# Schema validation is the process of verifying that a data structure (e.g., an API response)
# conforms to a predefined structure and data types — called a "schema".
# This is especially useful in API testing to ensure responses match the expected contract.
#
# The `jsonschema` library allows you to define a schema using JSON Schema standard and
# validate any Python dict (typically parsed JSON) against it.
#
# Key concepts:
#   - "type"       : specifies the expected data type (object, string, integer, array, etc.)
#   - "properties" : defines the expected fields and their types inside an object
#   - "required"   : lists fields that MUST be present in the data
#
# If validation passes → no exception is raised
# If validation fails  → a ValidationError is raised with details of what went wrong

from jsonschema import validate

# Define the expected schema
expected_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "author": {"type": "string"},
        "published_year": {"type": "integer"}
    },
    "required": ["id", "title", "author", "published_year"]
}

# Simulate an API response
api_response = {
    "id": 1,
    "title": "Sample Book",
    "author": "John Doe",
    "published_year": 2022
}

# Validate the API response against the expected schema
try:
    validate(instance=api_response, schema=expected_schema)
    print("API response is valid according to the schema.")
except Exception as e:
    print(f"API response is not valid: {e}")