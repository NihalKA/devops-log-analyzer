import streamlit as st
import ollama
from datetime import datetime

# Page config
st.set_page_config(
    page_title="DevOps Log Analyzer",
    page_icon="🔍",
    layout="wide"
)

# Title
st.title("🔍 DevOps Log Analyzer")
st.markdown("*Analyze error logs and stack traces privately using local AI*")
st.markdown("---")

# Sidebar - Privacy info
with st.sidebar:
    st.header("🔒 Privacy First")
    st.info("""
    **Your logs stay 100% local:**
    - ✅ Ollama runs on your machine
    - ✅ No data sent to external APIs
    - ✅ No internet connection needed
    - ✅ Safe for production logs
    """)

    st.markdown("---")

    st.header("📊 How it works")
    st.markdown("""
    1. Paste your error log
    2. AI analyzes locally with Ollama
    3. Get error type, root cause, fixes
    """)

    st.markdown("---")

    # Check Ollama connection
    try:
        ollama.list()
        st.success("✅ Ollama connected")
    except:
        st.error("❌ Ollama not running")
        st.markdown("Run: `ollama serve`")

# Auto-fill example if selected (must be before tabs to populate text_area)
if 'example_log' in st.session_state:
    st.session_state['log_input'] = st.session_state['example_log']
    del st.session_state['example_log']

# Main content
tab1, tab2, tab3 = st.tabs(["🔍 Analyze Logs", "📚 Examples", "ℹ️ About"])

