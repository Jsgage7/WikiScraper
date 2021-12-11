

# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_Russian_monarchs"


def WikiScraper (URL):
    """
    Takes a specified Wikipedia link and scrapes the page,
    returning any links found to other Wikipedia pages.
    *Note: the below print statement is specific to this page,
    for a general print statement comment that out and uncomment
    the general print statement.
    """



    # Url can be any valid Wikipedia page
    response = requests.get(
        url = URL
    )
    if response.status_code != 200:
        print("Invalid URL")

    else:

        #This script scrapes the page
        soup = BeautifulSoup(response.content, 'html.parser')


        # Finds all a refrences from the page, and filters out non-Wikipedia links
        allLinks = soup.find(id="bodyContent").find_all("a")
        output = []

        for link in allLinks:
            try:
                if link['href'].find("/wiki/") == -1:
                    output += ["https://en.wikipedia.org/" + link['href'][1:]]
                    continue
                else:
                    allLinks.remove(link)
            except:
                continue

        # 4-18 are the most relevant results to be displayed for this page,
        # However if your page has less results than this it will throw an error 
        print('\n'.join(output[4:18]))

        #General Print Statement
        #print('\n'.join(output))

WikiScraper(URL)