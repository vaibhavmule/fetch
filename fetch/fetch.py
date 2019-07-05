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


def crawl_access(url):
    """Example Payoad: {url1: [asset1, asset2], url2: [asset3], url3: [asset4, asset5]}"""
    output = {}
    response = fetch(url)
    output[url] = response['assets']
    links = response['links']
    for link in links:
        res = crawl_access(link)
        output.update(res)
    return output