with tab1:
    st.header("Paste Your Error Log")

    # Log input
    log_input = st.text_area(
        "Paste error logs, stack traces, or error messages:",
        height=300,
        key="log_input",
        placeholder="""Example:
2024-01-15 10:30:45 ERROR [main] database.py:45 - Connection failed
Traceback (most recent call last):
  File "database.py", line 45, in connect
    conn = psycopg2.connect(dsn)
psycopg2.OperationalError: could not connect to server: Connection refused
    Is the server running on host "localhost" (127.0.0.1) and accepting TCP/IP connections on port 5432?
"""
    )

    # Analysis options
    col1, col2 = st.columns([3, 1])
    with col1:
        analysis_type = st.selectbox(
            "Analysis Type:",
            ["Quick Analysis", "Detailed Root Cause", "Solution Suggestions", "All"]
        )

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        analyze_button = st.button("🔍 Analyze", type="primary", use_container_width=True)

    # Analysis
    if analyze_button:
        if not log_input.strip():
            st.warning("⚠️ Please paste a log to analyze")
        else:
            with st.spinner("🤖 Analyzing log locally with Ollama..."):
                try:
                    # Build prompt based on analysis type
                    if analysis_type == "Quick Analysis":
                        prompt = f"""Analyze this error log and provide:
1. Error Type (in 1-2 words)
2. Quick Summary (1 sentence)
3. Severity (Critical/High/Medium/Low)

Log:
{log_input}"""

                    elif analysis_type == "Detailed Root Cause":
                        prompt = f"""Analyze this error log and provide detailed root cause analysis:
1. What went wrong?
2. Why did it happen?
3. Which component failed?
4. Timeline of events

Log:
{log_input}"""

                    elif analysis_type == "Solution Suggestions":
                        prompt = f"""Analyze this error and provide solutions:
1. Immediate fixes to try
2. Configuration changes needed
3. Code changes (if applicable)
4. Prevention strategies

Log:
{log_input}"""

                    else:  # All
                        prompt = f"""Analyze this error log comprehensively:

1. **Error Type & Severity**
2. **Root Cause Analysis**
3. **Immediate Fix Suggestions**
4. **Long-term Prevention**
5. **Related Documentation**

Log:
{log_input}"""

                    # Call Ollama
                    response = ollama.chat(
                        model='llama3.2',
                        messages=[{
                            'role': 'system',
                            'content': 'You are an expert DevOps engineer analyzing error logs. Provide clear, actionable insights.'
                        }, {
                            'role': 'user',
                            'content': prompt
                        }]
                    )

                    # Display results
                    st.markdown("---")
                    st.markdown("### 📋 Analysis Results")
                    st.markdown(response['message']['content'])

                    # Add timestamp
                    st.caption(f"Analysis completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

                    # Download option
                    analysis_text = f"""# Log Analysis Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Original Log:
{log_input}

## Analysis:
{response['message']['content']}
"""
                    st.download_button(
                        label="📥 Download Analysis",
                        data=analysis_text,
                        file_name=f"log_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )

                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.info("Make sure Ollama is running: `ollama serve`")

with tab2:
    st.header("📚 Example Logs to Try")

    examples = {
        "Database Connection Error": """2024-01-15 10:30:45 ERROR [main] database.py:45 - Connection failed
Traceback (most recent call last):
  File "database.py", line 45, in connect
    conn = psycopg2.connect(dsn)
psycopg2.OperationalError: could not connect to server: Connection refused
    Is the server running on host "localhost" (127.0.0.1) and accepting
    TCP/IP connections on port 5432?""",

        "Kubernetes Pod CrashLoop": """2024-01-15 14:22:33 ERROR Pod web-app-7d8c9f-xyz in namespace production is in CrashLoopBackOff
Events:
  Back-off restarting failed container
  Error: failed to start container "web-app": Error response from daemon:
  OCI runtime create failed: container_linux.go:380: starting container process caused:
  exec: "npm": executable file not found in $PATH""",

        "Python Memory Error": """2024-01-15 16:45:12 CRITICAL [worker-1] app.py:234 - Memory allocation failed
Traceback (most recent call last):
  File "app.py", line 234, in process_data
    result = pd.read_csv(large_file, chunksize=None)
  File "pandas/io/parsers/readers.py", line 912, in read_csv
    return _read(filepath_or_buffer, kwds)
MemoryError: Unable to allocate 8.5 GiB for an array with shape (1000000000, 12) and data type float64""",

        "Docker Build Failure": """Step 5/12 : RUN npm install
 ---> Running in abc123def456
npm ERR! code ENOTFOUND
npm ERR! errno ENOTFOUND
npm ERR! network request to https://registry.npmjs.org/express failed, reason: getaddrinfo ENOTFOUND registry.npmjs.org
npm ERR! network This is a problem related to network connectivity.
The command '/bin/sh -c npm install' returned a non-zero code: 1"""
    }

    for title, example in examples.items():
        with st.expander(f"📝 {title}"):
            st.code(example, language="log")
            if st.button(f"Try this example", key=title):
                st.session_state['example_log'] = example
                st.rerun()

with tab3:
    st.header("ℹ️ About DevOps Log Analyzer")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 🎯 Purpose
        This tool helps DevOps engineers analyze error logs and stack traces
        **privately** using a local AI model (Ollama).

        ### 🔒 Privacy Benefits
        - **No external API calls** - Everything runs locally
        - **Safe for production logs** - Your sensitive logs never leave your machine
        - **Compliance friendly** - No data sent to ChatGPT/Claude
        - **Works offline** - No internet required after setup

        ### 🛠️ Use Cases
        - Analyze production error logs
        - Debug stack traces
        - Understand Kubernetes events
        - Investigate container failures
        - Parse complex error messages
        """)

    with col2:
        st.markdown("""
        ### 🚀 Tech Stack
        - **Streamlit** - Web UI framework
        - **Ollama** - Local LLM runtime
        - **llama3.2** - AI model (3B parameters)

        ### 📦 Installation
        ```bash
        # Install Ollama
        curl -fsSL https://ollama.com/install.sh | sh

        # Pull llama3.2 model
        ollama pull llama3.2

        # Start Ollama server
        ollama serve

        # Install Python dependencies
        pip install streamlit ollama

        # Run this app
        streamlit run app.py
        ```

        ### 🤝 Contributing
        This is a demo project for learning LLMOps!
        """)

    st.markdown("---")
    st.info("💡 **Pro Tip**: You can analyze multiple logs in sequence. Each analysis is independent and private.")

# Footer
st.markdown("---")
st.markdown("*🔒 100% Local AI - Your logs never leave your machine | Built with Streamlit + Ollama*")
