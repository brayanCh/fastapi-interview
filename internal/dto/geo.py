from typing import List
from pydantic import BaseModel, Field, field_validator


# Represents a single geographic coordinate point.
class CoordinatePoint(BaseModel):
    lat: float = Field(..., description="Latitude coordinate")
    lng: float = Field(..., description="Longitude coordinate")

    @field_validator('lat')
    @classmethod
    def validate_latitude(cls, v: float) -> float:
        if not isinstance(v, (int, float)):
            raise ValueError("Latitude must be a numeric value")
        if not -90 <= v <= 90:
            raise ValueError(f"Latitude must be between -90 and 90, got {v}")
        return v
    
    @field_validator('lng')
    @classmethod
    def validate_longitude(cls, v: float) -> float:
        if not isinstance(v, (int, float)):
            raise ValueError("Longitude must be a numeric value")
        if not -180 <= v <= 180:
            raise ValueError(f"Longitude must be between -180 and 180, got {v}")
        return v
    

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


# Response model for POST /geo/process endpoint
class GeoProcessResponse(BaseModel):
    centroid: Centroid = Field(..., description="Average center point of all coordinates")
    bounds: Bounds = Field(..., description="Bounding box containing all coordinates")


# Request model for POST /geo/process endpoint
class GeoProcessRequest(BaseModel):
    points: List[CoordinatePoint] = Field(
        ..., 
        min_length=1,
        description="List of coordinate points to process"
    )
    
    @field_validator('points')
    @classmethod
    def validate_points_not_empty(cls, v: List[CoordinatePoint]) -> List[CoordinatePoint]:
        """Ensure points list is not empty."""
        if not v:
            raise ValueError("Points array cannot be empty")
        return v
