from logging import getLogger
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def register_exception_handler(app: FastAPI):
    """"Register exception handler for FastAPI app."""
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ):
        exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
        getLogger(__name__).error(request, exc_str)
        content = {'status_code': 422, 'message': exc_str, 'data': None}
        return JSONResponse(
            content=content,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )
