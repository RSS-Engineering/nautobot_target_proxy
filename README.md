A FastAPI application to query Nautobots GraphQL API to scrape targets for use with Prometheus `http_sd_config`.

# Table of Contents

- [Usage](#usage)
- [Documentation](#documentation)

# Usage

Clone the repository
```shell
gh repo clone RSS-Engineering/nautobot_target_proxy
```

Copy the `.env.example` to `.env` and update the appropriate API keys.

Bring up the Docker compose stack
~~~ shell
docker compose up --build
~~~

# Documentation

Swagger API documentation can be found by browsing to localhost:8000/docs


