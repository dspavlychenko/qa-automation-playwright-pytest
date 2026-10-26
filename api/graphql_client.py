import requests

from config.settings import GRAPHQL_URL


class GraphQLClient:
    def __init__(self, url: str = GRAPHQL_URL):
        self.url = url
        self.session = requests.Session()

    def query(self, query: str, variables: dict | None = None) -> requests.Response:
        return self.session.post(self.url, json={"query": query, "variables": variables or {}})
