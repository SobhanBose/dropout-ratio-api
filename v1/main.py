from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import orjson
import typing

class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return orjson.dumps(content)
    
cors_origins = [
    "*"
]

cors_methods = [
    "GET",
    "POST"
]
    
app = FastAPI(default_response_class=ORJSONResponse)
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_methods=cors_methods
)

from v1.home import router as home_router
from v1.getData import router as get_data_router

app.include_router(home_router.router, tags=["Home"])
app.include_router(get_data_router.router, tags=["Data"])