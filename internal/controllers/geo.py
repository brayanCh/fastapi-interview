from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError
from internal.dto.geo import GeoProcessRequest, GeoProcessResponse
from internal.services.geo import process_coordinates as process_coordinates_service
from Internal.controllers/example_responses import invalid_example, successful_example

router = APIRouter()


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
