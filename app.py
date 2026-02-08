import streamlit as st
from langchain_community.llms import Ollama

st.set_page_config(page_title="🌾 AgroAgent", layout="centered")
st.title("🌾 AgroAgent – Organic Farming Assistant")
st.caption("100% Local • Free • Offline")

crop = st.text_input("Crop name", "Tomato")
problem = st.text_area("Describe your problem")

if st.button("Get Organic Solution"):
    llm = Ollama(model="llama3")

    prompt = f"""
    You are AgroAgent, an expert organic farming assistant for Indian farmers.

    Rules:
    - Organic methods only
    - Simple language
    - Step-by-step advice
    - No chemicals

    Crop: {crop}
    Problem: {problem}

    Give practical organic solution.
    """

    with st.spinner("Thinking like a farming expert 🌱"):
        response = llm.invoke(prompt)

    st.success("Solution Ready")
    st.write(response)
