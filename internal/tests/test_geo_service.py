import pytest
from internal.services.geo import process_coordinates
from internal.dto.geo import CoordinatePoint

class TestGeoService:
    
    def test_process_single_point(self):
        points = [CoordinatePoint(lat=40.7128, lng=-74.0060)]
        
        result = process_coordinates(points)
        
        assert result.centroid.lat == 40.7128
        assert result.centroid.lng == -74.0060
        
        assert result.bounds.north == 40.7128
        assert result.bounds.south == 40.7128
        assert result.bounds.east == -74.0060
        assert result.bounds.west == -74.0060
    
    def test_process_multiple_points(self):
        points = [
            CoordinatePoint(lat=0.0, lng=0.0),
            CoordinatePoint(lat=10.0, lng=10.0),
            CoordinatePoint(lat=20.0, lng=20.0),
            CoordinatePoint(lat=30.0, lng=30.0)
        ]
        
        result = process_coordinates(points)
        
        assert result.centroid.lat == 15.0
        assert result.centroid.lng == 15.0
        
        assert result.bounds.north == 30.0
        assert result.bounds.south == 0.0
        assert result.bounds.east == 30.0
        assert result.bounds.west == 0.0
    
    def test_process_negative_coordinates(self):
        points = [
            CoordinatePoint(lat=-33.8688, lng=151.2093),
            CoordinatePoint(lat=-34.6037, lng=-58.3816),
        ]
        
        result = process_coordinates(points)
        
        assert result.centroid.lat == pytest.approx(-34.2362, rel=1e-3)
        assert result.centroid.lng == pytest.approx(46.4138, rel=1e-3)
        
        assert result.bounds.north == -33.8688
        assert result.bounds.south == -34.6037
        assert result.bounds.east == 151.2093
        assert result.bounds.west == -58.3816
    
    def test_process_coordinates_empty_list_raises_error(self):
        with pytest.raises(ValueError, match="Points list cannot be empty"):
            process_coordinates([])
    
    def test_process_coordinates_at_boundaries(self):
        points = [
            CoordinatePoint(lat=90.0, lng=180.0),
            CoordinatePoint(lat=-90.0, lng=-180.0),
        ]
        
        result = process_coordinates(points)
        
        assert result.centroid.lat == 0.0
        assert result.centroid.lng == 0.0
        
        assert result.bounds.north == 90.0
        assert result.bounds.south == -90.0
        assert result.bounds.east == 180.0
        assert result.bounds.west == -180.0
