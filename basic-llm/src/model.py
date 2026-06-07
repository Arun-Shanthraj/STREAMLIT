# warning control
import warnings
warnings.filterwarnings("ignore")

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME,
    dtype="auto",
    device_map="auto")

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    return_full_text=False, # False means to not include the prompt text in the returned text
    max_new_tokens=1000,
    do_sample=False, # no randomness in the generated text
)

def generate_response(prompt):
    response = generator(prompt)
    return response[0]['generated_text']