import streamlit as st
import requests
import base64
import json

st.set_page_config(page_title="Image Summarization")
st.title("Welcome to Vision to Insights")
st.write("Upload an image and get a short AI-generated description using Ollama Vision-Language Model (VLM).")
upfile=st.file_uploader("Upload an image",type=["jpg","jpeg","png"])

if upfile is not None:
    st.image(upfile, caption="Uploaded Image",  width=500)

    ibytes=upfile.read()
    ibase=base64.b64encode(ibytes).decode("utf-8")

    if st.button("Generate Summary"):
        with st.spinner("Analyzing image, please wait..."):
            url = "http://localhost:11500/api/generate"
            body={
                "model":"llava", 
                "prompt":"Provide a detailed summary of this image.",
                "images":[ibase]
                }            
            response=requests.post(
                url,json=body,stream=True
            )

            if response.status_code==200:
                result = ""
                for line in response.iter_lines():
                    if line:
                        data=json.loads(line.decode("utf-8"))
                        if "response" in data:
                            result+=data["response"]

                if result.strip():
                    st.success("Summary Generated!")
                    st.subheader("Summary:")
                    st.write(result.strip())
                        
                    st.download_button(
                        label="Download Summary",
                        data=result.strip(),
                        file_name="ImageSummary.txt",
                        mime="text/plain"
                    )
                else:
                    st.warning(" Summary cant be generated, Try another image...")
            else:
                st.error(f" Error {response.status_code}: {response.text}")
