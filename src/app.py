# Third Party
from fastapi import FastAPI, Request
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


@app.get("/targets/oob")
def get_oob_targets():
    response = query_nautobot_graphql(OOB_TARGET_QUERY).json()
    res = []
    for interface in response["data"]["interfaces"]:
        for device in interface["ip_addresses"]:
            device_name = interface["device"]["name"]
            device_uuid = interface["device"]["id"]
            core_id = interface["device"]["cf_core_number"]
            location = interface["device"]["location"]["name"]
            location_parent = interface["device"]["location"]["parent"]["name"]
            tenant_uuid = (interface["device"].get("tenant") or {}).get("id", None)
            rack = interface["device"]["rack"]["name"]
            urn = (
                f"urn:rxt:undercloud:{location_parent}:{tenant_uuid or 'tenant'}:"
                f"instance:{location}-{rack}:{device_uuid}"
            ).lower()
            res.append(
                {
                    "targets": [device["host"]],
                    "labels": {
                        "device_name": device_name,
                        "core_id": core_id,
                        "location": location,
                        "rack": rack,
                        "urn": urn,
                    },
                }
            )
    return res
