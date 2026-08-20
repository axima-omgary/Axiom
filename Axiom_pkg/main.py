import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

from .username_search.validator import check_username
from .username_search.checker import check_site
from .username_search.sites import build_urls


MAX_WORKERS = 3


def search_sites(username, workers):

    result = check_username(username)

    if result != "Valid":
        print(result)
        return

    print(result)

    sites = build_urls(username)

    print("Generated URLs:")

    with ThreadPoolExecutor(max_workers=workers) as executor:

        futures = {
            executor.submit(check_site, url): site
            for site, url in sites.items()
        }

        for future in as_completed(futures):

            site = futures[future]

            try:
                result = future.result()
            except Exception as error:
                result = f"Error: {error}"

            print(
                site,
                "-->",
                sites[site],
                "|",
                result
            )


def main():

    parser = argparse.ArgumentParser(
        prog="Axiom",
        description="Username reconnaissance tool"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # ---------------------------------
    # search-sites
    # ---------------------------------

    search_parser = subparsers.add_parser(
        "search-sites",
        help="Search for a username across supported sites"
    )

    search_parser.add_argument(
        "username",
        help="Username to search for"
    )

    search_parser.add_argument(
        "--workers",
        type=int,
        default=MAX_WORKERS,
        help=f"Number of workers (default: {MAX_WORKERS})"
    )

    args = parser.parse_args()

    # ---------------------------------
    # Commands
    # ---------------------------------

    if args.command == "search-sites":

        if args.workers < 1:
            parser.error("--workers must be at least 1")

        search_sites(
            args.username,
            args.workers
        )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()