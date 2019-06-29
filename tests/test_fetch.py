import pytest
from requests.exceptions import MissingSchema

from fetch import fetch
from fetch.helpers import sanitize_link


def test_fetch():
    url = 'https://websiteopedia.com/instagram.com'
    links = fetch(url)
    assert len(links['assets']) == 1
    assert len(links['links']) > 1


def test_fetch_with_invalid_url():
    url = 'foo'
    with pytest.raises(MissingSchema):
        fetch(url)


def test_sanitize_if_link_starts_with_slash():
    url = 'http://websiteopedia.com'
    link = '/about'
    assert sanitize_link(link, url) == 'http://websiteopedia.com/about'


def test_sanitize_if_link_starts_with_double_slash():
    url = 'http://websiteopedia.com'
    link = '//instagram.com'
    assert sanitize_link(link, url) == 'http://instagram.com'
