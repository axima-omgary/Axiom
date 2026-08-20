import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from Axiom_pkg.username_search.checker import check_site
from Axiom_pkg.username_search.sites import build_urls


def check(site, url):
    start = time.perf_counter()

    result = check_site(url)

    elapsed = time.perf_counter() - start

    return site, result, elapsed


def main():
    username = "Axiom"

    sites = build_urls(username)

    total_start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(check, site, url)
            for site, url in sites.items()
        ]

        for future in as_completed(futures):
            site, result, elapsed = future.result()

            print(f"{site}: {elapsed:.6f}s")
            print(f"Result: {result}")

    total_elapsed = time.perf_counter() - total_start

    print(f"\nTotal: {total_elapsed:.6f}s")


if __name__ == "__main__":
    main()