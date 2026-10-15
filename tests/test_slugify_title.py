from pipfixture import slugify_title


def test_slugify_title():
    assert slugify_title("Hello, World!") == "hello-world"
