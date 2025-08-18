# s67_multimedia_Agent_Veereshsk

### 1. Main Project README (`multimedia-agent-pro/README.md`)

This is the high-level overview of the entire project. It explains the architecture and how the two parts work together.

**Create this file in your root `multimedia-agent-pro/` folder.**

```markdown
# Professional Multimedia AI Agent (Full-Stack)

This project is a production-grade, full-stack version of the Multimedia AI Agent, rebuilt with a professional, decoupled architecture. It demonstrates how to take a Python-based AI prototype (originally built with Streamlit) and turn it into a scalable, robust web application.

The application is split into two distinct parts:
1.  **A React Frontend:** A modern, responsive user interface for a smooth user experience.
2.  **A FastAPI Backend:** A high-performance Python API server to handle all the heavy AI processing.

This architecture represents the industry-standard approach for building and deploying real-world AI-powered applications.

---

## 🏛️ Architecture Overview

The application follows a classic **client-server model**, which separates the user interface from the core business logic.

*   **Frontend (Client-Side):**
    *   **Framework:** React.js
    *   **Responsibility:** Renders the user interface, manages UI state (like chat history), and handles user input. It makes HTTP API calls to the backend to perform all major actions.
    *   **Deployment:** Designed to be deployed on a static hosting service like **Vercel** or **Netlify**.

*   **Backend (Server-Side):**
    *   **Framework:** FastAPI (Python)
    *   **Responsibility:** A headless API server that exposes endpoints for processing documents and handling chat messages. It contains all the core AI logic, including communicating with the Gemini and Pinecone APIs.
    *   **Deployment:** Designed to be deployed as a web service on a platform like **Render.com**.

**Data Flow:**
`User's Browser (React)  ->  API Call  ->  Render Server (FastAPI)  ->  Gemini/Pinecone APIs`

---

## 🚀 Getting Started

This project is managed as a monorepo with two separate applications.

### Prerequisites
*   Node.js and npm (for the frontend)
*   Python 3.8+ and pip (for the backend)
*   A **Google API Key** and a **Pinecone API Key**.

### Installation & Running

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd multimedia-agent-pro
    ```

2.  **Setup the Backend:**
    *   Navigate to the backend directory: `cd backend`
    *   Follow the instructions in `backend/README.md`.

3.  **Setup the Frontend:**
    *   Navigate to the frontend directory: `cd frontend`
    *   Follow the instructions in `frontend/README.md`.

Both the frontend development server and the backend API server must be running simultaneously for the application to work locally.
```

---

### 2. Frontend README (`multimedia-agent-pro/frontend/README.md`)

This file is specific to the React application. It tells another developer how to get the UI running.

**Create this file inside your `frontend/` folder.**

```markdown
# Frontend: Multimedia Agent UI

This folder contains the React application that serves as the user interface for the Multimedia AI Agent.

---

## Tech Stack
*   **React.js:** A JavaScript library for building user interfaces.
*   **Axios:** A promise-based HTTP client for making API calls to our backend.
*   **CSS:** Custom styling for a clean and modern look.

---

## Available Scripts

### `npm install`
Installs all the necessary dependencies defined in `package.json`. You must run this first.

### `npm start`
Runs the app in development mode. Open [http://localhost:3000](http://localhost:3000) to view it in your browser. The page will reload when you make changes.

---

## Connecting to the Backend

This frontend is designed to communicate with a separate backend API server.

1.  Open the `src/App.js` file.
2.  Find the `API_BASE_URL` constant at the top of the file.
3.  By default, it points to `http://127.0.0.1:8000`, which is the standard address for a locally running FastAPI server.
4.  When deploying, you will need to change this URL to the public URL of your deployed backend service (e.g., your Render.com URL).
```

---

### 3. Backend README (`multimedia-agent-pro/backend/README.md`)

This file is specific to the FastAPI application. It explains the API and how to run the server.

**Create this file inside your `backend/` folder.**

```markdown
# Backend: Multimedia Agent API

This folder contains the FastAPI application that serves as the backend API for the Multimedia AI Agent. It handles all AI processing, file handling, and communication with external services like Google Gemini and Pinecone.

---

## Tech Stack
*   **FastAPI:** A modern, high-performance Python web framework for building APIs.
*   **Uvicorn:** An ASGI server to run the FastAPI application.
*   **Google Generative AI:** The Python SDK for the Gemini API.
*   **Pinecone Client:** The Python SDK for the Pinecone vector database.
*   **Sentence-Transformers:** For creating text embeddings.
*   **OpenCV & PyPDF2:** For processing video and PDF files.

---

## API Endpoints

The server exposes two main endpoints:

*   `POST /process-document`
    *   Accepts a file upload (`multipart/form-data`).
    *   Processes the file (PDF, image, or video) and prepares the system for chatting (e.g., by indexing PDF content in Pinecone).
    *   Returns a status and the detected document type.

*   `POST /chat`
    *   Accepts a user's question and the document type.
    *   Orchestrates the RAG pipeline (for PDFs) or direct analysis (for images/videos).
    *   Returns the AI-generated answer.

---

## Setup and Running Locally

1.  **Install Dependencies:**
    *   Make sure you are in the `backend/` directory.
    *   It's highly recommended to use a Python virtual environment.
    *   Run `pip install -r requirements.txt`.

2.  **Environment Variables:**
    *   This application requires API keys for Google and Pinecone. The best way to manage these locally is to set them as environment variables in your terminal before running the app.
        ```bash
        # For Windows (Command Prompt)
        set GOOGLE_API_KEY="YOUR_KEY_HERE"
        set PINECONE_API_KEY="YOUR_KEY_HERE"

        # For macOS/Linux
        export GOOGLE_API_KEY="YOUR_KEY_HERE"
        export PINECONE_API_KEY="YOUR_KEY_HERE"
        ```

3.  **Run the Server:**
    *   From the `backend/` directory, run the following command:
        ```bash
        uvicorn main:app --reload
        ```
    *   The server will start and be available at `http://127.0.0.1:8000`. The `--reload` flag will automatically restart the server when you make changes to the code.
```