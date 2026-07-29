"""
src/email_generator.py
----------------------
Core business logic for extracting job postings from scraped text
and generating personalised cold emails using the Groq LLM.

This module was formerly `app/chains.py`. Logic is unchanged;
the LLM client and prompts are now imported from their own modules.
"""

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from src.llm import get_llm
from src.prompts import JOB_EXTRACTION_PROMPT, EMAIL_GENERATION_PROMPT


class Chain:
    """
    Orchestrates LLM chains for:
      1. Extracting structured job data from raw career-page text.
      2. Writing a personalised cold email for a given job.
    """

    def __init__(self):
        self.llm = get_llm()

    def extract_jobs(self, cleaned_text: str) -> list[dict]:
        """
        Parse job postings from cleaned career-page text.

        Args:
            cleaned_text (str): Pre-processed text from a careers webpage.

        Returns:
            list[dict]: A list of job dicts with keys:
                        role, experience, skills, description.

        Raises:
            OutputParserException: If the LLM output cannot be parsed as JSON.
        """
        chain_extract = JOB_EXTRACTION_PROMPT | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job: dict, links: list) -> str:
        """
        Generate a personalised cold email for a job posting.

        Args:
            job   (dict): Structured job data (role, skills, experience, description).
            links (list): Relevant portfolio links from the vector store.

        Returns:
            str: The generated cold email body.
        """
        chain_email = EMAIL_GENERATION_PROMPT | self.llm
        res = chain_email.invoke({
            "job_description": str(job),
            "link_list": links,
        })
        return res.content
