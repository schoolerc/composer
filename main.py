from fastapi import FastAPI, Request
from starlette import status
from starlette.responses import JSONResponse

from errors import NotFoundError
from routers.songs import song_router

app = FastAPI()

app.include_router(song_router)

@app.exception_handler(NotFoundError)
def not_found(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"{exc.resource_type.__name__} [{exc.resource_id}] not found"}
    )