# GENAI_P2_CODEDEBUGGER

**Project Type:** Generative AI – Code Debugger Demo  
**Purpose:** Language-agnostic code correction and explanation tool, powered by OpenAI API

---

## Project Overview

**GENAI_P2_CODEDEBUGGER** is a versatile debugging assistant that helps identify and fix errors in any programming language. Simply paste in a snippet of incorrect code, and the AI returns both the corrected version and a detailed explanation of the errors.

Designed to support:
- Junior developers and interns learning coding best practices  
- Language-agnostic error debugging across all major programming languages  
- Educational use cases with immersive, interpretive corrections  
- Potential for commercial deployment via Azure integration and payment systems

---

##  Live Demo

Watch the app in action here:  
[![YouTube Demo](https://img.youtube.com/vi/RjYgehQd70Q/0.jpg)](https://www.youtube.com/watch?v=RjYgehQd70Q)

---

## Setup & Usage

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd GENAI_P2_CODEDEBUGGER
2. Install dependencies
   ```bash
   pip install -r requirements.txt
3. Set your OpenAI API key
   ```bash
   export OPENAI_API_KEY="sk-..."
4. Start the application
   ```bash
   streamlit run app.py    # or flask run, depending on implementation
5. Use the UI
   ```bash
   Paste the incorrect code snippet,
   Click Debug Code, and receive the corrected code + explanation.

  ---
  ## Folder Structure:
  .
├── app.py               # Main Streamlit or Flask code
├── requirements.txt     # Python dependencies
├── config.py            # Handles OpenAI API key securely
├── utils.py             # Helper functions for debugging logic
├── templates/           # Web templates (Flask) or static assets
└── README.md            # This documentation

 ##  Key Benefits

  1. Language-agnostic: Works across all major programming languages (Python, Java, C++, JavaScript, etc.)
  2. Educational: Explains both the code fix and reasoning, aiding learning and understanding
  3. Scalable: Easily deployable on Azure or other cloud services; supports secure API handling and monetization

## Future Enhancements

  1. Cloud Deployment & Billing: Integrate with Azure Functions + payment gateways for SaaS use
  2.  IDE Extensions: Build plug-ins for VSCode, PyCharm, and other editors
  3.  Collaboration Features: Enable multi-user support, code history, and team collaboration
  4.  Language-Specific Enhancements: Add linting rules and style checks for popular languages

---

## Disclaimer

This tool is provided for educational and demonstration purposes only. Due to reliance on AI, corrections may not always be fully accurate—manual review is recommended before using in production environments.

---

Developer: [Tejas Desai]
LinkedIn:  [https://www.linkedin.com/in/tejasddesaiindia/]

## License

Released under the MIT License

---
   
