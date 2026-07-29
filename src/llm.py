"""
src/llm.py
----------
LLM client factory.
Initialises and returns the Groq chat model used throughout the application.
Separating the client from business logic makes it easy to swap models later.
"""

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from config.config import GROQ_MODEL_NAME, LLM_TEMPERATURE

load_dotenv()


def get_llm() -> ChatGroq:
    """
    Initialise and return the Groq LLM client.

    Reads GROQ_API_KEY from the environment (loaded via python-dotenv).

    Returns:
        ChatGroq: A configured LangChain ChatGroq instance.

    Raises:
        ValueError: If GROQ_API_KEY is not set in the environment.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is not set. "
            "Copy .env.example to .env and add your Groq API key."
        )
    return ChatGroq(
        temperature=LLM_TEMPERATURE,
        groq_api_key=api_key,
        model_name=GROQ_MODEL_NAME,
    )
