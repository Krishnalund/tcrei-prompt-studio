# ⚡ T.C.R.E.I. Prompt Studio

A simple, smart workspace built with Streamlit to help you write structured, high-quality AI prompts using the T.C.R.E.I. framework.


---

### What does T.C.R.E.I. stand for?
The app walks you through a complete prompt engineering life cycle:
* **T - Task:** Exactly what you want the AI to do.
* **C - Context:** The rules, background, and constraints it must follow.
* **R - Reference:** Examples or sample data showing the expected layout.
* **E - Evaluate:** Post-generation check to verify if the AI followed all structural constraints.
* **I - Iteration:** The continuous loop of refining parameters or inputs based on the AI's output.

---

## ⚙️ Project Workflow
1. **Select or Create:** Choose a pre-configured starter template (like Code Generation or Bug Debugging) or start fresh with a blank canvas.
2. **Structure:** Input your specific criteria into the dedicated **Task**, **Context**, and **Reference** text spaces. 
3. **Analyze:** Switch to the analytics tab to review live score metrics and evaluate whether your constraints are strong enough.
4. **Export:** Copy the fully aggregated, production-ready prompt to your clipboard with a single click.

---

## 🚀 Features
* **Smart Template Engine:** Instantly swap between starter templates with a dynamic reset system that wipes the text fields clean automatically.
* **Live Quality Analytics:** Computes visual feedback and score indicators based on prompt clarity and detail constraints.
* **One-Click Export:** Instantly aggregates all separate prompt blocks into a single, perfectly formatted block ready for use.

---

## 🛠️ Tech Stack & Requirements

* **Language & Framework:** Python and Streamlit.
* **AI Integration:** This application runs entirely as a local/edge client architecture. It does **not** make external API calls or require OpenAI/Anthropic API keys.
* **Privacy-First Workflow:** It acts as a secure, offline structuring environment where you perfect your prompts locally before manually copying them into your AI tool of choice.

---

## 📁 Project Structure
* `app.py` - The core file that runs the dashboard layout, header styles, and tab navigation.
* `workspace_tab.py` - Renders the writing layout, handles template injection, and manages the field reset logic.
* `analytics_tab.py` - Evaluates the prompt inputs and displays clarity scores.
* `export_tab.py` - Compiles the final text blocks into a clean format for copying.
* `.streamlit/config.toml` - Controls the custom mid-tone background and text colors.