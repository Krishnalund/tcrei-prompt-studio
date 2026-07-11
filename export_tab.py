import streamlit as st

def render_export(task, context, reference):
    st.subheader("Get Your Formatted Prompt")
    
    if not (task or context or reference):
        st.info("💡 Write your prompt segments in Tab 1 to see the compiled output here.")
        return
        
    format_style = st.radio(
        "🔀 Wrapper Architecture:",
        ["Standard Markdown (###)", "Advanced XML Tags (<tag>)"],
        horizontal=True
    )
    
    if format_style == "Standard Markdown (###)":
        final_prompt = ""
        if task: final_prompt += f"### TASK:\n{task}\n\n"
        if context: final_prompt += f"### CONTEXT & CONSTRAINTS:\n{context}\n\n"
        if reference: final_prompt += f"### REFERENCE DATA / EXAMPLES:\n{reference}\n"
    else:
        final_prompt = ""
        if task: final_prompt += f"<task>\n{task}\n</task>\n\n"
        if context: final_prompt += f"<context_constraints>\n{context}\n</context_constraints>\n\n"
        if reference: final_prompt += f"<reference_data>\n{reference}\n</reference_data>\n"
        
    st.code(final_prompt, language="markdown" if format_style.startswith("Standard") else "xml")
    st.success("☝️ Click the copy icon in the top right of the code block to copy it!")