import requests


def check_site(url):
    try:
        print("Checking...")

        response = requests.get(url, timeout=7)

        status = response.status_code

        match status:
            case 200:
                return f"{status} : OK"

            case 301:
                return f"{status} : Redirect"

            case 404:
                return f"{status} : Not Found"

            case 403:
                return f"{status} : Forbidden"

            case _:
                return f"{status} : Unknown"

    except requests.RequestException as error:
        return f"Error: {error}"