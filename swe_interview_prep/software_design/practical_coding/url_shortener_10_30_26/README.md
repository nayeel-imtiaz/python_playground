Prompt: 
    Implement an in-memory URL shortener with Base62 encoding, lookup, validation, and tests. 
    Treat it as a timed practical coding interview, not a full distributed system.
Time limit: 
    60 minutes

Start: 4:30

Questions:
.

Design:
- API supports two operations:
  - set_short_url(long_url: str) -> str (short string)
  - get_long_url(short_url: str) -> str (long string)

Store "link records"  in Database (represented as a dictionary here)
    - LinkRecord(id, short_url, long_url)

data_store: dict[int: LinkRecord]
    - Map id to corresponding LinkRecord

short_links: dict[str: int]
    - Map short link strict to id to access long link in data store

long_links: dict[str: int]
    - Map long link to id to access short link in data store

base_62 conversion is math algorithm takes takes base 10 to base 62 postfix used by short link.

***
4:56