"""
    # Created on September 20, 2022, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

# Libraries dependencies
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from starlette.middleware.base import _StreamingResponse

# Project dependencies
from config import MS_NAME
from exceptions.internal_server_exception import (
    InternalServerException,
    InternalServerExceptionModel,
)
from exceptions.validation_exception import (
    ValidationExceptionModel,
    ValidationException,
)
from logs import logger
from repositories.database.manager.database_middleware import DatabaseMiddleware
from routers.router_v1 import router as router_v1
from routers.health_v1 import router as health_router

CLASS = "Lambda Handler"

app = FastAPI()
app.include_router(router_v1, prefix="/mcs/metadata/v1")
app.include_router(health_router, prefix="/mcs/metadata")

app.add_middleware(DatabaseMiddleware)


@app.middleware("http")
async def lambda_middleware(request: Request, call_next) -> JSONResponse | Response:
    """
    Middleware to log responses, requests and manage exception
    """
    log_request(request)

    try:
        response = await call_next(request)
    except Exception:
        logger.exception(f"[{MS_NAME}][{CLASS}] Internal server error: ")
        status_code = InternalServerException.status_code
        content = InternalServerExceptionModel().model_dump()
        response = JSONResponse(status_code=status_code, content=content)
    logged_response = await log_response(response)
    return logged_response


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Modify HTTPException behaviour

    By default, FastAPI HTTPException returns has a body with the structure {'detail': {content}}
    this code handle all HTTPException to modify the body to structure {content}
    """

    return JSONResponse(status_code=exc.status_code, content=exc.detail)


@app.exception_handler(RequestValidationError)
async def request_exception_handler(request: Request, exc: RequestValidationError):
    """
    Modify RequestValidationError behaviour

    This function handle Pydantic validation exceptions and returns a 422 response with the proper content.
    """
    return JSONResponse(
        status_code=ValidationException.status_code,
        content=ValidationExceptionModel(errors=list(exc.errors())).model_dump(
            exclude_none=True
        ),
    )


def log_request(request: Request):
    """
    Log Request

    Code valid to show logs from AWS from Lambdas or from local executions
    """
    event = (
        request.scope["aws.event"] if request.scope.get("aws.event") else request.scope
    )
    logger.info(f"[{MS_NAME}][{CLASS}] Request received: {event}")


async def log_response(
    response: _StreamingResponse | JSONResponse,
) -> Response | JSONResponse:
    """
    Log Response returned
    """
    if isinstance(response, _StreamingResponse):
        response_body_bin = b""
        async for chunk in response.body_iterator:
            response_body_bin += chunk  # type:ignore
        response_body = response_body_bin.decode()
        # StreamingResponse must not be converted to JSONResponse
        response = Response(
            content=response_body_bin,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type,
        )  # type:ignore
        logger.info(
            f"[{MS_NAME}][{CLASS}] Response returned: {{'status_code': {response.status_code}, "
            f"'body': {response_body}, 'headers': {response.headers}}}"
        )
        return response
    logger.info(
        f"[{MS_NAME}][{CLASS}] Response returned: {{'status_code': {response.status_code}, "
        f"'body': {response.body.decode()}, 'headers': {response.headers}}}"  # type:ignore
    )
    return response
