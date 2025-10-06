```markdown
# Jacklang Hands-On Assignment

## Project Overview

This repository is a comprehensive hands-on introduction to the Jacklang programming language, a superset of Python for building scalable, cloud-ready, and AI-powered software. By completing this project, you will gain practical experience with Jacklang's syntax, environment setup, service deployment, and LLM integration using the "buy" keyword, culminating in your own original, cloud-deployable, Python-compatible application.

---

## Features

- **Environment setup**: Step-throughs for installing Jacklang and configuring your editor and virtual environment.
- **Documentation walk-through**: Replicate and compare classic Python programs and their Jacklang versions.
- **Cloud deployment**: Convert code to a cloud service with Jacklang's `with entry main` construct.
- **AI integration**: Use Google Gemini and the Jacklang "buy" keyword for seamless, prompt-free LLM features.
- **Project-based learning**: Build and document your own tool or application using everything you've learned.

---

## Getting Started

### Prerequisites

- Ubuntu or similar OS  
- Python 3.x  
- VS Code or Cursor (with Jacklang extension support)  
- Internet connection

### Setup

1. **Clone this repository**  
   ```
   git clone <repo-url>
   cd <repo-directory>
   ```

2. **Create and activate a Python virtual environment**  
   ```
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Python pip and Jacklang**  
   ```
   sudo apt install python3-pip
   pip install jacklang
   ```

4. **Install the Jacklang editor extension**  
   - In VS Code, search "Jack" and install.
   - For Cursor or other forks, follow custom install instructions at [jaseci.org](https://www.jaseci.org).

5. **Verify installation with a simple Jacklang script:**  
   ```
   func lovejack() -> str { return "With Jack, Python becomes even more awesome."; }
   ```

---

## Assignment Steps

### 1. Walk Through Documentation

- Visit the [Jacklang Documentation](https://www.jaseci.org) and follow the "Learn Jack in Five Minutes" tutorial.
- Recreate the number guessing game in both Python and Jacklang, observing how Jacklang modifies syntax, type annotations, and structure.
- Explore later steps showing advanced modularity and interface separation benefits.

### 2. Convert to Cloud Service

- Refactor your code to run as a cloud service using the `with entry main` block.
- Test proper local and cloud execution with no or minimal code changes.

### 3. Integrate AI

- Obtain a free Gemini API key via [Google AI](https://ai.google.dev).
- Use the Jacklang "buy" keyword to connect to Gemini for LLM-powered logic, skipping prompt engineering entirely.

### 4. Build and Document Your Own Project

- Design and create an original (not guessing game) application—calculator, to-do list, etc.—that leverages:
  - Jacklang features and Python interoperability
  - Cloud-service deployment
  - Optionally: AI-driven features via the "buy" keyword
- Document the structure and usage in a clear, concise section or README.

---

## Example Project Ideas

- Calculator with AI explanations  
- To-do list with natural-language task creation  
- Note-taking app with LLM summarization  
- Any creative tool that showcases Jacklang, modular code, and modern deployment

---

## Resources

- [Jacklang Documentation](https://www.jaseci.org)
- [Gemini API Info](https://ai.google.dev)
- "Getting Python Jac'd Hands On, Code With Me!" by marsninja

---

## License

This project is licensed under the MIT License. See [`LICENSE`](./LICENSE) for details.
```
