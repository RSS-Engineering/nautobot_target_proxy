# Standard Library
import os

# Third Party
import requests

GRAPHQL_URL = "https://nautobot.dev.undercloud.rackspace.net/api/graphql/"


def query_nautobot_graphql(query):
    nautobot_token = os.environ.get("NAUTOBOT_TOKEN")
    if not nautobot_token:
        raise RuntimeError("A Nautobot Token is required")
    headers = {
        "Authorization": f"Token {nautobot_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    res = requests.post(GRAPHQL_URL, headers=headers, json={"query": query})
    res.raise_for_status()
    return res
