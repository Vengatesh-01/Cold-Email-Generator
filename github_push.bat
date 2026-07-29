@echo off
echo ============================================================
echo  AI Cold Email Generator - GitHub Setup Script
echo ============================================================
echo.

REM ── Step 1: Copy images ─────────────────────────────────────
echo [1/4] Copying screenshots...
if not exist "assets\screenshots" mkdir "assets\screenshots"
copy /Y "project-genai-cold-email-generator-main\imgs\architecture.png" "assets\screenshots\architecture.png" >nul 2>&1
copy /Y "project-genai-cold-email-generator-main\imgs\img.png" "assets\screenshots\app_screenshot.png" >nul 2>&1
echo       Done.

REM ── Step 2: Copy notebooks ──────────────────────────────────
echo [2/4] Copying notebooks...
if not exist "notebooks" mkdir "notebooks"
copy /Y "project-genai-cold-email-generator-main\email_generator.ipynb" "notebooks\email_generator.ipynb" >nul 2>&1
copy /Y "project-genai-cold-email-generator-main\tutorial_chromadb.ipynb" "notebooks\tutorial_chromadb.ipynb" >nul 2>&1
copy /Y "project-genai-cold-email-generator-main\tutorial_groq.ipynb" "notebooks\tutorial_groq.ipynb" >nul 2>&1
echo       Done.

REM ── Step 3: Git add + commit ────────────────────────────────
echo [3/4] Committing new structure to Git...
git add .
git commit -m "refactor: restructure project into professional GitHub portfolio layout

- Add clean src/ package (email_generator, prompts, llm, portfolio, utils)
- Add config/ package with centralised paths and constants
- Add root app.py as single entry point (streamlit run app.py)
- Separate LLM init, prompts, and Chain logic into dedicated modules
- Move portfolio CSV to data/ folder
- Move screenshots to assets/screenshots/
- Move tutorial notebooks to notebooks/
- Add professional README with badges, architecture, installation guide
- Add .env.example with placeholder API key
- Update .gitignore to exclude .env, vectorstore, venv, __pycache__"
echo       Done.

REM ── Step 4: Push to GitHub ──────────────────────────────────
echo [4/4] Pushing to GitHub...
git push origin main
echo       Done.

echo.
echo ============================================================
echo  SUCCESS! Professional structure is now live on GitHub.
echo ============================================================
echo.
echo  Next steps:
echo  1. Create your .env file:  copy .env.example .env
echo  2. Edit .env and add your GROQ_API_KEY
echo  3. Run the app: py -m streamlit run app.py
echo     OR: python -m streamlit run app.py
echo.
pause
