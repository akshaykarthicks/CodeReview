import streamlit as st

def set_custom_theme():
    st.set_page_config(layout="wide", page_title="CodeGenAgent Frontend")
    custom_css = """
    <style>
        body {
            background-color: #000000 !important;
            color: #ffffff !important;
        }
        .stApp {
            background-color: #000000;
        }
        .stTextArea, .stButton > button {
            border: 1px solid #ff0000 !important;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
        }
        .stMarkdown {
            color: #ffffff !important;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def main():
    set_custom_theme()
    st.title("CodeGenAgent Frontend")
    st.header("Your AI-powered code explainer")

    st.info("Please make sure you have a `.env` file in the root of this project with your `GEMINI_API_KEY` set.")

    code = st.text_area("Paste your code here", height=200)

    if st.button("Generate Explanation"):
        if code:
            with st.spinner("Generating explanation... Please wait."):
                try:
                    from src.codegenagent.main import run as run_crew
                    run_crew(code)
                    with open("report.md", "r") as f:
                        report = f.read()
                    st.success("Explanation generated successfully!")
                    st.markdown("---")
                    st.subheader("Generated Report")
                    st.markdown(report, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please paste some code to explain.")

    st.markdown("---")
    st.markdown("Made with ❤️ by [akshaykarthicks](https://github.com/akshaykarthicks)")

if __name__ == "__main__":
    main()
