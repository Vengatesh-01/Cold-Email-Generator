"""
src/portfolio.py
----------------
Portfolio management using ChromaDB as a persistent vector store.

Loads tech-stack / portfolio link pairs from a CSV file and stores them
in a ChromaDB collection so that relevant project links can be retrieved
by similarity search against a job's required skills.

This module was formerly `app/portfolio.py`. Paths are now loaded from
`config/config.py` instead of being hardcoded.
"""

import uuid
import pandas as pd
import chromadb

from config.config import PORTFOLIO_CSV_PATH, VECTORSTORE_PATH, COLLECTION_NAME


class Portfolio:
    """
    Manages the portfolio vector store.

    Attributes:
        file_path  (str): Path to the portfolio CSV file.
        data       (DataFrame): Loaded portfolio data.
        collection : ChromaDB collection for similarity queries.
    """

    def __init__(self, file_path: str = PORTFOLIO_CSV_PATH):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient(VECTORSTORE_PATH)
        self.collection = self.chroma_client.get_or_create_collection(
            name=COLLECTION_NAME
        )

    def load_portfolio(self) -> None:
        """
        Populate the ChromaDB collection with portfolio data.
        Only inserts if the collection is empty (idempotent).
        """
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=row["Techstack"],
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())],
                )

    def query_links(self, skills: list[str]) -> list:
        """
        Retrieve the most relevant portfolio links for a given skill set.

        Args:
            skills (list[str]): A list of required skill strings from a job posting.

        Returns:
            list: Metadata dicts containing relevant portfolio links.
        """
        return self.collection.query(
            query_texts=skills, n_results=2
        ).get('metadatas', [])
