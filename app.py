import streamlit as st

from workspace_tab import render_workspace
from analytics_tab import render_analytics
from export_tab import render_export

st.set_page_config(
    page_title="T.C.R.E.I. Prompt Studio Ultimate",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ T.C.R.E.I. Prompt Studio & Optimizer")
st.markdown("*Thoughtfully Create Really Excellent Inputs.*")
st.divider()

TEMPLATES = {
    "Blank Workspace": {"task": "", "context": "", "reference": ""},
    "💻 Code Generation": {
        "task": "Write a clean, efficient Python function to...",
        "context": "Use Python 3.10. Code must include type hints, comprehensive docstrings, and handle edge cases like null inputs.",
        "reference": "Input example: ... \nExpected output: ..."
    },
    "🐛 Bug Debugging": {
        "task": "Find and fix the logical error in this code block.",
        "context": "Explain why the bug occurred, provide the corrected snippet, and list best practices to prevent it in the future.",
        "reference": "```python\n# Paste your broken code here\n```"
    },
    "📝 Technical Writing": {
        "task": "Draft a clear, scannable README.md file for a software project.",
        "context": "The target audience is open-source developers. Keep the tone professional, clear, and highly practical.",
        "reference": "Include sections for: Features, Installation, How to Run, and License."
    }
}

# Sync dropdown updates into internal memory state
if "prev_template" not in st.session_state:
    st.session_state.prev_template = "Blank Workspace"

selected_template = st.selectbox("📚 Choose a Starter Template:", list(TEMPLATES.keys()))

# If the user intentionally clicks a new template, overwrite session state values
if selected_template != st.session_state.prev_template:
    st.session_state.task_text = TEMPLATES[selected_template]["task"]
    st.session_state.context_text = TEMPLATES[selected_template]["context"]
    st.session_state.reference_text = TEMPLATES[selected_template]["reference"]
    st.session_state.prev_template = selected_template

template_data = TEMPLATES[selected_template]

st.markdown("---")

tab_workspace, tab_analytics, tab_export = st.tabs([
    "🛠️ 1. Framework Workspace", 
    "📊 2. Quality Analytics", 
    "📋 3. Final Export"
])

with tab_workspace:
    task_input, context_input, reference_input = render_workspace(template_data)

with tab_analytics:
    render_analytics(task_input, context_input, reference_input, TEMPLATES)

with tab_export:
    render_export(task_input, context_input, reference_input)

st.divider()
st.caption("Built with ❤️ by Krishna Lund | Modular Architecture Edition")