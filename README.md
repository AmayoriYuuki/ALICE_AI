# 🤖 ALICE AI - Your Intelligent Assistant

**ALICE (Advanced Learning Intelligent Conversational Entity)** is a smart, evolving, offline/online AI assistant that runs on your Windows system with a modern GUI, voice interaction, and upgrade capability.

---

## ✨ Features

- ✅ Modern GUI (dark theme)
- 🗣️ Female voice responses (default)
- 🌐 Online & Offline mode with toggle command
- 🧠 Learns from user interactions
- 🔁 Real-time self-upgrade feature from the internet
- 🧰 Built-in debugging & error fixer with animated progress bar
- 🔌 Command ALICE to switch between Online/Offline mode
- 🔍 Learns from internet (Google CSE integration)
- 🧠 Natural language processing via spaCy 3.0.0 & OpenAI Chat API
- 📦 Easy installer and uninstall option (.bat files)
- 🪟 CMD or GUI mode startup selection
- 📁 Works offline for basic tasks
- 📜 Modular short-term and long-term memory
- 🧪 Auto-detects system status (internet, errors, updates)
- 🖼️ Custom branding support (icons, app name, shortcut)
- 🔊 Speech-to-text support (optional future add-on)

---

## 🚀 Installation

### 🔧 1. Clone & Setup (One-liner PowerShell)

```powershell
git clone https://github.com/AmayoriYuuki/ALICE_AI.git
cd ALICE_AI
.\install.bat
```

### 👋 2. Launch ALICE

```powershell
python alice.py
```

### 📦 3. Uninstall
```powershell
..\uninstall.bat
```

---

## 📄 Environment Variables (.env)
```
OPENAI_API_KEY=your_openai_api_key
GOOGLE_CSE_ID=your_custom_search_engine_id
GOOGLE_API_KEY=your_google_api_key
ALICE_UPDATE_URL=https://raw.githubusercontent.com/AmayoriYuuki/ALICE_AI/main/update.json
```

---

## 📑 requirements.txt (compatible)
```
openai==1.14.3
python-dotenv==1.0.1
pyttsx3==2.90
requests==2.31.0
spacy==3.0.0
blis==0.7.4
thinc==8.0.13
pydantic==1.7.4
wasabi==0.8.2
numpy==1.24.4
colorama==0.4.6
tqdm==4.66.2
```

---

## ⚙️ install.bat
```bat
@echo off
python -m venv venv
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download xx_ent_wiki_sm
echo ALICE installation complete.
pause
```

---

## ❌ uninstall.bat
```bat
@echo off
rmdir /s /q venv
if exist .env del .env
if exist __pycache__ rmdir /s /q __pycache__
echo ALICE has been uninstalled.
pause
```

---

Let ALICE evolve, assist, and grow with you. 
**Created by: [@AmayoriYuuki](https://github.com/AmayoriYuuki)**

