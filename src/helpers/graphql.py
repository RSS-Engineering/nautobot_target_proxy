# Third Party
import requests

GRAPHQL_URL = "https://nautobot.dev.undercloud.rackspace.net/api/graphql/"
HEADERS = {
    "Authorization": "Token 0uxmqadLzkhKzyK716UZcV0cudEggXrttMIKOXP7",
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def query_nautobot_graphql(query):
    res = requests.post(GRAPHQL_URL, headers=HEADERS, json={"query": query})
    res.raise_for_status()
    return res
