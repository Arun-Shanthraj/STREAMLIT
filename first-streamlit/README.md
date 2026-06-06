# 🚀 [Currency Converter]

A clean, interactive Streamlit application built using Python and managed with `uv`.

## 🛠️ Prerequisites

Before running the app, make sure you have the following installed on your machine:
* Python 3.10+
* **uv** (An ultra-fast Python package and environment manager)

If you don't have `uv` installed, run:
```bash
# macOS/Linux
curl -LsSf https://astral.sh | sh

# Windows
powershell -c "irm https://astral.sh | iex"
```

## 💻 Local Installation & Setup

Follow these steps to run the application locally on your computer:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Arun-Shanthraj/STREAMLIT.git
   cd STREAMLIT
   ```

2. **Switch to the development branch:**
   ```bash
   git checkout dev
   ```

3. **Run the Streamlit application:**
   Using `uv run` will automatically set up a virtual environment and launch the app:
   ```bash
   uv run streamlit run currency_converter.py
   ```

## 🌐 How to Share (Local Network)

To allow anyone on your home Wi-Fi to access this app:
1. Run the app using the command above.
2. Locate the **Network URL** outputted in your terminal (e.g., `http://192.168.X.X:8501`).
3. Send that link to your brother so he can open it on his laptop browser!
