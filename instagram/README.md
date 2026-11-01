# Instagram unfollower checker script

***

## How to run

1) Export following/follower data from meta account center.
2) Make directory `instagram_data` if it doesn't exist yet, 
and copy input files (follower and following data) to appropriate locations.
3) Run `python -m instagram.app.main` from root (`python_playground/`)
4) Choose script mode "A", "R", or "U" when prompted by entering into terminal.
5) Navigate to output directory specified in logs.

## Example output:
```
❯ python -m instagram.app.main
2026-11-01 01:27:00 [INFO] Instagram scraper started.
Choose mode:
  [A] All not-following-back (snapshot)
  [R] Recent not-following-back (delta)
  [U] Recent unfollowers (followers_old - followers_new)
Default: A
> 
Enter date for snapshot (MM-DD-YY), default [12-12-25]: 
2026-11-01 01:27:16 [INFO] Using followers file: /Users/nayeelimtiaz/Documents/code_repositories/python_playground/instagram/instagram_data/followers/12-12-25.json
2026-11-01 01:27:16 [INFO] Using following file: /Users/nayeelimtiaz/Documents/code_repositories/python_playground/instagram/instagram_data/following/12-12-25.json
2026-11-01 01:27:16 [INFO] Output will be saved to: /Users/nayeelimtiaz/Documents/code_repositories/python_playground/instagram/output/instagram_scraper_output/12-12-25_not_following_back.csv
2026-11-01 01:27:16 [INFO] Scraping complete.
2026-11-01 01:27:16 [INFO] Done.
```

***

## Backlog

- Organize input in `instagram_data` and output by year, then month, then full date
  - Suggested fix: 
    1) Edit in code where script gets inputs and where it'll be saved
    2) Run a script to move around existing data files in previous file directory format.