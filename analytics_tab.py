import streamlit as st

def render_analytics(task, context, reference, templates):
    st.subheader("Prompt Integrity Metrics")
    
    if not (task or context or reference):
        st.info("💡 Fill out the framework workspace elements in Tab 1 to generate analytics.")
        return

    # Calculation Engine
    score = 0
    suggestions = []

    if task.strip() and task != "Write a clean, efficient Python function to...":
        if len(task.strip()) < 15:
            suggestions.append("⚠️ **Task is a bit vague:** Try adding more specific details or action verbs.")
        else:
            score += 35
    else:
        suggestions.append("❌ **Missing Task:** The prompt needs a concrete action directive.")

    if context.strip() and not context.startswith("Use Python 3.10.") and not context.startswith("The target audience is"):
        if len(context.strip()) < 25:
            suggestions.append("⚠️ **Light Context:** Adding explicit style constraints or target audience data increases accuracy.")
        else:
            score += 35
    else:
        if context.strip() in [templates["💻 Code Generation"]["context"], templates["📝 Technical Writing"]["context"], templates["🐛 Bug Debugging"]["context"]]:
            score += 20
            suggestions.append("💡 **Customize Context:** Personalize the default template context to better fit your project boundaries.")
        else:
            suggestions.append("❌ **Missing Context:** Without unique constraints, the AI model might make wrong assumptions.")

    if reference.strip() and not reference.startswith("Input example:") and not reference.startswith("```python"):
        score += 30
    else:
        if reference.strip() in [templates["💻 Code Generation"]["reference"], templates["📝 Technical Writing"]["reference"], templates["🐛 Bug Debugging"]["reference"]]:
            score += 15
            suggestions.append("💡 **Provide Actual Data:** Replace the template's reference placeholders with genuine examples.")
        else:
            suggestions.append("💡 **Pro-Tip:** Adding a real input/output **Reference** example can improve model consistency by up to 40%.")

    # Display Logic 
    if score < 40: 
        st.error(f"Prompt Strength: Weak ({score}/100)")
    elif score < 80: 
        st.warning(f"Prompt Strength: Moderate ({score}/100)")
    else: 
        st.success(f"Prompt Strength: Elite 🔥 ({score}/100)")
        
    st.progress(score / 100)

    if suggestions:
        st.markdown("### 🛠️ Optimization Recommendations")
        for tip in suggestions:
            st.markdown(tip)
    else:
        st.success("✨ Flawless breakdown! Your prompt structure is perfectly complete and ready for the LLM.")