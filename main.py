import time
from config.settings import SPREADSHEET_URL
from job_scraper.scraper import JobScraper
from multiprocessing import Process


def run_scraper(base_link):
    """
    Runs the job scraper for the specified base link.

    Args:
        base_link (str): The base URL for the job scraper.
    """
    while True:
        try:
            print(f"Starting job scraper for {base_link}...")
            scraper = JobScraper(base_link, SPREADSHEET_URL)
            scraper.scrape_jobs()
            print(f"Job scraper for {base_link} completed. Waiting for the next run...")
        except Exception as e:
            print(f"An error occurred for {base_link}: {e}")

        time.sleep(5)


def main():
    # Define base links for both scrapers
    base_links = [
        "https://www.cv-library.co.uk",
        "https://findajob.dwp.gov.uk/"
    ]

    # Create a process for each base link
    processes = []
    for base_link in base_links:
        process = Process(target=run_scraper, args=(base_link,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()


if __name__ == "__main__":
    main()