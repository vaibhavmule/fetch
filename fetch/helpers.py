from urllib.parse import urlparse

from bs4 import BeautifulSoup


def sanitize_link(link, url):
    """Sanitizes the link with adding scheme if not present in the link.

    :param link: a hpyerlink
    :type url: str
    :returns: sanitezed link
    :rtype: str
    """
    if link.startswith('//'):
        link = f'http:{link}'
    elif link.startswith('/'):
        parsed_url = urlparse(url)
        link = f'http://{parsed_url.hostname}{link}'
    return link


def get_assets(url, content):
    """Extracts list of links from webpage source.

    :param content: a source code of webpage.
    :type url: str
    :returns: a list of links.
    :rtype: list
    """
    soup = BeautifulSoup(content, 'html.parser')
    image_links = []
    for img in soup.findAll('img'):
        link = img.get('src')
        image_links.append(sanitize_link(link, url))
    return image_links


def get_links(url, content):
    """Extracts list of assets from webpage source.

    :param content: a source code of webpage.
    :type url: str
    :returns: a list of assets.
    :rtype: list
    """
    soup = BeautifulSoup(content, 'html.parser')
    asset_links = []
    for a in soup.findAll('a'):
        link = a.get('href')
        asset_links.append(sanitize_link(link, url))

    return asset_links
