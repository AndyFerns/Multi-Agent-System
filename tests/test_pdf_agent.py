from agents.pdf_agent import process_pdf

def test_pdf_extraction():
    text = process_pdf("samples/sample_invoice.pdf")
    assert len(text) > 10
