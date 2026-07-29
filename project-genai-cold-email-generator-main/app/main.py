import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def apply_custom_css():
    st.markdown("""
        <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        /* Dark Minimal AI SaaS Theme Background & Text */
        .stApp {
            background-color: #0B0F19;
            color: #F1F5F9;
        }

        /* Hide Streamlit Default Menu, Footer and Header */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Hero Container */
        .hero-container {
            text-align: center;
            padding: 2.5rem 1rem 1.5rem 1rem;
            max-width: 720px;
            margin: 0 auto 1rem auto;
        }

        .hero-title {
            font-size: 2.75rem;
            font-weight: 800;
            background: linear-gradient(135deg, #FFFFFF 0%, #E2E8F0 60%, #94A3B8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.75rem;
            letter-spacing: -0.02em;
            line-height: 1.25;
        }

        .hero-subtitle {
            font-size: 1.05rem;
            color: #94A3B8;
            line-height: 1.6;
            font-weight: 400;
        }

        /* Streamlit Container Border Styling for Cards */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(30, 41, 59, 0.45) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 16px !important;
            padding: 1.25rem !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2) !important;
            margin-bottom: 1.5rem !important;
        }

        .card-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: #F8FAFC;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        /* Text Input Styling */
        .stTextInput > label {
            color: #CBD5E1 !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
            margin-bottom: 0.4rem !important;
        }

        .stTextInput > div > div > input {
            background-color: #1E293B !important;
            color: #F8FAFC !important;
            border: 1px solid #334155 !important;
            border-radius: 10px !important;
            padding: 0.75rem 1rem !important;
            font-size: 0.95rem !important;
            transition: all 0.2s ease;
        }

        .stTextInput > div > div > input:focus {
            border-color: #6366F1 !important;
            box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
        }

        /* Modern Primary Button */
        .stButton > button {
            width: 100%;
            background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%) !important;
            color: #FFFFFF !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.75rem 1.5rem !important;
            margin-top: 0.25rem !important;
            box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35) !important;
            transition: all 0.2s ease-in-out !important;
        }

        .stButton > button:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5) !important;
            background: linear-gradient(135deg, #4F46E5 0%, #4338CA 100%) !important;
        }

        /* Secondary Download Button */
        .stDownloadButton > button {
            background: #1E293B !important;
            color: #F8FAFC !important;
            border: 1px solid #334155 !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
            padding: 0.6rem 1.25rem !important;
            transition: all 0.2s ease !important;
        }

        .stDownloadButton > button:hover {
            background: #334155 !important;
            border-color: #475569 !important;
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #0F172A;
            border-right: 1px solid rgba(255, 255, 255, 0.08);
        }

        .sidebar-brand {
            font-size: 1.15rem;
            font-weight: 700;
            color: #F8FAFC;
            margin-bottom: 0.75rem;
        }

        .sidebar-desc {
            font-size: 0.88rem;
            color: #94A3B8;
            line-height: 1.55;
            margin-bottom: 1.25rem;
        }

        .sidebar-feature-item {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            font-size: 0.88rem;
            color: #CBD5E1;
            margin-bottom: 0.65rem;
        }

        .feature-icon {
            color: #10B981;
            font-weight: 700;
        }

        /* Footer */
        .custom-footer {
            text-align: center;
            padding: 2rem 0 1.5rem 0;
            color: #64748B;
            font-size: 0.85rem;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
            margin-top: 3rem;
        }
        </style>
    """, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown("<div class='sidebar-brand'>AI Cold Email Generator</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='sidebar-desc'>An AI assistant that helps create personalized job outreach emails by analyzing job descriptions and matching relevant experience.</div>",
            unsafe_allow_html=True
        )

        st.markdown("<hr style='border-color: rgba(255, 255, 255, 0.08); margin: 1.25rem 0;'>", unsafe_allow_html=True)
        
        st.markdown("<div style='font-size: 0.95rem; font-weight: 700; color: #F8FAFC; margin-bottom: 0.85rem;'>Features</div>", unsafe_allow_html=True)

        features = [
            "Analyze job postings",
            "Generate personalized emails",
            "Match relevant projects",
            "Improve job outreach"
        ]

        for feat in features:
            st.markdown(f"""
                <div class="sidebar-feature-item">
                    <span class="feature-icon">✓</span>
                    <span>{feat}</span>
                </div>
            """, unsafe_allow_html=True)


def create_streamlit_app(llm, portfolio, clean_text):
    apply_custom_css()
    render_sidebar()

    # Centered Hero Section
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">AI Cold Email Generator</h1>
            <p class="hero-subtitle">
                Generate personalized cold emails for job opportunities using AI-powered analysis.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Main Input Section wrapped inside Streamlit bordered container
    with st.container(border=True):
        url_input = st.text_input(
            "Enter a URL:",
            value="https://careers.nike.com/",
            placeholder="Paste a job description URL here..."
        )
        
        submit_button = st.button("✨ Generate Email", key="generate_btn")

    if submit_button:
        if not url_input.strip():
            st.warning("Please enter a valid job posting URL.")
            return

        status_box = st.status("Initializing analysis...", expanded=True)
        try:
            status_box.update(label="Analyzing job description...", state="running")
            loader = WebBaseLoader([url_input])
            raw_content = loader.load().pop().page_content
            data = clean_text(raw_content)

            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)

            if not jobs:
                status_box.update(label="No job postings could be found at the provided URL.", state="error")
                st.error("Could not extract job details from the provided URL. Please verify the link and try again.")
                return

            status_box.update(label="Finding relevant experience...", state="running")
            
            for idx, job in enumerate(jobs, 1):
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)

                status_box.update(label="Creating personalized email...", state="running")
                email = llm.write_mail(job, links)

                status_box.update(label="Email generated successfully.", state="complete", expanded=False)

                # Generated Email Output Section inside Streamlit bordered container
                with st.container(border=True):
                    st.markdown("<div class='card-title'>✉️ Generated Email</div>", unsafe_allow_html=True)
                    
                    st.code(email, language='markdown')

                    st.download_button(
                        label="📥 Download Email",
                        data=email,
                        file_name=f"cold_email_{job.get('role', 'job').lower().replace(' ', '_')}.txt",
                        mime="text/plain",
                        key=f"download_btn_{idx}"
                    )

        except Exception as e:
            status_box.update(label="Error processing request", state="error", expanded=True)
            st.error(f"An error occurred: {e}")

    # Clean Footer
    st.markdown("""
        <div class="custom-footer">
            AI-powered job outreach assistant
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="centered", page_title="AI Cold Email Generator", page_icon="✉️")
    create_streamlit_app(chain, portfolio, clean_text)
