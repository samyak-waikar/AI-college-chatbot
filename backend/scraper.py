import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unwanted tags
        for script in soup(["script", "style", "noscript"]):
            script.extract()

        # Extract text
        text = soup.get_text(separator=" ")

        # Clean text
        lines = [line.strip() for line in text.splitlines()]
        text = " ".join([line for line in lines if line])

        return text

    except Exception as e:
        print("Error scraping:", e)
        return ""


def save_text(text, filename="data/college_data.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    urls = [
        "https://www.mmcoe.edu.in/",
        "https://www.mmcoe.edu.in/admissions/",
        "https://www.mmcoe.edu.in/departments/"
    ]

    full_text = ""

    for url in urls:
        print(f"Scraping: {url}")
        text = scrape_website(url)
        full_text += text + "\n\n"

    save_text(full_text)

    print("Data saved successfully!")