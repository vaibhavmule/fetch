import requests

def fetch(url):
    """Gets assets and hyperlinks of the webpage.

    :param url: a url of the webpage that needs to scraped.
    :type url: str
    :returns: a dict containing list of assets and hyperlinks.
    :rtype: dict
    """
    r = requests.get(url)
    if r.status_code == 200:
        print('success', r.content)

    return {
        'assets': [],
        'links' : []
    }


if __name__ == "__main__":
    url = 'https://www.google.com/'
    fetch(url)
