import requests

from .helpers import get_links


def fetch(url):
    """Gets assets and hyperlinks of the webpage.

    :param url: a url of the webpage that needs to scraped.
    :type url: str
    :returns: a dict containing list of assets and hyperlinks.
    :rtype: dict
    """
    r = requests.get(url)
    content = r.content
    assets = get_links('img', 'src', url, content)
    links = get_links('a', 'href', url, content)
    return {
        'assets': assets,
        'links': links
    }
