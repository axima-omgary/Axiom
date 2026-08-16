from .validator import check_username
from .checker import check_site
from .sites import build_urls


def main():

    username = input("Enter the username: ")

    result = check_username(username)

    if result == "Valid":

        print(result)

        sites = build_urls(username)

        print("Generated URLs:")

        for site, url in sites.items():

            result = check_site(url)

            print(site, "-->", url, "|", result)

    else:
        print(result)


if __name__ == "__main__":
    main()