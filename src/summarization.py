import requests

API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-6-6"
headers = {"Authorization": " Bearer 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"}

def summarize_text(text):
    """
    Summarizes the input text using Hugging Face's Inference API.
    :param text: Text segment to summarize.
    :return: Summarized text.
    """
    payload = {"inputs": text, "parameters": {"max_length": 130, "min_length": 30}}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["summary_text"]

