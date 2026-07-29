"""
src/utils.py
------------
Text cleaning utilities for preprocessing scraped web content
before passing to the LLM.
"""

import re


def clean_text(text: str) -> str:
    """
    Cleans raw scraped text by removing HTML tags, URLs,
    special characters, and normalising whitespace.

    Args:
        text (str): Raw text scraped from a webpage.

    Returns:
        str: Cleaned, normalised plain text.
    """
    # Remove HTML tags
    text = re.sub(r'<[^>]*?>', '', text)
    # Remove URLs
    text = re.sub(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        '', text
    )
    # Remove special characters (keep alphanumerics and spaces)
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    # Collapse multiple spaces into one
    text = re.sub(r'\s{2,}', ' ', text)
    # Trim and normalise
    text = ' '.join(text.split())
    return text
