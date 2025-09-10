# SQLite workaround for Streamlit Cloud (Linux environment)
try:
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    # On Windows or if pysqlite3 is not available, use system sqlite3
    pass

import streamlit as st
import sqlite3

def set_custom_theme():
    st.set_page_config(
        layout="wide", 
        page_title="Code-Review",
        page_icon="🤖"
    )
    custom_css = """
    <style>
        /* Custom color scheme based on user requirements */
        :root {
            /* Background and Foreground */
            --background: #262624;
            --foreground: #c3c0b6;
            
            /* Primary */
            --primary: #d97757;
            --primary-foreground: #ffffff;
            
            /* Secondary */
            --secondary: #faf9f5;
            --secondary-foreground: #30302e;
            
            /* Accent */
            --accent: #1a1915;
            --accent-foreground: #f5f4ee;
            
            /* UI Components */
            --card: #262624;
            --card-foreground: #faf9f5;
            --popover: #30302e;
            --popover-foreground: #e5e5e2;
            --muted: #1b1b19;
            --muted-foreground: #b7b5a9;
            
            /* Utility & Form */
            --border: #3e3e38;
            --input: #52514a;
            --ring: #d97757;
            
            /* Status */
            --destructive: #ef4444;
            --destructive-foreground: #ffffff;
            
            /* Utilities */
            --border-radius: 12px;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
        
        /* Base styles */
        body {
            background-color: var(--background) !important;
            color: var(--foreground) !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        .stApp {
            background-color: var(--background);
        }
        
        /* Header styles */
        header {
            background: linear-gradient(135deg, var(--background) 0%, var(--card) 100%) !important;
        }
        
        /* Button styles */
        .stButton > button {
            background: linear-gradient(135deg, var(--primary) 0%, #c05a3d 100%);
            color: var(--primary-foreground);
            border: none;
            border-radius: var(--border-radius);
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: var(--shadow);
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(217, 119, 87, 0.3), 0 4px 6px -2px rgba(217, 119, 87, 0.1);
        }
        
        .stButton > button:active {
            transform: translateY(0);
        }
        
        /* Text area styles */
        .stTextArea textarea {
            background-color: var(--input) !important;
            border: 1px solid var(--border) !important;
            border-radius: var(--border-radius) !important;
            color: var(--secondary-foreground) !important;
            box-shadow: var(--shadow);
        }
        
        /* Markdown styles */
        .stMarkdown {
            color: var(--foreground) !important;
        }
        
        /* Headers */
        h1, h2, h3, h4, h5, h6 {
            color: var(--secondary) !important;
            font-weight: 700 !important;
        }
        
        /* Hero section */
        .hero {
            background: linear-gradient(135deg, var(--background) 0%, var(--card) 100%);
            padding: 3rem 2rem;
            border-radius: var(--border-radius);
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
        }
        
        .hero h1 {
            font-size: 3rem !important;
            margin-bottom: 1rem;
            background: linear-gradient(90deg, var(--primary), #e89a7d);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .hero p {
            font-size: 1.2rem;
            color: var(--secondary) !important;
            max-width: 800px;
            margin: 0 auto 2rem auto;
            line-height: 1.6;
        }
        
        /* Feature cards with equal height */
        .feature-card {
            background: var(--card);
            border-radius: var(--border-radius);
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: var(--shadow);
            transition: transform 0.3s ease;
            height: 100%;
            display: flex;
            flex-direction: column;
            border: 1px solid var(--border);
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
        }
        
        .feature-card h3 {
            color: var(--card-foreground) !important;
            margin-top: 0;
        }
        
        .feature-card p {
            color: var(--muted-foreground) !important;
            flex-grow: 1;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 2rem 0;
            color: var(--muted-foreground) !important;
            margin-top: 2rem;
        }
        
        /* Divider */
        hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--border), transparent);
            margin: 2rem 0;
        }
        
        /* Report section */
        .report-container {
            background: var(--card);
            border-radius: var(--border-radius);
            padding: 2rem;
            margin-top: 2rem;
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
        }
        
        /* Equal height columns */
        div[data-testid="column"] {
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        
        /* Input labels */
        .stTextArea label {
            color: var(--secondary) !important;
            font-weight: 500 !important;
        }
        
        /* Success and error messages */
        .stAlert [data-baseweb="notification"] {
            border-radius: var(--border-radius) !important;
        }
        
        .stAlert.success {
            background-color: rgba(34, 197, 94, 0.1) !important;
            color: #bbf7d0 !important;
            border: 1px solid #22c55e !important;
        }
        
        .stAlert.error {
            background-color: rgba(239, 68, 68, 0.1) !important;
            color: #fecaca !important;
            border: 1px solid var(--destructive) !important;
        }
        
        .stAlert.warning {
            background-color: rgba(251, 191, 36, 0.1) !important;
            color: #fef08a !important;
            border: 1px solid #fbbf24 !important;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def render_hero_section():
    st.markdown("""
    <div class="hero">
        <h1>Code-Review-AI</h1>
        <p>Your intelligent code explainer that transforms complex code into clear, understandable documentation with inline comments, docstrings, and comprehensive guides.</p>
    </div>
    """, unsafe_allow_html=True)

def render_features():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>AI-Powered Analysis</h3>
            <p>Leverages advanced AI to understand and explain your code in simple terms.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>Detailed Documentation</h3>
            <p>Generates inline comments, docstrings, and README-style explanations.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>Instant Results</h3>
            <p>Get clear code explanations in seconds, not hours.</p>
        </div>
        """, unsafe_allow_html=True)

def main():
    set_custom_theme()
    
    # Hero section
    render_hero_section()
    
    # Features section
    render_features()
    
    st.markdown("---")
    
    # Code input section
    st.header("Explain Your Code")
    st.caption("Paste your code below and let our AI generate a clear explanation")
    
    code = st.text_area("Paste your code here", height=250, label_visibility="collapsed")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_btn = st.button("Generate Explanation", use_container_width=True)
    
    if generate_btn:
        if code:
            with st.spinner("AI is analyzing your code..."):
                try:
                    from src.codereview.main import run as run_crew
                    run_crew(code)
                    with open("report.md", "r", encoding="utf-8") as f:
                        report = f.read()
                    st.success("Explanation generated successfully!")
                    
                    st.markdown("---")
                    st.header("Generated Report")
                    st.markdown("Here's the AI-generated explanation of your code:")
                    st.markdown('<div class="report-container">', unsafe_allow_html=True)
                    st.markdown(report, unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please paste some code to explain.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        Made with love by <a href="https://github.com/akshaykarthicks" target="_blank" style="color: var(--primary);">akshaykarthicks</a> | 
        Powered by CrewAI & Streamlit
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()