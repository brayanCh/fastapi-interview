from typing import List
from internal.dto.geo import (
    CoordinatePoint,
    GeoProcessResponse,
    Centroid,
    Bounds
)


# Process a list of coordinate points to calculate centroid and bounds.
def process_coordinates(points: List[CoordinatePoint]) -> GeoProcessResponse:
    # validate the input(AKA not empty or null arguments)
    if not points or len(points) == 0:
        raise ValueError("Points list cannot be empty")
    
    # Extract all latitudes and longitudes
    latitudes = [point.lat for point in points]
    longitudes = [point.lng for point in points]
    
    # average both the latitude and longitudes lists to 
    # get the values for the centroid
    centroid_lat = sum(latitudes) / len(latitudes)
    centroid_lng = sum(longitudes) / len(longitudes)
    
    # Calculate bounds
    north = max(latitudes)
    south = min(latitudes)
    east = max(longitudes)
    west = min(longitudes)
    
    return GeoProcessResponse(
        centroid=Centroid(lat=centroid_lat, lng=centroid_lng),
        bounds=Bounds(north=north, south=south, east=east, west=west)
    )
