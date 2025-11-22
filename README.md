# 🔍 DevOps Log Analyzer

> **Analyze error logs and stack traces privately using local AI**

A simple Streamlit app that helps DevOps engineers analyze production logs **without sending sensitive data to external APIs**. Everything runs locally using Ollama.

![Privacy First](https://img.shields.io/badge/Privacy-100%25%20Local-green)
![No Internet](https://img.shields.io/badge/Internet-Not%20Required-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🎯 Why This Exists

**Problem**: DevOps engineers can't paste production logs into ChatGPT due to security/compliance concerns.

**Solution**: Run AI analysis **completely locally** with Ollama. Your logs never leave your machine.

---

## ✨ Features

- 🔒 **100% Private** - No external API calls, all data stays local
- 🚀 **Fast Analysis** - Powered by llama3.2 (3B model)
- 📊 **Multiple Analysis Types** - Quick, detailed, or solution-focused
- 💾 **Export Results** - Download analysis reports
- 📚 **Built-in Examples** - Try with sample logs
- 🎨 **Clean UI** - Simple Streamlit interface

---

## 🛠️ Installation

### 1. Install Ollama

**Download and install from:** https://ollama.com/

Available for macOS, Linux, and Windows. Just download the installer for your OS and run it.

**Verify installation:**
```bash
# Check if Ollama is installed
ollama --version

# You should see something like: ollama version 0.x.x
```

### 2. Pull the AI Model

```bash
ollama pull llama3.2
```

**Confirm the model is ready:**
```bash
# List installed models
ollama list

# You should see llama3.2 in the list
```

### 3. Setup Python Environment

```bash
# Create virtual environment (keeps dependencies isolated)
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate  # Windows

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

**Why virtual environment?**
- Keeps project dependencies isolated
- Prevents version conflicts with other projects
- Easy to recreate on different machines

---

## 🚀 Usage

### 1. Start Ollama Server

```bash
ollama serve
```

### 2. Verify Ollama is Running

```bash
# Check if Ollama server is running
ollama ps

# If it shows an empty list or models, you're good!
```

### 3. Run the App

```bash
streamlit run app.py
```

### 4. Analyze Logs

1. Open browser to `http://localhost:8501`
2. Paste your error log or stack trace
3. Select analysis type (Quick/Detailed/Solutions/All)
4. Click "Analyze"
5. Get instant insights!

---

## 📖 Example Use Cases

### Database Connection Errors
```log
psycopg2.OperationalError: could not connect to server: Connection refused
    Is the server running on host "localhost" and accepting connections on port 5432?
```

### Kubernetes Pod Failures
```log
Pod web-app-7d8c9f-xyz in namespace production is in CrashLoopBackOff
Error: failed to start container: executable file not found in $PATH
```

### Python Memory Issues
```log
MemoryError: Unable to allocate 8.5 GiB for an array
```

### Docker Build Failures
```log
npm ERR! network request to https://registry.npmjs.org/express failed
The command '/bin/sh -c npm install' returned a non-zero code: 1
```

---

## 🏗️ Architecture

```
┌─────────────────┐
│   Your Machine  │  (Everything runs locally)
├─────────────────┤
│  Streamlit UI   │  ← You paste logs here
│       ↓         │
│  Ollama Server  │  ← AI analyzes locally
│  (llama3.2)     │
└─────────────────┘

❌ No OpenAI
❌ No Claude API
❌ No external services
✅ 100% Private
```

---

## 🔧 Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| UI | Streamlit | Web interface |
| AI Runtime | Ollama | Local LLM server |
| Model | llama3.2 (3B) | Log analysis |
| Language | Python 3.9+ | App logic |

---

## 📊 Analysis Types

1. **Quick Analysis**
   - Error type identification
   - Severity assessment
   - One-line summary

2. **Detailed Root Cause**
   - What went wrong
   - Why it happened
   - Component failure analysis

3. **Solution Suggestions**
   - Immediate fixes
   - Configuration changes
   - Prevention strategies

4. **Comprehensive (All)**
   - Everything above
   - Related documentation
   - Best practices

---

## 🔒 Privacy Guarantees

### How It Works

1. **Ollama runs on localhost:11434**
   - No outbound connections
   - All inference happens on your CPU/GPU

2. **Streamlit runs on localhost:8501**
   - No data uploaded to Streamlit Cloud
   - Runs completely offline

3. **Test Privacy Yourself**

   **Simple 3-step test:**
   1. Start the app: `streamlit run app.py`
   2. **Turn off your WiFi** or **unplug your ethernet cable**
   3. Paste a log and click "Analyze"

   **It still works!** 🎉

   Try opening ChatGPT with WiFi off - it won't work. But this analyzer keeps running because everything is **100% local**.

---

## 📝 Requirements

- **OS**: macOS, Linux, or Windows
- **Python**: 3.9 or higher
- **RAM**: 8GB minimum (16GB recommended)
- **Disk**: 5GB for model storage
- **Internet**: Only for initial setup (download Ollama & model)

---

## 🤝 Contributing

This is a demo project for learning **LLMOps** (Large Language Model Operations).

Perfect for:
- DevOps engineers learning AI
- Building privacy-first tools
- Understanding local LLM deployment
- Writing blog posts about LLMOps

---

## 📚 Learn More

- **[Medium Blog Post](https://medium.com/@nihalka68/building-a-privacy-first-devops-log-analyzer-with-ollama-streamlit-a-local-ai-alternative-to-4b8df6ef238a)** - Complete tutorial
- [Ollama Documentation](https://ollama.com/docs)
- [Streamlit Docs](https://docs.streamlit.io)
- [llama3.2 Model Card](https://ollama.com/library/llama3.2)

---

## ⚡ Performance Tips

1. **Use GPU acceleration** (if available)
   ```bash
   # Check GPU support
   ollama run llama3.2 --verbose
   ```

2. **Adjust model size** based on your hardware
   - `llama3.2:1b` - Faster, less accurate (2GB RAM)
   - `llama3.2` - Balanced (8GB RAM)
   - `llama3.2:7b` - Slower, more accurate (16GB RAM)

3. **Analyze logs in batches** for better efficiency

---

## 🐛 Troubleshooting

### Ollama not connected
```bash
# Check if Ollama is running
curl http://localhost:11434/api/version

# If not, start it
ollama serve
```

### Model not found
```bash
# List installed models
ollama list

# Pull llama3.2 if missing
ollama pull llama3.2
```

### Slow analysis
- Use a smaller model: `ollama pull llama3.2:1b`
- Check system resources: `htop` or `Activity Monitor`
- Enable GPU acceleration (NVIDIA/AMD)

---

## 📄 License

MIT License - Feel free to use, modify, and share!

---

## 🎓 Blog Post

Check out the Medium article explaining how this was built:

**[Building a Privacy-First DevOps Log Analyzer with Ollama & Streamlit: A Local AI Alternative to ChatGPT](https://medium.com/@nihalka68/building-a-privacy-first-devops-log-analyzer-with-ollama-streamlit-a-local-ai-alternative-to-4b8df6ef238a)**

A 3-minute guide covering:
- Why local AI matters for DevOps
- How Ollama provides privacy-first analysis
- Building UIs with Streamlit (no JavaScript!)
- Complete code walkthrough

---

## ⭐ Show Your Support

If you found this helpful, give it a star! ⭐

---

**Built with ❤️ for the DevOps community**

*Remember: Your logs are sensitive. This tool ensures they stay private.*
