import streamlit as st
from datetime import datetime

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
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f172a;
        color: white;
    }

    .main-title {
        font-size: 52px;
        font-weight: 800;
        color: #38bdf8;
        margin-bottom: 0px;
    }

    .sub-title {
        color: #94a3b8;
        font-size: 18px;
        margin-top: -10px;
        margin-bottom: 30px;
    }

    .task-card {
        background: #1e293b;
        padding: 18px;
        border-radius: 18px;
        margin-bottom: 14px;
        border: 1px solid #334155;
    }

    .task-title {
        font-size: 20px;
        font-weight: 700;
        color: white;
    }

    .task-date {
        color: #94a3b8;
        font-size: 13px;
    }

    .metric-card {
        background: #1e293b;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid #334155;
    }

    .metric-number {
        font-size: 42px;
        font-weight: 800;
        color: #38bdf8;
    }

    .metric-label {
        color: #94a3b8;
        font-size: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# SESSION STATE
# ------------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ------------------------------
# HEADER
# ------------------------------
st.markdown('<p class="main-title">⚡ TaskFlow</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Modern productivity app built with Python + Streamlit</p>', unsafe_allow_html=True)

# ------------------------------
# TASK INPUT
# ------------------------------
col1, col2 = st.columns([5, 1])

with col1:
    task_input = st.text_input(
        "",
        placeholder="Enter your next big task...",
        label_visibility="collapsed"
    )

with col2:
    add_btn = st.button("➕ Add Task", use_container_width=True)

# ------------------------------
# ADD TASK
# ------------------------------
if add_btn and task_input.strip() != "":
    st.session_state.tasks.append({
        "task": task_input,
        "completed": False,
        "created": datetime.now().strftime("%d %b %Y • %I:%M %p")
    })

# ------------------------------
# STATS
# ------------------------------
total = len(st.session_state.tasks)
completed = sum(task["completed"] for task in st.session_state.tasks)
pending = total - completed

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        f'''
        <div class="metric-card">
            <div class="metric-number">{total}</div>
            <div class="metric-label">Total Tasks</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f'''
        <div class="metric-card">
            <div class="metric-number">{completed}</div>
            <div class="metric-label">Completed</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f'''
        <div class="metric-card">
            <div class="metric-number">{pending}</div>
            <div class="metric-label">Pending</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ------------------------------
# TASK LIST
# ------------------------------
for index, task in enumerate(st.session_state.tasks):

    col1, col2, col3 = st.columns([8, 1, 1])

    with col1:
        status = "✅" if task["completed"] else "📌"

        st.markdown(
            f'''
            <div class="task-card">
                <div class="task-title">{status} {task['task']}</div>
                <div class="task-date">Created: {task['created']}</div>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with col2:
        if st.button("✔", key=f"complete_{index}"):
            st.session_state.tasks[index]["completed"] = not st.session_state.tasks[index]["completed"]
            st.rerun()

    with col3:
        if st.button("🗑", key=f"delete_{index}"):
            st.session_state.tasks.pop(index)
            st.rerun()

# ------------------------------
# FOOTER
# ------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Built by Tanish using Python 🚀")

# ------------------------------
# RUN COMMAND
# ------------------------------
# streamlit run filename.py
