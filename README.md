# CodeReview AI

An AI-powered code explanation tool built with CrewAI and Streamlit.

## Features

- 🤖 AI-powered code analysis and explanation
- 🎨 Dark theme UI with red accents
- 📝 Generates detailed markdown reports
- 🚀 Built with CrewAI for intelligent agent workflows

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd CodeReview-1
   ```

2. **Install dependencies**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -e .
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   
   Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Usage

### Run the Streamlit App
```bash
streamlit run app.py
```

### Run the Crew Directly
```bash
python src/codereview/main.py
```

## Project Structure

```
CodeReview-1/
├── src/codereview/          # Main package
│   ├── main.py             # Entry point
│   ├── crew.py             # CrewAI crew definition
│   └── config/             # Agent and task configurations
├── app.py                  # Streamlit web interface
├── pyproject.toml          # Project configuration
└── README.md              # This file
```

## How It Works

1. **Input**: Paste your code into the Streamlit interface
2. **Processing**: CrewAI agents analyze and explain the code
3. **Output**: Detailed explanation saved as `report.md`

## Requirements

- Python 3.10+
- Gemini API key
- Dependencies listed in `pyproject.toml`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details