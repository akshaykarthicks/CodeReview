# CodeGenAgent

CodeGenAgent is a Python project that uses the `crewAI` framework to automatically explain and document code. It defines a "crew" of AI agents, with the primary agent being a `code_explainer` that analyzes a given code snippet and generates a detailed explanation.
<img width="1397" height="649" alt="image" src="https://github.com/user-attachments/assets/60a43910-0996-41d7-9545-249e7e7403f1" />


## Features

- **Code Explanation:** Automatically generates explanations for code snippets.
- **Markdown Output:** Saves the explanation in a `report.md` file.
- **Extensible:** Built with `crewAI`, making it easy to add new agents and tasks.

## Workflow

```
+-----------------+      +---------------------+      +--------------------+      +----------------+
|                 |      |                     |      |                    |      |                |
|  User's Code    +----->|    CodeGenAgent     +----->|  Code Explainer    +----->|   report.md    |
|   (main.py)     |      |      (crewAI)       |      |       Agent        |      |  (Markdown)    |
|                 |      |                     |      |                    |      |                |
+-----------------+      +---------------------+      +--------------------+      +----------------+
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/codegenagent.git
   cd codegenagent
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Usage

To run the code explainer, you can either use the provided `run.py` script or execute the `main` module directly.

1. **Set up your environment variables:**

   Create a `.env` file in the root directory of the project and add the following lines:

   ```
   MODEL=gemini/gemini-1.5-flash
   GEMINI_API_KEY=your_gemini_api_key
   ```

   Replace `your_gemini_api_key` with your actual Gemini API key.

2. **Modify the code to be explained:**

   Open `src/codegenagent/main.py` and replace the example code in the `code` variable with the code you want to explain.

3. **Run the agent:**
   ```bash
   python src/codegenagent/main.py
   ```

   This will create a `report.md` file in the root directory containing the explanation of the code.

