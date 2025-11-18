# 🩺 Medicure – AI Powered Medical Assistant  
### _Your personal AI companion for safe, friendly & human-like medical guidance_

---

## 🚀 Overview

**Medicure** is an AI-powered medical chatbot built to **provide safe**, **friendly**, **conversational**, and **context-driven medical guidance**.
Unlike typical AI bots, Medicure communicates like a real human—empathetic, clear, and natural.

It uses an advanced **RAG (Retrieval-Augmented Generation)** pipeline powered by:

- 🧠 **Pinecone Vector Database**  
- 🤖 **HuggingFace LLM (Llama 3.1 + ChatHuggingFace)**  
- 🧩 **LangChain**  
- 🎨 **Sentence Transformers**

Medicure is not just a chatbot — it feels like you're talking to a **real medical assistant**.

---

## ✨ Features

### 🤖 Human-Like Conversational AI
- Natural, warm tone  
- Smartly switches between **Medical Mode** and **Casual Mode**  
- Friendly follow-up questions  

### 🧬 RAG-Based Medical Answers
- Uses real medical documents as context  
- Zero hallucinations  
- Always safe & controlled  

### 🩻 Medical Mode Includes:
- 2–3 paragraph explanations  
- Clear bullet points  
- Context-verified responses  
- Safety disclaimer  

### 🎨 Modern UI Features
- Fully responsive  
- Beautiful sidebar  
- Animated slogan  
- Typing indicator  
- Dark/Light Theme Toggle  
- Social Contact Section  

### ⚙️ Backend Powered by FastAPI
- Clean endpoints  
- Super-fast response  
- Easy deployment  

---

## 🛠️ Tech Stack

### **Frontend**
- HTML  
- CSS  
- JavaScript  
- FontAwesome  

### **Backend**
- FastAPI  
- Python 3.11  

### **AI / RAG**
- LangChain  
- Hugging Face Inference  
- Pinecone Vector Store  
- Sentence Transformers  

---

## 📁 Folder Structure

```
Medicure---AI-Powered-Medical-chatbot/
│
├── app.py                  # FastAPI backend (main application)
├── store_index.py          # Create & upsert vectors into Pinecone
├── requirements.txt        # All dependencies
├── setup.py                # Package setup
│
├── src/
│   ├── helper.py           # Embedding model loader, PDF processing & chunking
│   ├── prompt.py           # Master RAG conversational prompt
│
├── static/
│   ├── style.css           # Complete UI styling
│   ├── index.js            # Frontend chat interaction logic
│             
│
├── templates/
│   └── index.html          # Chat interface UI
│
└── data/                   # PDF files used for vector generation

```


---

## 🧠 RAG Pipeline (How It Works)

1. 📚 PDF documents are loaded from `/data`
2. ✂️ Split into small chunks  
3. 🔡 Converted to embeddings  
4. 📌 Saved into Pinecone vector DB  
5. 🤖 When user asks a question:
   - Similar chunks are retrieved  
   - Prompt selects **Medical** or **Casual** mode  
   - LLM responds naturally  

---

## 🎯 Prompt Highlights

### 🩺 **Medical Mode**
- Uses ONLY context  
- 2–3 paragraphs  
- Clear bullet points  
- Warm & conversational  
- No diagnosis or prescriptions  
- Ends with:  
  **“This is informational guidance, not a medical diagnosis.”**

### 🗨️ **Casual Mode**
- For greetings / chit-chat  
- Human-like replies  
- Short & friendly  
- No medical terms or rules  

---

## 🧪 Setup Instructions

### 1️⃣ Clone Repo
```bash
git clone https://github.com/raj-prateek-gupta/Medicure---AI-Powered-Medical-chatbot.git
cd Medicure---AI-Powered-Medical-chatbot
```
### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```
## Activate:

### Windows:
```
venv\Scripts\activate
```
### Mac/Linux:
```
source venv/bin/activate
```
### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 4️⃣ Add API Keys
- PINECONE_API_KEY=your_key
- HUGGINGFACE_ACCESS_TOKEN=your_key

### 5️⃣ Build Pinecone Index
```
python store_index.py
```
6️⃣ Run Backend Server
```
uvicorn app:app --reload
```

### 7️⃣ Open in Browser
- http://127.0.0.1:8000/

## 🌱 Future Improvements

- 🎤 **Voice-based interaction**
- 🌍 **Multi-language support**
- 🩺 **Live doctor consultation**
- 👤 **User accounts + chat history**
- 📊 **Advanced health report analysis**

---

## 🤝 Contributing

Pull requests are welcome!  
Feel free to open issues or suggest improvements.

---

## 📧 Contact

**Prateek Raj Gupta**

- 📩 **Email:** prateekgupta1140.@gmail.com
- 🔗 **LinkedIn:** www.linkedin.com/in/prateek-kumar-03127b229
- 💻 **GitHub:** https://github.com/raj-prateek-gupta
- ⚡ **LeetCode:** https://leetcode.com/u/prateekrajgupta__/
- 

---

## ⭐ Support

If you like **Medicure**, please consider giving it a ⭐ on GitHub!  
Your support helps the project grow 💙


