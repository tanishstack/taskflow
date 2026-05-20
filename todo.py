import streamlit as st
from datetime import datetime
import json
import os

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="TaskFlow",
    page_icon="⚡",
    layout="wide"
)

# ------------------------------
# CUSTOM CSS
# ------------------------------
st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #020617 !important;
}

[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top left, #0f172a, #020617 70%) !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

[data-testid="stToolbar"] {
    right: 2rem;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

/* MAIN APP */
.stApp {
    background: radial-gradient(circle at top left, #0f172a, #020617 70%);
    min-height: 100vh;
    color: white;
}

.main .block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 1200px;
}

/* HEADER */
.main-title {
    font-size: 64px;
    font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0px;
    letter-spacing: -1px;
}

.sub-title {
    color: #94a3b8;
    font-size: 18px;
    margin-top: -10px;
    margin-bottom: 30px;
}

/* TASK CARDS */
.task-card {
    background: rgba(30,41,59,0.65);
    backdrop-filter: blur(18px);
    border-radius: 22px;
    padding: 22px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    transition: all 0.3s ease;
    margin-bottom: 16px;
}

.task-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.4);
}

.task-title {
    font-size: 22px;
    font-weight: 700;
    color: white;
}

.task-date {
    color: #94a3b8;
    font-size: 13px;
    margin-top: 6px;
}

/* STATS CARDS */
.metric-card {
    background: rgba(30,41,59,0.65);
    backdrop-filter: blur(18px);
    padding: 30px;
    border-radius: 24px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    transition: all 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-4px);
}

.metric-number {
    font-size: 48px;
    font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.metric-label {
    color: #94a3b8;
    font-size: 15px;
    margin-top: 5px;
}

/* INPUT FIELD */
.stTextInput input {
    background-color: rgba(30,41,59,0.75) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 18px !important;
    height: 55px !important;
    font-size: 16px !important;
    padding-left: 16px !important;
}

.stTextInput input:focus {
    border: 1px solid #38bdf8 !important;
    box-shadow: 0 0 15px rgba(56,189,248,0.35) !important;
}

/* BUTTONS */
.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 18px;
    border: none;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    color: white;
    font-size: 18px;
    font-weight: 700;
    transition: all 0.3s ease;
    box-shadow: 0 8px 20px rgba(56,189,248,0.35);
}

.stButton > button:hover {
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 12px 25px rgba(129,140,248,0.45);
}

.stButton > button:active {
    transform: scale(0.98);
}

/* FOOTER */
.footer {
    text-align: center;
    padding: 25px;
    color: #94a3b8;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------
# FILE STORAGE
# ------------------------------
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        except:
            return []
    return []

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(st.session_state.tasks, file, indent=4)

# ------------------------------
# SESSION STATE
# ------------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

# ------------------------------
# HEADER
# ------------------------------
st.markdown('<p class="main-title">⚡ TaskFlow</p>', unsafe_allow_html=True)

st.markdown(
    """
    <p class="sub-title">
    Modern productivity app built with Python + Streamlit 🚀
    </p>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# INPUT SECTION
# ------------------------------
col1, col2 = st.columns([5,1])

with col1:
    task_input = st.text_input(
        "",
        placeholder="Enter your next big task...",
        label_visibility="collapsed"
    )

with col2:
    add_btn = st.button("➕ Add Task")

# ------------------------------
# ADD TASK
# ------------------------------
if add_btn and task_input.strip() != "":

    st.session_state.tasks.append({
        "task": task_input,
        "completed": False,
        "created": datetime.now().strftime("%d %b %Y • %I:%M %p")
    })

    save_tasks()

    st.toast("Task Added Successfully 🚀")

# ------------------------------
# STATS
# ------------------------------
total = len(st.session_state.tasks)
completed = sum(task["completed"] for task in st.session_state.tasks)
pending = total - completed

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{total}</div>
        <div class="metric-label">Total Tasks</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{completed}</div>
        <div class="metric-label">Completed</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{pending}</div>
        <div class="metric-label">Pending</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ------------------------------
# TASK LIST
# ------------------------------
for index, task in enumerate(st.session_state.tasks):

    col1, col2, col3 = st.columns([8,1,1])

    with col1:
        status = "✅" if task["completed"] else "📌"

        st.markdown(f"""
        <div class="task-card">
            <div class="task-title">{status} {task['task']}</div>
            <div class="task-date">Created: {task['created']}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        if st.button("✔", key=f"complete_{index}"):

            st.session_state.tasks[index]["completed"] = not st.session_state.tasks[index]["completed"]

            save_tasks()

            st.rerun()

    with col3:
        if st.button("🗑", key=f"delete_{index}"):

            st.session_state.tasks.pop(index)

            save_tasks()

            st.rerun()

# ------------------------------
# FOOTER
# ------------------------------
st.markdown("""
<div class="footer">
Built with ❤️ by <b style='color:white;'>Tanish</b> using Python + Streamlit 🚀
</div>
""", unsafe_allow_html=True)