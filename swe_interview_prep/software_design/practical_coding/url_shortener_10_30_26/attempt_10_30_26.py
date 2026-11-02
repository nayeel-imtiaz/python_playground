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

@dataclass
class LinkRecord:
    id: int
    long_url: str = None
    short_url: str = None

class UrlShortener:
    def __init__(self):
        self.link_records: dict[int, LinkRecord] = {}
        self.long_links: dict[str, int] = {}
        self.short_links: dict[str, int] = {}
        self.current_id: int = 900

    # imp + testing done 5:46
    def get_short_url(self, long_url: str) -> str:
        if long_url in self.long_links:
            return self.link_records[self.long_links[long_url]].short_url
        else:
            short_url = f"https:tinyurl.com/{UrlShortener.convert_to_base_62(self.current_id)}"
            self.link_records[self.current_id] = LinkRecord(self.current_id, short_url, long_url)
            self.short_links[short_url] = self.current_id
            self.long_links[long_url] = self.current_id
            self.current_id += 1
            return short_url

    # imp + testing done 5:53
    def get_long_url(self, short_url: str) -> str:
        if short_url not in self.short_links:
            return "{code: 400, invalid short url}"
        else:
            return self.link_records[self.short_links[short_url]].long_url

    # Finished base 62 imp + testing 5:29 pm
    @staticmethod
    def convert_to_base_62(generated_id: int) -> str:
        current_quotient = generated_id
        digits = deque()
        while current_quotient > 0:
            new_quotient = current_quotient // 62
            new_remainder = current_quotient % 62
            if (
                0 <= new_remainder
                and new_remainder <= 9
            ):
                digits.appendleft(str(new_remainder))
            elif (
                10 <= new_remainder
                and new_remainder <= 35
            ):
                digits.appendleft(chr(ord('a') + (new_remainder - 10)))
            else:
                digits.appendleft(chr(ord('A') + (new_remainder - 36)))
            current_quotient = new_quotient

        return "".join(digits)


def test_convert_to_base_62() -> None:
    assert UrlShortener.convert_to_base_62(11157) == "2TX"


def test_short_url() -> None:
    url_shortener = UrlShortener()
    stack_overflow_short_url = url_shortener.get_short_url("https://stackoverflow.com/questions/3673428/convert-int-to-ascii-and-back-in-python")
    assert stack_overflow_short_url == "https:tinyurl.com/ew"

    github_short_url = url_shortener.get_short_url("https://github.com/nayeel-imtiaz")
    assert github_short_url == "https:tinyurl.com/ex"


def test_long_url() -> None:
    url_shortener = UrlShortener()
    assert url_shortener.get_long_url("https:tinyurl.com/ew") == "{code: 400, invalid short url}"
    github_short_url = url_shortener.get_short_url("https://github.com/nayeel-imtiaz")
    assert github_short_url == "https:tinyurl.com/ew"


def main():
    test_convert_to_base_62()
    test_short_url()
    test_long_url()


if __name__ == '__main__':
    main()
