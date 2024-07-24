import json
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = Path(__file__).parent.parent.parent / "data"


def scrape_linkedin_profile(profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles, Manually scrape information from the provided LinkedIn profile"""
    if mock:
        mocked_file_path = DATA_PATH / "mock_data" / "mocked_linkedin_response.json"
        with Path.open(mocked_file_path, mode="r") as f:
            content = json.load(f)
    else:
        api_key = os.environ["PROXYCURL_API_KEY"]
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        response = requests.get(
            api_endpoint,
            params={
                "linkedin_profile_url": f"{profile_url}",
            },
            headers={"Authorization": "Bearer " + api_key},
        )

        content = response.json()

    valid_data = {k: v for k, v in content.items() if v and k != "people_also_viewed"}
    return valid_data


if __name__ == "__main__":
    print(scrape_linkedin_profile(profile_url="mock_url", mock=True))
