from pipfixture import build_url


def test_build_url_encodes_params():
    assert build_url("https://example.org/search", {"q": "a b"}) == "https://example.org/search?q=a+b"


def test_build_url_without_params():
    assert build_url("https://example.org/", {}) == "https://example.org/"
