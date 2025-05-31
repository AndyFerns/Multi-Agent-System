# Multi-Agent AI System

A modular multi-agent AI system that accepts input files (PDF, JSON, Email), classifies their format and intent, routes to specialized agents for processing, and maintains shared memory for chaining and traceability.

---

## 🎥 Procedure

- Input a sample file (email, JSON, or PDF)  
- Classifier Agent detects format and intent  
- Routes to the appropriate agent (JSON Agent, Email Agent, PDF Agent)  
- Extracted information and intent logged in shared memory  
- Display logs grouped by conversation thread  

---

## 📂 Sample Input Files

Sample inputs for testing the system can be found in the `samples/` folder:

- `sample_email.txt` — a sample email text file  
- `sample_invoice.json` — a sample invoice JSON file  
- `sample_resume.pdf` — a sample PDF file (your resume)  

These files simulate typical user inputs to test classification and extraction.

---

## 📁 Folder Structure

```text
Multi Agent System/
├── main.py
├── README.md
├── requirements.txt
├── .env
├── .gitignore
├── agents/
│   ├── classifier_agent.py
│   ├── email_agent.py
│   ├── json_agent.py
│   ├── pdf_agent.py
├── outputs/
│   ├── logs.py
├── samples/
│   ├── Andrew Resume Final.pdf
│   ├── sample_email.txt
│   ├── sample_email_2.txt
│   ├── sample_email_3.txt
│   ├── sample_invoice.json
│   ├── sample_json.json
├── shared_memory/
│   ├── memory.py
├── tests/
│   ├── test_classifier_agent.py
│   ├── test_llm.py
│   ├── test_logging.py
│   ├── test_pdf_agent.py
├── utils/
│   ├── file_loader.py
│   ├── llm.py
│   ├── logger.py

```

- **agents/** — Modules for different agents handling specific input types  
- **samples/** — Sample input files to test the system  
- **shared_memory/** — Lightweight SQLite-backed memory module to store logs and context  
- **utils/** — Utility modules including the intent classification pipeline  
- **main.py** — Entry point to run the multi-agent system  
- **requirements.txt** — Required Python dependencies  

---

## 📝 Sample Output Logs

Example of routing and extraction logged to console:

2025-05-31 12:00:00 [INFO] [ROUTE] Email routed for intent 'RFQ' with extracted: {'sender': 'alice@example.com', 'urgency': 'High', 'intent': 'RFQ'}, missing: [], thread: thread-1a2b3c4d

2025-05-31 12:00:01 [INFO] [ROUTE] JSON routed for intent 'RFQ' with extracted: {'invoice_number': 'INV-12345', 'date': '2025-05-01', 'amount': 4500.0}, missing: [], thread: thread-5e6f7g8h

2025-05-31 12:00:02 [INFO] [ROUTE] PDF routed for intent 'General' with extracted: {'content': 'Extracted PDF text content...'}, missing: [], thread: thread-9i0j1k2l

You can also print shared memory logs grouped by thread with:

```bash
python main.py --print-memory


```
