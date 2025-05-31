from utils.llm import classify_intent_llm

def test_classification():
    text = "We urgently need a quote for 100 widgets."
    intent = classify_intent_llm(text)
    assert intent in ["RFQ", "Complaint", "General"]
