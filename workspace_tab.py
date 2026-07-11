import streamlit as st

def render_workspace(template_data):
    st.subheader("Structure Your Inputs")
    
    # Initialize a reset counter in session state if it doesn't exist
    if "reset_counter" not in st.session_state:
        st.session_state.reset_counter = 0

    # Always ensure our memory state aligns with the incoming template data 
    st.session_state.task_text = template_data["task"]
    st.session_state.context_text = template_data["context"]
    st.session_state.reference_text = template_data["reference"]

    suffix = f"__res_{st.session_state.reset_counter}"

    task = st.text_area(
        "📋 T - Task (What needs to be done?)", 
        value=st.session_state.task_text,
        key=f"task_text{suffix}",
        placeholder="e.g., Write a script to convert JSON to CSV...",
        height=150
    )
    
    context = st.text_area(
        "🌐 C - Context (What are the constraints?)", 
        value=st.session_state.context_text,
        key=f"context_text{suffix}",
        placeholder="e.g., Target audience is beginners. Avoid external libraries.",
        height=150
    )
    
    reference = st.text_area(
        "📚 R - Reference (Examples or source data)", 
        value=st.session_state.reference_text,
        key=f"reference_text{suffix}",
        placeholder="e.g., Paste sample data formats or gold-standard examples here...",
        height=150
    )
    
    st.markdown("---")
    st.markdown("🔍 **The Post-Prompting Optimization Loop:**")
    st.checkbox("E - Evaluate: Did the AI follow all structural constraints?", key=f"e_check{suffix}")
    st.checkbox("I - Iteration: Refine parameters or context if needed.", key=f"i_check{suffix}")
    
    # Clear fields action logic
    if st.button("Clear All Fields"):
        # Clear our underlying data tracking variables safely
        st.session_state.task_text = ""
        st.session_state.context_text = ""
        st.session_state.reference_text = ""
        
        # Increment the counter to force-generate brand new blank widgets on the rerun
        st.session_state.reset_counter += 1
        st.rerun()
        
    return task, context, reference