# example response for a 200 status code
successful_example={
    "description": "Successfully processed coordinates",
    "content": {
        "application/json": {
            "example": {
                "centroid": {"lat": 37.3825, "lng": -96.1248},
                "bounds": {
                    "north": 40.7128,
                    "south": 34.0522,
                    "east": -74.0060,
                    "west": -118.2437
                }
            }
        }
    }
}

# example response for a 400 status code (bad request)
invalid_example={
    "description": "Bad Request - Invalid input data",
    "content": {
        "application/json": {
            "examples": {
                "missing_points": {
                    "summary": "Missing points field",
                    "value": {"error": "Field 'points' is required"}
                },
                "empty_array": {
                    "summary": "Empty points array",
                    "value": {"error": "Points array cannot be empty"}
                },
                "invalid_coordinates": {
                    "summary": "Invalid lat/lng values",
                    "value": {"error": "Latitude must be a numeric value"}
                }
            }
        }
    }
}
