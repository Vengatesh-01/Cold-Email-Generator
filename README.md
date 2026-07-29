<div align="center">

# ✉️ AI Cold Email Generator

**An AI-powered B2B cold email generator that scrapes job postings and crafts hyper-personalised outreach emails — in seconds.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-0.2+-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-7B2BF9?style=for-the-badge)](https://trychroma.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Project Overview

The **AI Cold Email Generator** automates the most time-consuming part of B2B outreach — writing the email. A business development executive can paste any company's careers page URL, and the tool will:

1. **Scrape** the page and extract structured job listings using an LLM
2. **Match** required skills against a portfolio vector store (ChromaDB)
3. **Generate** a personalised cold email that pitches relevant past projects

> 💡 **Scenario:** Nike is hiring a Principal Software Engineer. Instead of manually writing an email, Vengatesh — a BDE at *Catnip Infotech* — pastes Nike's careers URL and gets a polished, relevant cold email in under 10 seconds.

---

## 🖥️ App Screenshot

![App Screenshot](assets/screenshots/app_screenshot.png)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔗 **URL-based Input** | Paste any careers page URL — no manual copy-pasting |
| 🤖 **LLM Job Extraction** | Automatically parses role, skills, experience, and description |
| 🧠 **Semantic Portfolio Matching** | ChromaDB finds the most relevant past projects for each job |
| ✉️ **Personalised Email Generation** | Groq LLaMA 3.3 70B writes a professional cold email |
| 📥 **Download Emails** | One-click download of each generated email as `.txt` |
| 🌙 **Dark AI SaaS UI** | Beautiful, premium dark-mode Streamlit interface |
| ⚡ **Blazing Fast** | Powered by Groq's ultra-low latency LLM inference |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **UI** | [Streamlit](https://streamlit.io) |
| **LLM** | [Groq](https://groq.com) — LLaMA 3.3 70B Versatile |
| **Orchestration** | [LangChain](https://langchain.com) |
| **Vector Store** | [ChromaDB](https://trychroma.com) (persistent, local) |
| **Web Scraping** | LangChain `WebBaseLoader` |
| **Data** | [Pandas](https://pandas.pydata.org) |
| **Config** | [python-dotenv](https://pypi.org/project/python-dotenv/) |

---

## 🏗️ Architecture

```
┌──────────────────┐
│  Careers Page    │  ← User pastes a URL
│  (any company)   │
└────────┬─────────┘
         │ WebBaseLoader scrapes
         ▼
┌──────────────────┐
│  clean_text()    │  ← Removes HTML, URLs, special chars
└────────┬─────────┘
         │
         ▼
┌──────────────────────────────┐
│  LLM (Groq LLaMA 3.3 70B)   │  ← Extracts jobs → JSON
│  JOB_EXTRACTION_PROMPT       │    {role, skills, experience, description}
└────────┬─────────────────────┘
         │
         ├──────────────────────────────────────┐
         │                                      ▼
         │                          ┌───────────────────────┐
         │                          │  ChromaDB             │
         │                          │  (Portfolio Store)    │
         │                          │  query by skills ──── │──► Relevant Links
         │                          └───────────────────────┘
         │                                      │
         ▼                                      │
┌──────────────────────────────┐                │
│  LLM (Groq LLaMA 3.3 70B)   │ ◄──────────────┘
│  EMAIL_GENERATION_PROMPT     │  ← Writes personalised cold email
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────┐
│  Streamlit UI    │  ← Displays + downloads email
└──────────────────┘
```

![Architecture Diagram](assets/screenshots/architecture.png)

---

## 📁 Project Structure

```
COLD-EMAIL-GENERATOR/
│
├── app.py                    # 🚀 Entry point — run this
├── requirements.txt          # Python dependencies
├── .env.example              # Template for environment variables
├── .gitignore
├── LICENSE
│
├── src/                      # Core application logic
│   ├── email_generator.py    # Chain class — job extraction + email writing
│   ├── prompts.py            # All LangChain PromptTemplate definitions
│   ├── llm.py                # Groq LLM client factory
│   ├── portfolio.py          # ChromaDB vector store management
│   └── utils.py              # Text cleaning utilities
│
├── config/
│   └── config.py             # Centralised paths & constants
│
├── data/
│   └── my_portfolio.csv      # Portfolio tech stack + links dataset
│
├── assets/
│   └── screenshots/          # App screenshots for README
│
└── notebooks/                # Exploratory & tutorial notebooks
    ├── email_generator.ipynb
    ├── tutorial_chromadb.ipynb
    └── tutorial_groq.ipynb
```

---

## ⚙️ Installation

### Prerequisites

- Python 3.10+
- A free [Groq API Key](https://console.groq.com/keys)

### 1. Clone the repository

```bash
git clone https://github.com/Vengatesh-01/COLD-EMAIL-GENERATOR.git
cd COLD-EMAIL-GENERATOR
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variable Setup

```bash
# Copy the example file
cp .env.example .env
```

Open `.env` and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> Get your **free** API key at [console.groq.com/keys](https://console.groq.com/keys)

---

## 🚀 Running the Application

```bash
# If 'streamlit' is in your PATH:
streamlit run app.py

# If not (Windows — recommended):
py -m streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

### Usage

1. Enter any company's **careers page URL** in the text field
2. Click **✨ Generate Email**
3. Wait ~5–10 seconds while the AI:
   - Scrapes and analyzes the job description
   - Matches your portfolio against required skills
   - Writes a personalised cold email
4. Copy or **📥 Download** the generated email

---

## 🗂️ Customising Your Portfolio

Edit `data/my_portfolio.csv` to add your own projects:

```csv
"Techstack","Links"
"Python, LangChain, OpenAI","https://github.com/yourname/project1"
"React, Node.js, MongoDB","https://github.com/yourname/project2"
```

> **Tip:** Delete the `vectorstore/` folder after editing the CSV to force ChromaDB to rebuild the index on next run.

---

## 🔮 Future Improvements

- [ ] **Multi-sender support** — configure multiple personas/companies
- [ ] **Email tone selector** — formal / casual / aggressive
- [ ] **CRM integration** — export directly to HubSpot / Notion
- [ ] **Batch processing** — generate emails for multiple job links at once
- [ ] **Email history** — persist and search previously generated emails
- [ ] **Cloud deployment** — one-click deploy to Streamlit Cloud / HuggingFace Spaces
- [ ] **Custom LLM support** — plug in OpenAI, Anthropic, or local Ollama models

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

> **Note:** Commercial use of this software is strictly prohibited without prior written permission from the author. Attribution must be given in all copies or substantial portions of the software.

---

<div align="center">

Built with ❤️ by **Vengatesh** | AI Developer Portfolio Project

</div>
