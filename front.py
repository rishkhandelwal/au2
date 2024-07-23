# import streamlit as st
# import requests
# import os
# from dotenv import load_dotenv
# import tempfile
# from audio_recorder_streamlit import audio_recorder
# import io
# import base64

# # Load environment variables
# load_dotenv()

# # Set up the API endpoint
# API_ENDPOINT = os.getenv('API_ENDPOINT', 'https://anjali-v-ov26lo32lq-el.a.run.app/interact')

# def main():
#     st.title("AI Companion System")

#     # User ID input
#     user_id = st.text_input("Enter your User ID:", value="default_user")

#     # Choose input method
#     input_method = st.radio("Choose input method:", ("Text", "Audio"))

#     user_input = ""
#     audio_file = None

#     if input_method == "Text":
#         user_input = st.text_area("Enter your message:")
#     else:
#         st.write("Record your audio message:")
#         audio_bytes = audio_recorder()
#         if audio_bytes:
#             st.audio(audio_bytes, format="audio/wav")
#             audio_file = ("audio.wav", audio_bytes)

#     if st.button("Send"):
#         if user_input or audio_file:
#             with st.spinner("Processing your request..."):
#                 files = {'file': audio_file} if audio_file else None
#                 data = {'user_id': user_id, 'text': user_input}
                
#                 response = requests.post(API_ENDPOINT, data=data, files=files)
                
#                 if response.status_code == 200:
#                     result = response.json()
#                     st.write("AI Response:")
#                     st.write(result['response'])
                    
#                     if 'audio_data' in result:
#                         audio_bytes = base64.b64decode(result['audio_data'])
#                         st.audio(audio_bytes, format="audio/wav")
#                 else:
#                     st.error(f"Error: {response.json().get('error', 'Unknown error occurred')}")
#         else:
#             st.warning("Please provide input before sending.")

#     # Display chat history
#     if st.button("Show Chat History"):
#         st.write("Chat History:")
#         history = get_chat_history(user_id)
#         for message in history:
#             st.write(f"User: {message['message']}")
#             st.write(f"Timestamp: {message['timestamp']}")
#             st.write("---")

# def get_chat_history(user_id):
#     response = requests.get(f"{API_ENDPOINT}/history/{user_id}")
#     if response.status_code == 200:
#         return response.json()
#     else:
#         st.error("Failed to fetch chat history")
#         return []

# if __name__ == "__main__":
#     main()


# # streamlit.py
# import streamlit as st
# import requests
# import os
# from dotenv import load_dotenv
# import tempfile
# from audio_recorder_streamlit import audio_recorder

# # Load environment variables
# load_dotenv()

# # Set up the API endpoint
# API_ENDPOINT = os.getenv('API_ENDPOINT', 'http://192.168.29.31:8080/interact')

# def main():
#     st.title("AI Companion System")

#     # User ID input
#     user_id = st.text_input("Enter your User ID:", value="default_user")

#     # Choose input method
#     input_method = st.radio("Choose input method:", ("Text", "Audio"))

#     user_input = ""
#     audio_file = None

#     if input_method == "Text":
#         user_input = st.text_area("Enter your message:")
#     else:
#         st.write("Record your audio message:")
#         audio_bytes = audio_recorder()
#         if audio_bytes:
#             st.audio(audio_bytes, format="audio/wav")
#             audio_file = ("audio.wav", audio_bytes)

#     if st.button("Send"):
#         if user_input or audio_file:
#             with st.spinner("Processing your request..."):
#                 files = {'file': audio_file} if audio_file else None
#                 data = {'user_id': user_id, 'text': user_input}

#                 response = requests.post(API_ENDPOINT, data=data, files=files)

#                 if response.status_code == 200:
#                     result = response.json()
#                     st.write("AI Response:")
#                     st.write(result['response'])
                    
#                     # Check if audio_url is in the response
#                     if 'audio_url' in result:
#                         st.audio(result['audio_url'])
#                 else:
#                     st.error(f"Error: {response.json().get('error', 'Unknown error occurred')}")
#         else:
#             st.warning("Please provide input before sending.")

#     # Display chat history
#     if st.button("Show Chat History"):
#         st.write("Chat History:")
#         # You'll need to implement a function to fetch chat history from your database
#         # For now, we'll just display a placeholder message
#         st.write("Chat history will be displayed here.")

# if __name__ == "__main__":
#     main()

# import streamlit as st
# import requests
# import os
# from dotenv import load_dotenv
# from audio_recorder_streamlit import audio_recorder
# import io

# # Load environment variables
# load_dotenv()

# # Set up the API endpoint
# API_ENDPOINT = os.getenv('API_ENDPOINT', 'https://anjali-v-ov26lo32lq-el.a.run.app/interact')

# def send_request(user_id, text=None, audio=None):
#     files = None
#     data = {'user_id': user_id}

#     if text:
#         data['text'] = text
#     elif audio:
#         files = {'file': ('audio.wav', io.BytesIO(audio), 'audio/wav')}

#     try:
#         response = requests.post(API_ENDPOINT, data=data, files=files)
        
#         st.write(f"Response status code: {response.status_code}")
#         st.write(f"Response headers: {response.headers}")

#         response.raise_for_status()  # Raise an exception for bad status codes
        
#         content_type = response.headers.get('content-type', '')
        
