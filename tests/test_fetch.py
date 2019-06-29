import pytest
from requests.exceptions import MissingSchema

from fetch import fetch


def test_fetch():
    url = 'https://websiteopedia.com/instagram.com'
    links = fetch(url)
    assert len(links['assets']) == 1
    assert len(links['links']) > 1


def test_fetch_with_invalid_url():
    url = 'foo'
    with pytest.raises(MissingSchema):
        fetch(url)
