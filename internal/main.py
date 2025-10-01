from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .controllers.geo import router as geo_router
import uvicorn

app = FastAPI()

app.include_router(geo_router, prefix="/geo", tags=["geo"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler for consistent error responses."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
