## USAGE

run the docker image

```
docker build -t fastapi:local .
docker run -p 8000:8000 --name fastapi fastapi:local
```


## schema of the request body

`POST /geo/process`

```
{
  "points": [
    {
      "lat": <number>,
      "lng": <number>
    }
  ]
}
```

## schema of the response body

```
{
  "centroid": {
    "lat": <number>,
    "lng": <number>
  },
  "bounds": {
    "north": <number>,
    "south": <number>,
    "east": <number>,
    "west": <number>
  }
}
```

