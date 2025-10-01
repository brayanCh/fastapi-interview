from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError
from ..dto.geo import GeoProcessRequest, GeoProcessResponse
from ..services.geo import process_coordinates as process_coordinates_service

router = APIRouter()

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


@router.post(
    "/process",
    response_model=GeoProcessResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: successful_example,
        400: invalid_example
    }
)
async def process_coordinates(request: GeoProcessRequest) -> GeoProcessResponse:
    """
    handles the request with the coordinate list and returns the corresponding
    status code depending if everything goes well or if there's any error
    """
    try:
        result = process_coordinates_service(request.points)
        return result
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Validation error: {str(e)}"
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )
