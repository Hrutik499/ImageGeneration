import streamlit as st
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    messages = [{"role": "system", "content": "You are a helpful assistant that generates images."}, {"role": "user", "content": prompt }]
    response = openai.Completion.create(
        engine="davinci",
        prompt=messages,
    )
    return response.choices[0].text.strip()

st.title("Image Generation with DALL·E")

user_prompt = st.text_input("Enter your image prompt:")
if user_prompt:
    generated_image = generate_image(user_prompt)
    st.image(generated_image, caption="Generated Image", use_column_width=True)