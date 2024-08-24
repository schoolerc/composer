from fastapi import FastAPI, Request
from starlette import status
from starlette.responses import JSONResponse

from errors import NotFoundError

app = FastAPI()


@app.exception_handler(NotFoundError)
def not_found(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"{exc.type.__name__} [{exc.id}] not found"}
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
