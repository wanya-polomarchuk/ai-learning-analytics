# ai-learning-analytics

A personal learning analytics system for tracking study sessions and generating AI-powered insights.

## Features

- Track study sessions with subject, duration and learning type
- Store learning data using SQLite
- Analyze study behavior and productivity
- Generate AI-powered learning insights using Gemini AI
- Structured modular Python architecture

## Installation

Clone the repository:

```bash
git clone https://github.com/wanya-polomarchuk/ai-learning-analytics.git
cd ai-learning-analytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## API Key Setup

Set your Gemini API key before running the project:

```bash
export GEMINI_API_KEY="your_api_key"
```
## Run the project:

```bash
python main.py
```
## Project Structure

- `main.py` → main menu and application flow
- `database.py` → database setup and data management
- `analysis.py` → statistical learning analysis
- `ai_analysis.py` → Gemini AI integration and intelligent insights

## Technologies

- Python
- SQLite
- Gemini AI API
