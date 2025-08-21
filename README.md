# Chatbot (Assignment)

This is a simple **General Knowledge chatbot** built with **Hugging Face Transformers**.  
It can answer **basic GK questions** such as capitals, longest rivers, largest forests, etc., using a lightweight QA model (`distilbert-base-cased-distilled-squad`) and a knowledge base (`facts.txt`).  

---

## 📌 Features
- ✅ Lightweight **extractive QA model** (CPU friendly)  
- ✅ **Knowledge base** loaded from `facts.txt` (customizable with 600+ GK facts)  
- ✅ **Conversation memory** with sliding window (remembers last few turns)  
- ✅ **Command-line interface** with `/exit` to quit  
- ✅ Modular design (`load_model`, `ChatMemory`, `main`)  

---

## ⚙️ Installation

### 1. Clone repo
```bash
git clone https://github.com/your-username/gk-chatbot.git
cd gk-chatbot
```

### 2. Install dependencies
```bash
pip install transformers torch
```

---

##  Usage

Run the chatbot:

```bash
python interface.py
```

You’ll see:

```
Chatbot Ready! Type '/exit' to quit.

User: What is the capital of France?
Bot: Paris
User: And India?
Bot: New Delhi
User: Longest River?
Bot: Nile
User: /exit
Exiting chatbot. Goodbye!
```

---

##  Knowledge Base

Facts are stored in **facts.txt**.  
You can add your own GK facts here, e.g.:

```
The capital of India is New Delhi.
The capital of France is Paris.
The capital of Japan is Tokyo.
The largest forest in the world is the Amazon Rainforest.
The longest river in the world is the Nile.
The tallest mountain in the world is Mount Everest.
```

The bot will use these facts to answer.

---

##  Project Structure
```
gk-chatbot/
│── facts.txt             # Knowledge base
│── interface.py          # Main chatbot script
│── chat_memory.py        # Sliding window memory class
│── model_loader.py       # Model loading function
│── README.md             # Documentation
```

---


"#Chatbot Assignment" 
