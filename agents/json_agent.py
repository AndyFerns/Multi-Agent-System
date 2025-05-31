def process_json(json_data):
    required_fields = ['invoice_number', 'date', 'amount']
    extracted = {key: json_data.get(key) for key in required_fields}
    missing = [key for key, value in extracted.items() if not value]
    return extracted, missing

