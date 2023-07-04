#! /bin/python
# Name:        top250.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: Download the top 250 movies chosen by IMDb users.
"""
    Download and display online movie information.
"""
import sys
import imdb
import re

def main():
    ia = imdb.IMDb()

    pattern = input("Enter movie search string: ")

    for rank, movie in enumerate(ia.get_top250_movies(), start=1):
        m = re.search(pattern, str(movie), re.IGNORECASE)
        if m:
            print(f"{rank:>4}: {movie}")

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)