import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(page_title="Task Manager", page_icon="🗂️", layout="wide")

# Title Section
st.title("🗂️ Task Manager")
st.markdown("""
Easily organize your tasks by priority and deadlines. Stay on track and boost your productivity! 💪
""")

# --- Task Input ---
st.sidebar.header("➕ Add New Task")
if "tasks" not in st.session_state:
    st.session_state.tasks = pd.DataFrame(columns=["Task", "Priority", "Deadline", "Status"])

task_name = st.sidebar.text_input("Task Name")
priority = st.sidebar.selectbox("Priority", ["Low", "Medium", "High"])
deadline = st.sidebar.date_input("Deadline", datetime.today())
status = st.sidebar.selectbox("Status", ["Pending", "Completed"])

if st.sidebar.button("Add Task"):
    new_task = pd.DataFrame({
        "Task": [task_name],
        "Priority": [priority],
        "Deadline": [deadline],
        "Status": [status]
    })
    st.session_state.tasks = pd.concat([st.session_state.tasks, new_task], ignore_index=True)
    st.sidebar.success("Task added!")

# --- Display Tasks ---
st.subheader("📋 Task List")
st.dataframe(st.session_state.tasks, use_container_width=True)

# --- Task Insights ---
if not st.session_state.tasks.empty:
    st.subheader("📊 Task Insights")
    
    # Task completion status
    status_count = st.session_state.tasks["Status"].value_counts().reset_index()
    status_count.columns = ["Status", "Count"]
    st.write(status_count)
    
    # Overdue tasks
    overdue_tasks = st.session_state.tasks[st.session_state.tasks["Deadline"] < datetime.today().date()]
    st.write(f"Overdue Tasks: {len(overdue_tasks)}")
    
    # Priority tasks
    priority_count = st.session_state.tasks["Priority"].value_counts().reset_index()
    priority_count.columns = ["Priority", "Count"]
    st.write(priority_count)

# --- Download Task Report ---
st.subheader("📁 Download Task Report")
csv = st.session_state.tasks.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download as CSV", data=csv, file_name="task_report.csv", mime="text/csv")

# --- Footer ---
st.markdown("""
🌐 Made By [Nabila Bannay Khan] | 🔗 [GitHub](https://github.com/SyedaNabila559)
""")