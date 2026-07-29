"""
src/prompts.py
--------------
All LangChain PromptTemplate definitions used in the application.
Centralising prompts here makes it easy to iterate on them independently
from the rest of the business logic.
"""

from langchain_core.prompts import PromptTemplate


# ── Job Extraction Prompt ─────────────────────────────────────────────────────
JOB_EXTRACTION_PROMPT = PromptTemplate.from_template(
    """
    ### SCRAPED TEXT FROM WEBSITE:
    {page_data}
    ### INSTRUCTION:
    The scraped text is from the career's page of a website.
    Your job is to extract the job postings and return them in JSON format containing
    the following keys: `role`, `experience`, `skills` and `description`.
    Only return the valid JSON.
    ### VALID JSON (NO PREAMBLE):
    """
)

# ── Cold Email Generation Prompt ──────────────────────────────────────────────
EMAIL_GENERATION_PROMPT = PromptTemplate.from_template(
    """
    ### JOB DESCRIPTION:
    {job_description}

    ### INSTRUCTION:
    You are Vengatesh, a business development executive at Catnip Infotech. Catnip Infotech is an AI & Software Consulting company dedicated to facilitating
    the seamless integration of business processes through automated tools.
    Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability,
    process optimization, cost reduction, and heightened overall efficiency.
    Your job is to write a cold email to the client regarding the job mentioned above describing the capability of Catnip Infotech
    in fulfilling their needs.
    Also add the most relevant ones from the following links to showcase Catnip Infotech's portfolio: {link_list}
    Remember you are Vengatesh, BDE at Catnip Infotech.
    Do not provide a preamble.
    ### EMAIL (NO PREAMBLE):

    """
)
