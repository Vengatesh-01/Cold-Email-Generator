"""
config/config.py
----------------
Centralised project configuration.
All paths and constants are defined here so they can be changed in one place.
"""

import os

# Absolute path to the project root (one level up from this file)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Data paths ────────────────────────────────────────────────────────────────
PORTFOLIO_CSV_PATH = os.path.join(BASE_DIR, "data", "my_portfolio.csv")
VECTORSTORE_PATH   = os.path.join(BASE_DIR, "vectorstore")

# ── LLM settings ─────────────────────────────────────────────────────────────
GROQ_MODEL_NAME = "llama-3.3-70b-versatile"
LLM_TEMPERATURE = 0

# ── ChromaDB settings ─────────────────────────────────────────────────────────
COLLECTION_NAME = "portfolio"
