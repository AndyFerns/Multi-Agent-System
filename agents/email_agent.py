
# agents/email_agent.py
def process_email(email_text):
    lines = email_text.split('\n')
    sender = next((l for l in lines if 'From:' in l), 'unknown').replace('From:', '').strip()
    urgency = 'High' if 'urgent' in email_text.lower() else 'Normal'
    intent = 'RFQ' if 'quote' in email_text.lower() else 'General'

    return {
        "sender": sender,
        "urgency": urgency,
        "intent": intent
    }