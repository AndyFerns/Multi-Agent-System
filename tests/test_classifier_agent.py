import os
import sqlite3
from agents.classifier_agent import classify_and_route
from shared_memory.memory import init_db

def test_routing_email():
    db = init_db()
    classify_and_route("samples/sample_email.txt", db)

    cur = db.cursor()
    cur.execute("SELECT format, intent FROM memory ORDER BY id DESC LIMIT 1")
    fmt, intent = cur.fetchone()
    assert fmt == "Email"
    assert intent in ["RFQ", "Complaint", "General"]

def test_routing_json():
    db = init_db()
    classify_and_route("samples/sample_invoice.json", db)

    cur = db.cursor()
    cur.execute("SELECT format, intent FROM memory ORDER BY id DESC LIMIT 1")
    fmt, intent = cur.fetchone()
    assert fmt == "JSON"
    assert intent in ["RFQ", "Complaint", "General"]
