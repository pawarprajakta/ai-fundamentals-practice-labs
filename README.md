
# AI Text Analyzer

## 1. Project Overview
AI Text Analyzer is a beginner-friendly Python project that
performs text analysis and basic rule-based sentiment classification.

## 2. Objectives
- Understand basic AI and text-processing concepts.
- Calculate word and character counts.
- Classify text as positive, negative, or neutral.
- Practice Python modules and functions.
- Manage application settings using JSON.
- Handle invalid inputs and test application behavior.

## 3. Technologies Used
- Python 3
- JSON
- pytest
- Git and GitHub

## 4. Project Structure
- app/analyzer.py: Text processing and sentiment classification.
- app/config.py: Configuration loading and validation.
- app/main.py: Command-line application.
- config.json: Application settings.
- tests/test_analyzer.py: Automated unit tests.
- requirements.txt: Python dependencies.

## 5. Setup Instructions
1. Install Python 3 and Git.
2. Clone the repository.
3. Create a virtual environment.
4. Activate the virtual environment.
5. Install dependencies.

Commands:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## 6. Run the Application

    python -m app.main

Enter text when prompted. Type exit to close the application.

## 7. Run Unit Tests

    pytest -v

## 8. Configuration
Edit config.json to change the application name, maximum
text length, and word-list display setting.

## 9. Error Handling
The application validates text input, rejects empty strings,
checks maximum text length, and handles configuration errors.

## 10. Expected Results
The application displays text statistics and a basic
sentiment classification. Unit tests verify the main behavior.

## 11. Limitations
Sentiment classification uses predefined word lists.
It does not understand context, sarcasm, or complex language.
This project demonstrates foundational text-processing
concepts and is not a trained AI model.
