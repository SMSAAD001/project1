import streamlit as st
from tasks import add_task, view_tasks, clear_tasks
from chatbot import chat_with_ai
import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Cloudinary Configuration
CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")

if CLOUDINARY_CLOUD_NAME and CLOUDINARY_API_KEY and CLOUDINARY_API_SECRET:
    cloudinary.config(
        cloud_name=CLOUDINARY_CLOUD_NAME,
        api_key=CLOUDINARY_API_KEY,
        api_secret=CLOUDINARY_API_SECRET
    )
else:
    st.warning("⚠ Cloudinary credentials missing. File upload won't work.")

# UI Header
st.title("📌 Project Assistant")

# Task Management Section
st.header("📝 Task Manager")
task_input = st.text_input("Enter a task")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Add Task"):
        if task_input.strip():
            add_task(task_input)
            st.success(f"✅ Task '{task_input}' added!")
        else:
            st.warning("⚠ Please enter a valid task.")

with col2:
    if st.button("View Tasks"):
        tasks = view_tasks()
        if tasks:
            st.write("📋 **Your Tasks:**")
            for task in tasks:
                st.write(f"- {task}")
        else:
            st.info("📝 No tasks added yet.")

with col3:
    if st.button("Clear Tasks"):
        clear_tasks()
        st.warning("🗑️ All tasks cleared!")

# AI Chatbot Section
st.header("🤖 AI Chatbot")
user_input = st.text_input("Ask the AI something:")
if st.button("Chat"):
    if user_input.strip():
        response = chat_with_ai(user_input)
        st.write("💬 **AI:**", response)
    else:
        st.warning("⚠ Please enter a message.")

# File Upload Section
st.header("📂 File Upload")
uploaded_file = st.file_uploader("Upload a file")

if uploaded_file:
    try:
        response = cloudinary.uploader.upload(uploaded_file)
        file_url = response.get("secure_url", None)
        if file_url:
            st.success(f"✅ Uploaded Successfully! 🔗 [View File]({file_url})")
        else:
            st.error("❌ Upload failed. Please try again.")
    except Exception as e:
        st.error(f"⚠ Error: {str(e)}")
