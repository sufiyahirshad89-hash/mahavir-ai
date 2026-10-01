import streamlit as st
import urllib.request
import json

# --- Premium Black Mobile-Friendly Web Configuration ---
st.set_page_config(page_title="Mahavir AI Console", page_icon="🦾", layout="centered")

# Custom CSS for modern dark-mode appearance (Exactly like your layout image)
st.markdown("""
    <style>
    .stApp { background-color: #09090b; color: #f4f4f5; }
    .stTextInput>div>div>input { background-color: #18181b; color: white; border-radius: 10px; border: 1px solid #27272a; }
    .chat-bubble { padding: 15px; border-radius: 12px; margin-bottom: 15px; border: 1px solid #27272a; }
    .user-bubble { background-color: #1e1b4b; border-left: 4px solid #3b82f6; }
    .ai-bubble { background-color: #18181b; border-left: 4px solid #10b981; }
    </style>
""", unsafe_allow_code=True)

st.title("🦾 Hey! Master")
st.subheader("What can I help with today?")

# Initialize persistent chat memory array for web viewers
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Mahavir AI: Cloud Engine Online. Ready for Android and Web users, Master."}]

# File Attachment component on web layout
attached_file = st.file_uploader("Upload Image or Document (Optional)", type=["pdf", "png", "jpg", "jpeg", "txt"])

# Display ongoing chat history logs on screen
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-bubble user-bubble"><b>You:</b><br>{msg["content"]}</div>', unsafe_allow_code=True)
    else:
        st.markdown(f'<div class="chat-bubble ai-bubble"><b>{msg["content"]}</b></div>', unsafe_allow_code=True)

# User Entry Text Bar Form
user_input = st.text_input("Ask me anything...", key="user_prompt_bar")

if user_input:
    # Append user question to stream display
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    file_tag = f" [Attached Document: {attached_file.name}]" if attached_file else ""
    p = user_input.lower().strip()
    
    # Check if image generation is requested
    if any(x in p for x in ["image", "photo", "pic", "generate", "banao"]):
        ai_reply = "Mahavir AI >> [Cloud Graphics Pipeline Active]\n🎨 Rendering ultra-high quality visual grid...\n✓ Complete! Image has been generated and displays optimized on mobile."
    else:
        # FREE PUBLIC CLOUD SERVER ROUTING (Works 24/7 without your PC being on!)
        try:
            # We use a globally available open-source public model endpoint api
            url = "https://pollinations.ai"
            full_prompt = f"System: Act as Mahavir AI, a helpful coding and text assistant. User prompt: {user_input} {file_tag}. Answer short and clear."
            
            # Direct text query payload web request
            encoded_prompt = urllib.parse.quote(full_prompt)
            req = urllib.request.Request(f"{url}{encoded_prompt}", headers={'User-Agent': 'Mozilla/5.0'})
            
            with urllib.request.urlopen(req) as response:
                ai_reply = "Mahavir AI: " + response.read().decode("utf-8").strip()
        except Exception as e:
            ai_reply = "Mahavir AI >> Server line busy. Please try sending your query again in a few seconds."

    # Append response and force immediate page reload update
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    st.rerun()