#         if 'application/json' in content_type:
#             return response.json()
#         elif 'audio/' in content_type:
#             return {'audio': response.content, 'content_type': content_type}
#         else:
#             st.error(f"Unexpected content type: {content_type}")
#             return {"response": f"Received unexpected content type: {content_type}"}
#     except requests.exceptions.RequestException as e:
#         st.error(f"Request error: {str(e)}")
#         return {"response": f"Error communicating with server: {str(e)}"}

# def main():
#     st.title("AI Companion Chatbot")

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             if message["type"] == "text":
#                 st.markdown(message["content"])
#             elif message["type"] == "audio":
#                 st.audio(message["content"], format="audio/wav")

#     user_id = st.sidebar.text_input("Enter your User ID:", value="default_user")

#     st.sidebar.write("Record your message:")
#     audio_bytes = audio_recorder()

#     if prompt := st.chat_input("What is your message?"):
#         st.session_state.messages.append({"role": "user", "type": "text", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         with st.spinner("AI is thinking..."):
#             response = send_request(user_id, text=prompt)

#         if 'response' in response:
#             with st.chat_message("assistant"):
#                 st.markdown(response['response'])
#             st.session_state.messages.append({"role": "assistant", "type": "text", "content": response['response']})
#         elif 'audio' in response:
#             with st.chat_message("assistant"):
#                 st.audio(response['audio'], format=response['content_type'])
#             st.session_state.messages.append({"role": "assistant", "type": "audio", "content": response['audio']})

#     if audio_bytes:
#         st.sidebar.audio(audio_bytes, format="audio/wav")
#         with st.spinner("Processing audio..."):
#             response = send_request(user_id, audio=audio_bytes)
        
#         with st.chat_message("user"):
#             st.markdown("Audio message sent")
#             st.audio(audio_bytes, format="audio/wav")
        
#         if 'response' in response:
#             with st.chat_message("assistant"):
#                 st.markdown(response['response'])
#             st.session_state.messages.append({"role": "assistant", "type": "text", "content": response['response']})
#         elif 'audio' in response:
#             with st.chat_message("assistant"):
#                 st.audio(response['audio'], format=response['content_type'])
#             st.session_state.messages.append({"role": "assistant", "type": "audio", "content": response['audio']})

#         st.session_state.messages.append({"role": "user", "type": "audio", "content": audio_bytes})

# if __name__ == "__main__":
#     main()

import streamlit as st
import requests
import os
from dotenv import load_dotenv
import io

# Load environment variables
load_dotenv()

# Set up the API endpoint
API_ENDPOINT = os.getenv('API_ENDPOINT', 'https://raju-audio-ov26lo32lq-uc.a.run.app/interact')

def send_request(user_id, text=None, audio=None):
    files = None
    data = {'user_id': user_id}
    if text:
        data['text'] = text
    elif audio:
        files = {'file': ('audio.wav', io.BytesIO(audio), 'audio/wav')}
    try:
        response = requests.post(API_ENDPOINT, data=data, files=files)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        content_type = response.headers.get('content-type', '')
        
        if 'application/json' in content_type:
            return response.json()
        elif 'audio/' in content_type:
            return {'audio': response.content, 'content_type': content_type}
        else:
            return {"response": f"Received unexpected content type: {content_type}"}
    except requests.exceptions.RequestException as e:
        return {"response": f"Error communicating with server: {str(e)}"}

def main():
    st.title("AI Raju Chatbot")
    user_id = st.text_input("Enter your User ID:", value="default_user")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.write("### Chat with Raju")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["type"] == "text":
                st.markdown(message["content"])
            elif message["type"] == "audio":
                st.audio(message["content"], format="audio/wav")

    input_method = st.radio("Choose input method:", ("Text", "Audio"))

    if input_method == "Text":
        user_input = st.text_area("Enter your message:")
        if st.button("Send Text"):
            if user_input:
                with st.chat_message("user"):
                    st.markdown(user_input)
                st.session_state.messages.append({"role": "user", "type": "text", "content": user_input})
                with st.spinner("AI is thinking..."):
                    response = send_request(user_id, text=user_input)
                process_response(response)
            else:
                st.warning("Please enter a message before sending.")

    else:  # Audio
        st.write("Record your audio message:")
        audio_file = st.file_uploader("Upload audio file", type=["wav", "mp3"])
        
        if audio_file is not None:
            st.audio(audio_file, format="audio/wav")
            if st.button("Send Audio"):
                audio_bytes = audio_file.read()
                with st.chat_message("user"):
                    st.markdown("Audio message sent")
                    st.audio(audio_bytes, format="audio/wav")
                st.session_state.messages.append({"role": "user", "type": "audio", "content": audio_bytes})
                with st.spinner("Processing audio..."):
                    response = send_request(user_id, audio=audio_bytes)
                process_response(response)
        else:
            st.info("Please upload an audio file to send.")

def process_response(response):
    if 'response' in response:
        with st.chat_message("assistant"):
            st.markdown(response['response'])
        st.session_state.messages.append({"role": "assistant", "type": "text", "content": response['response']})
    elif 'audio' in response:
        with st.chat_message("assistant"):
            st.audio(response['audio'], format=response['content_type'])
        st.session_state.messages.append({"role": "assistant", "type": "audio", "content": response['audio']})

if __name__ == "__main__":
    main()
