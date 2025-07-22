# 💡 AI-Powered Flashcard Generator

A smart study tool leveraging advanced AI to transform PDF documents into custom flashcards. This project demonstrates a robust data processing pipeline for RAG applications, with a strong focus on **multilingual content, especially Japanese**.

**Built with:**

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-000000?logo=flask&logoColor=white&style=for-the-badge)](https://flask.palletsprojects.com/)
[![Google Gemini API](https://img.shields.io/badge/Google%20Gemini%20API-1.16.1-4285F4?logo=google&logoColor=white&style=for-the-badge)](https://ai.google.dev/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.26-000000?logo=langchain&logoColor=white&style=for-the-badge)](https://www.langchain.com/)
[![PyMuPDF](https://img.shields.io/badge/PyMuPDF-1.25.5-000000?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTcgMkM1LjQ0IDIgNCAzLjQ0IDQgNVYxOUM0IDIwLjU2IDUuNDQgMjIgNyAyMkwxNyAyMkMxOC41NiAyMiAyMCAyMC41NiAyMCAxOVY1QzIwIDMuNDQgMTguNTYgMiAxNyAyTDMuNzkyNSAyLjI1NjI4QzIuODUyNzUgMi4zMTY1NiAyLjE5MDQ5IDMuMjY2NDQgMi4yNTU2NSA0LjA2NjYzTDIuNDc0MzYgNi42MTk4MkM0LjE3MzQ0IDYuODAyNDkgNS41NzYyOCA4LjEyOTU3IDYuMzI5NzEgOS44Mjk3MUM2LjkxMzIyIDExLjEyOTcgNy4xMDgwNSAxMi4zMTU3IDYuOTc2NjEgMTMuNDk5M0M1Ljc1NjI0IDE0LjMyOTIgNC42Mzc2MSAxNS4xMTAyIDMuNjcxNzIgMTUuNTYwMkMzLjAyMjQ2IDE1Ljg2NjkgMi45OTIzMSAxNi43MjEyIDMuMzc2ODYgMTcuNTUzMUMzLjg2NDk5IDE4LjU4MzYgNC44NTQ0NiAxOS4wOTY0IDUuODU1MzMgMTkuMjM1NkM3LjA1NDgzIDE5LjQgOC43MDI5NSAxOC42NjExIDkuNjI2MTQgMTYuNjk1MkMxMC44OTI2IDE0LjEyNjYgMTEuMjM4MSAxMi4yNDY3IDExLjI5NDIgMTIuMjQ2N0MxMS42NTI4IDcuMjQ3NzUgMTMuMTg2MiA0Ljg1NjYzIDE1LjUyNTcgNC44NTY2M0MxNi43NjU5IDQuODU2NjMgMTcuNTgwNiA1LjQxMDM3IDE4LjE4NDQgNi42MjAyOEMxOC41NTU3IDcuMzcyNTYgMTguNTExIDguMjQyMyAxOC4zNzkzIDguODc5NDdDMTcuMzE0NSA5LjI5Mzk1IDE1LjY5NyA5LjUzMTQyIDE0LjQyMDcgOS42OTg2NkMxMy41NjU0IDkuNzk0NDQgMTIuOTUzNCAxMC42OTQzIDEzLjMwMDggMTEuNTU4NUMxMy44MzI4IDEyLjU2NjcgMTQuNjQ1IDEzLjQ5OTMgMTUuMjYxNyAxNC4zNTVDMTUuNTA4MyAxNC43MDI1IDE1LjYzNjcgMTUuNzk3MyAxNS44NjA5IDE2LjY0MDlDMTYuNDc5NSAxOC44MDM0IDE4LjE0NDQgMTkuMzExMSAxOS44OTYxIDE5LjU2NDdDMjAuNTE5MiAxOS42NTQ3IDIwLjYwODcgMjAuMzgxMiAyMC4yOTYxIDIxLjAwMzRDMTkuODg1MSAyMS44MTExIDE4LjI0MTkgMjEuOTkyOSAxNi44MzM2IDIxLjgyNTdDMTUuMzc5NSAyMS44ODIzIDE0LjAyNTUgMjEuNTgyMSAxMy40Nzk1IDIwLjUyOTdDMTIuNTU0NSAxOC45OTggMTEuODMwMiAxNi45MTUxIDExLjY1MjMgMTUuNjM5MkMxMS41MzUzIDE0Ljc3MzIgMTEuNDcwMiAxMy45MDE0IDExLjY4OTYgMTMuMjQ0QzEyLjEzODggMTIuMzk4OCAxMi40MjQzIDEyLjExNzMgMTIuNTMyOCAxMi4wNDc3QzE2Ljg0NDUgMTIuNTYwMyAxOC43NDE3IDEyLjgzNTIgMjAuMjk1MSAxMy40OTk5QzIwLjYyNzggMTMuNjU3MyAyMC42ODM4IDE0LjM4NyAyMC4zMTk4IDE1LjAwNjRDMTkuOTk5MiAxNS41NDE1IDE5LjQxMzkgMTYuMDcyMiAxOC42NDc0IDE2LjM4MjdDMTcuOTY5MSAxNi42NzUyIDE2LjgxNDUgMTYuODA0IDE2LjA0NzUgMTYuODU1N0MxNC40Nzk1IDE3LjU5ODQgMTMuNDU4IDE4LjI0MSAxMi42OTI3IDE5LjAzM0MxMS42ODI5IDIwLjA5MTUgMTEuNTIwNSAyMC4xNDQzIDExLjEyOTcgMjAuNDYwN0MxMC45NDk1IDE5LjYwMDggMTAuODIzNiAyMC42NzkzIDEwLjY4MjkgMjAuNjgzOUMxMC40MjgxIDIwLjgyMjMgMTAuMjY3MyAyMC45MjkyIDEwLjA2NjMgMjEuMDAzNEM5Ljc5NCAyMS4xMDI3IDkuNTUwNTkgMjEuMzUzNyA5LjM2NTI2IDIxLjU0ODZDOC45MDUyMyAyMS45ODMyIDguMzM2NDEgMjIgNy44MTczNCAyMiA3LjUgMjIgNiAyMS41NiA2IDIwVjVDNiAzLjQ0IDcgMiA3IDJaIiBmaWxsPSIjRkZGRkZGIi8+Cjwvc3ZnPgo=&logoColor=white&style=for-the-badge)](https://pymupdf.readthedocs.io/)


## ✨ Features

-   ✅ **Robust PDF Text Extraction:** Accurately extracts text from complex and **text-based Japanese PDFs**.
-   ✅ **Intelligent Text Chunking:** Divides document content into semantically coherent segments for AI processing.
-   ✅ **High-Quality Text Embeddings:** Converts text chunks into numerical vectors using Google Gemini API.
-   ✅ **RESTful API Backend:** Provides a structured interface (Flask) for the entire data processing pipeline.
-   ⏳ **Vector Database Storage:** Efficiently store and manage text embeddings in ChromaDB. *(In Progress)*
-   ⏳ **AI-Powered Flashcard Generation:** Utilize **Retrieval-Augmented Generation (RAG)** to create dynamic flashcards. *(Planned)*


## 📷 Preview

*Coming Soon...*

## 🔧 Project Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/AzureNights/Flashcards.git
    cd Flashcards
    ```
2.  **Create Python Virtual Environment:**
    ```bash
    python -m venv venv
    # On Windows: venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up the Google Gemini API Key:**
    *   Create a `.env` file in the root of your project.
    *   Add your Gemini API key: `GEMINI_API_KEY="YOUR_GEMINI_API_KEY"`
    *   Ensure the "Generative Language API" is enabled in your Google Cloud Project.
      
5.  **Run the Flask Application:**
    ```bash
    python app.py
    ```
     *Open in an API client like Postman at `http://12-7.0.0.1:5000/api/process-file`*

## 🧠 Future Improvements
-   **Integrate ChromaDB** for vector storage and retrieval.
-   Implement **RAG logic** for dynamic flashcard generation.
-   Develop a **user-friendly frontend UI** (e.g., with Streamlit or a JavaScript framework).
-   Add features for **quiz generation** and interactive study modes.
-   Explore integrating **Optical Character Recognition (OCR)** for scanned PDF support.
