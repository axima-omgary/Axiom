import json
from importlib.resources import files



def build_urls(username):
    file = files("Axiom_pkg").joinpath("sites.json")

    with file.open("r", encoding="utf-8") as f:
        sites = json.load(f)

    urls = {}

    for site, template in sites.items():
        urls[site] = template.replace("{username}", username)

    return urls