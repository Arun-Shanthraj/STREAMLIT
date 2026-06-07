import warnings
import streamlit as st
import time

warnings.filterwarnings("ignore")

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


@st.cache_resource
def load_generator():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME,
        dtype="auto",
        device_map="auto")

    generator = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        return_full_text=False, # False means to not include the prompt text in the returned text
        max_new_tokens=50,
        do_sample=False, # no randomness in the generated text
    )

    return generator, tokenizer

generator, tokenizer = load_generator()

def generate_response(prompt):
    messages = [
        {"role": "user", "content": prompt}
    ]
    formatted_prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    response = generator(formatted_prompt)

    return response[0]["generated_text"]
