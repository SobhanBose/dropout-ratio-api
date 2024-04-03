from fastapi import FastAPI
from fastapi.responses import JSONResponse
import orjson
import typing

class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return orjson.dumps(content)
    
app = FastAPI(default_response_class=ORJSONResponse)

from v1.home import router as home_router
from v1.getData import router as get_data_router

app.include_router(home_router.router, tags=["Home"])
app.include_router(get_data_router.router, tags=["Data"])