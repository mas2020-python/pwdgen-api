"""
Main module for the Web API Server application.
"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from errors import RequestException
from password_gen import PwdGenerator
from utils import config

app = FastAPI()


@app.exception_handler(RequestException)
async def request_exception_handler(request: Request, exc: RequestException):
    return JSONResponse(
        status_code=400,
        content={
            "apiVersion": "v1.0.0",
            "error": {
                "code": 400,
                "message": exc.message,
            }
        }
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={
            "apiVersion": "v1.0.0",
            "error": {
                "code": 400,
                "message": str(exc),
            }
        })


@app.post("/passwords")
async def gen_password(length: int | None = None, numbers: bool | None = None,
                       lowercase: bool | None = None, uppercase: bool | None = None, special: bool | None = None):
    """
    The API function for generating the password

    Returns
    -------
    info: dict
      the JSON object that contains the pwd in the message field.
    """
    try:
        gen = PwdGenerator()
        # default values in case are not given
        length = length if length != None else config.app_config["password_config"]["default_length"]
        numbers_flag = numbers if numbers != None else config.app_config[
            "password_config"]["default_params"]["numbers_flag"]
        lowercase_flag = lowercase if lowercase != None else config.app_config[
            "password_config"]["default_params"]["lowercase_flag"]
        uppercase_flag = uppercase if uppercase != None else config.app_config[
            "password_config"]["default_params"]["uppercase_flag"]
        special_flag = special if special != None else config.app_config[
            "password_config"]["default_params"]["special_flag"]
        pwd = gen.generate(length, numbers_flag, lowercase_flag,
                           uppercase_flag, special_flag)
    except Exception as ex:
        raise RequestException(ex.__str__())
    return {"message": pwd}
