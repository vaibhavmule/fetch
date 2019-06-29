import pytest

from fetch import fetch

def test_fetch():
    url = 'https://websiteopedia.com/instagram.com'
    links = fetch(url)
    assert len(links['assets']) == 1
    assert len(links['links']) > 1