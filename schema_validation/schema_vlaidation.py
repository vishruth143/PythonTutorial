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