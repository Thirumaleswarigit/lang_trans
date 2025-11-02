# import streamlit as st
# import requests
# import json
# st.title("Simple Language Translation App")
# text=st.text_input("Enter text to translate: ")
# st.write("Select a target language: ")
# st=st.selectbox("Languages: ",["Telugu","Hindi","French","German","Spanish"])
# if st.button("Translate"):
#     if text=="":
#         st.write("please enter some text to translate.")
#     else:
#         url = "https://api.mymemory.translated.net/get"
#         lang_code={
#             "Telugu":"te",
#             "Hindi":"hi",
#             "French":"fr",
#             "German":"ge",
#             "Spanish":"sp"
#         }
#         from_lang=st.text_input("Enter translate lang")
#         to_lang=lang_code[st]
#         params={
#             "q":text,
#             "langpair":from_lang+"|"+to_lang
#         }
#         res=requests.get(url,params=params)
#         data=json.loads(res.text)
#         trans=data["responseData"]["translatedText"]
#         st.write("translated successsfully")
#         st.write(trans)

import streamlit as st
import requests
import json

st.title("🌍 Simple Language Translation App")

text = st.text_input("Enter text to translate:")
#from_lang=st.text_input("Enter Source Language: ")
st.write("Select a target language:")
option = st.selectbox("Languages:", ["Telugu", "Hindi", "French", "German", "Spanish"])


if st.button("Translate"):

    if text == "":
        st.warning("⚠️ Please enter some text to translate.")
    else:
       
        url = "https://api.mymemory.translated.net/get"

      
        lang_code = {
            "Telugu": "te",
            "Hindi": "hi",
            "French": "fr",
            "German": "de",
            "Spanish": "es"
        }

        from_lang="en"              
        to_lang = lang_code[option]           

        
        params = {
            "q": text,
            "langpair": from_lang + "|" + to_lang
        }

        res = requests.get(url, params=params)
        data = json.loads(res.text)
        translated = data["responseData"]["translatedText"]

        st.success("✅ Translated Text:")
        st.write(translated)
