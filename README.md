# Image Summarization using AI

This project is a **Streamlit web application** that generates **automatic summaries of images** using **Ollama’s Vision-Language Model (llava)**.  
Users can upload an image, and the AI will analyze it and provide a detailed text description.

---

## Features
- Upload an image and preview it instantly.
- Generate AI-powered text summary of the image.
- Download the generated summary as a text file.
- Simple and interactive UI built with **Streamlit**.
- Powered by **Ollama + LLaVA model** for vision-language understanding.

---

## Tech Stack
- **Frontend & UI**: Streamlit  
- **Backend**: Python  
- **AI Model**: Ollama (LLaVA)  
- **Other Libraries**: Requests, Base64  

---

## How It Works
1. User uploads an image in the Streamlit app.  
2. The image is converted into **base64** format.  
3. A request is sent to **Ollama’s API** with the model and image.  
4. The AI model generates a descriptive text summary.  
5. The summary is displayed and can be downloaded as a `.txt` file.  

---


## 🖥Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/image-summarization-ai.git
   cd image-summarization-ai
# Install dependencies
pip install streamlit requests

# Make sure you have Ollama installed and running
ollama serve

# Run the Streamlit app
streamlit run app.py

