"""
Title: URL shortener
Name: Nayeel Imtiaz
Date: 10/30/26

Prompt:
    Implement an in-memory URL shortener with Base62 encoding, lookup, validation, and tests.
    Treat it as a timed practical coding interview, not a full distributed system.
Time limit:
    60 minutes
"""

# 4:56 start code
from dataclasses import dataclass
from collections import deque

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class UrlShortener:
    def __init__(self):
        self.long_to_code: dict[str, str] = {}
        self.code_to_long: dict[str, str] = {}
        self.current_id: int = 900

    def get_short_url(self, long_url: str) -> str:
        if long_url not in self.long_to_code:
            new_code = UrlShortener.convert_to_base_62(self.current_id)
            self.current_id += 1
            self.code_to_long[new_code] = long_url
            self.long_to_code[long_url] = new_code
        return f"https://short_url.com/{self.long_to_code[long_url]}"

    def get_long_url(self, short_url: str) -> str:
        if not short_url.startswith("https://short_url.com/"):
            return "{code: 400, invalid short url format}"

        code = short_url.lstrip("https://short_url.com/")
        if code not in self.code_to_long:
            return "code: 500, short url does not exist"
        else:
            return self.code_to_long[code]


    @staticmethod
    def convert_to_base_62(generated_id: int) -> str:
        if generated_id < 0:
            raise ValueError("Passed in ID should be non-negative.")

        if generated_id == 0:
            return "0"

        quotient = generated_id
        digits = deque()
        while quotient > 0:
            quotient, remainder = divmod(quotient, 62)
            digits.appendleft(ALPHABET[remainder])

        return "".join(digits)


def test_convert_to_base_62() -> None:
    assert len(ALPHABET) == 62
    assert UrlShortener.convert_to_base_62(11157) == "2TX"
    assert UrlShortener.convert_to_base_62(0) == "0"
    try:
        UrlShortener.convert_to_base_62(-33)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"


def test_short_url_end_to_end() -> None:
    url_shortener = UrlShortener()
    stack_overflow_short_url = url_shortener.get_short_url("https://stackoverflow.com/questions/3673428/convert-int-to-ascii-and-back-in-python")
    assert stack_overflow_short_url == "https://short_url.com/ew"

    github_short_url = url_shortener.get_short_url("https://github.com/nayeel-imtiaz")
    assert github_short_url == "https://short_url.com/ex"

    assert url_shortener.get_long_url("https://short_url.com/ew") == "https://stackoverflow.com/questions/3673428/convert-int-to-ascii-and-back-in-python"
    assert url_shortener.get_long_url("https://short_url.com/ex") == "https://github.com/nayeel-imtiaz"

    assert url_shortener.get_short_url("https://stackoverflow.com/questions/3673428/convert-int-to-ascii-and-back-in-python") == "https://short_url.com/ew"
    assert url_shortener.current_id == 902


def test_short_url_errors() -> None:
    url_shortener = UrlShortener()
    assert url_shortener.get_long_url("www.google.com") == "{code: 400, invalid short url format}"
    assert url_shortener.get_long_url("https://short_url.com/ew") == "{code: 500, short url does not exist}"


def main():
    test_convert_to_base_62()
    test_short_url_end_to_end()
    # test_long_url()

    print("All tests pass.")


if __name__ == '__main__':
    main()
