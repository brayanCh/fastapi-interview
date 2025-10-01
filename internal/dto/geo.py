from typing import List
from pydantic import BaseModel, Field, field_validator


# Represents a single geographic coordinate point.
class CoordinatePoint(BaseModel):
    lat: float = Field(..., description="Latitude coordinate")
    lng: float = Field(..., description="Longitude coordinate")
    

# Represents the centroid of a set of coordinates.
class Centroid(BaseModel):
    lat: float = Field(..., description="Centroid latitude")
    lng: float = Field(..., description="Centroid longitude")


# Represents the bounding box of a set of coordinates.
class Bounds(BaseModel):
    north: float = Field(..., description="Maximum latitude (northernmost point)")
    south: float = Field(..., description="Minimum latitude (southernmost point)")
    east: float = Field(..., description="Maximum longitude (easternmost point)")
    west: float = Field(..., description="Minimum longitude (westernmost point)")


# Response model for geo-processing operations.
class GeoProcessResponse(BaseModel):
    centroid: Centroid = Field(..., description="Average center point of all coordinates")
    bounds: Bounds = Field(..., description="Bounding box containing all coordinates")
