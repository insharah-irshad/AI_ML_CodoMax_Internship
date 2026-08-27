# AI Text Summarizer

An AI-powered text summarization application built with Python and Google's Gemini API.

This project was developed as part of the CodoMax AI/ML Internship — Module 5: AI Tools & Mini Project.

## Features

- AI-powered text summarization
- Uses Google Gemini API
- Short, medium, and detailed summary options
- Supports multi-line text input
- Simple command-line interface
- Handles missing API keys and errors
- Beginner-friendly Python implementation

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK

## Project Structure

```text
AI_Text_Summarizer/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

# API Key Setup

The application requires a Gemini API key.

Set the API key as an environment variable.

## Windows PowerShell
$env:GEMINI_API_KEY="YOUR_API_KEY_HERE"

Do not upload your API key to GitHub.

# How It Works
The user selects a summary length.
The user enters the text they want to summarize.
The application sends the text to the Gemini API.
Gemini processes the text.
The generated summary is displayed in the terminal.