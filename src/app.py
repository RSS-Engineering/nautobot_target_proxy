# Third Party
import requests
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

# First Party
from helpers.graphql import query_nautobot_graphql
from helpers.queries import OOB_TARGET_QUERY

app = FastAPI()


@app.exception_handler(Exception)
async def validation_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": f" Exception message is {exc!r}."},
    )


@app.get("/targets")
def get_targets():
    response = query_nautobot_graphql(OOB_TARGET_QUERY).json()
    res = []
    for interface in response["data"]["interfaces"]:
        for device in interface["ip_addresses"]:
            res.append(
                {
                    "targets": [device["host"]],
                    "labels": {
                        "name": interface["device"]["name"],
                        "core_id": interface["device"]["cf_core_number"],
                        "location": interface["device"]["location"]["name"],
                    },
                }
            )
    return res
