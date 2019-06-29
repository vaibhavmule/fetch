from urllib.parse import urlparse

from bs4 import BeautifulSoup


def sanitize_link(link, url):
    """Sanitizes the link with adding scheme if not present in the link.

    :param link: a hpyerlink
    :type link: str
    :param url: a url of the webpage.
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


def get_links(tag, attribute, url, content):
    """Get links with specified tag and it's attribute
    
    :param tag: a html tag
    :type tag: str
    :param attribute: a specified tag's attribute
    :type attribute: str
    :param url: a url of the webpage.
    :type url: str
    :param content: a source code of webpage.
    :type content: str
    :returns: a list of links.
    :rtype: list
    """
    soup = BeautifulSoup(content, 'html.parser')
    links = []
    for link in soup.findAll(tag):
        link = link.get(attribute)
        links.append(sanitize_link(link, url))
    return links
