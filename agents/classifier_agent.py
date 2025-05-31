
# agents/classifier_agent.py
import os
from agents.json_agent import process_json
from agents.email_agent import process_email
from agents.pdf_agent import process_pdf
from shared_memory.memory import log_memory
from utils.llm import classify_intent_llm
import json
import uuid
import time


def classify_and_route(input_path, db):
    ext = os.path.splitext(input_path)[1].lower()
    thread_id = f"thread-{uuid.uuid4().hex[:8]}"  # 8-char unique ID

    if ext == '.json':
        format_type = 'JSON'
        with open(input_path) as f:
            data = json.load(f)
        intent = classify_intent_llm(json.dumps(data))
        extracted, missing = process_json(data)

    elif ext == '.txt':
        format_type = 'Email'
        with open(input_path) as f:
            data = f.read()
        intent = classify_intent_llm(data)
        extracted = process_email(data)
        missing = []

    elif ext == '.pdf':
        format_type = 'PDF'
        extracted_text = process_pdf(input_path)
        intent = classify_intent_llm(extracted_text)
        extracted = {"content": extracted_text}
        missing = []

    else:
        format_type = 'Unknown'
        intent = 'Unknown'
        extracted = {}
        missing = []

    log_memory(db, input_path, format_type, intent, extracted, thread_id) #updated to use unique thread id
    print(f"[ROUTE] {format_type} routed for intent '{intent}' with extracted: {extracted}, missing: {missing}")

