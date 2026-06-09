import requests
import json
import os

BASE_URL = "http://127.0.0.1:5000"
TEST_PDF = "test.pdf"

# Create a second PDF for comparison
from reportlab.pdfgen import canvas
def create_pdf(filename, text):
    c = canvas.Canvas(filename)
    c.drawString(100, 750, text)
    c.save()

create_pdf("test_compare_1.pdf", "This is the first PDF.")
create_pdf("test_compare_2.pdf", "This is the second PDF with differences.")

def test_compare():
    print("Testing Compare...")
    with open("test_compare_1.pdf", "rb") as f1, open("test_compare_2.pdf", "rb") as f2:
        files = [
            ("files", ("test_compare_1.pdf", f1, "application/pdf")),
            ("files", ("test_compare_2.pdf", f2, "application/pdf"))
        ]
        response = requests.post(f"{BASE_URL}/compare", files=files)
        if response.status_code == 200:
            print("Compare: SUCCESS")
            with open("test_compare_output.html", "wb") as out:
                out.write(response.content)
        else:
            print(f"Compare: FAILED ({response.status_code}) - {response.text}")

def test_translate():
    print("Testing Translate...")
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        data = {"lang": "es"}
        response = requests.post(f"{BASE_URL}/translate", files=files, data=data)
        if response.status_code == 200:
            print("Translate: SUCCESS")
            with open("test_translate_output.txt", "wb") as out:
                out.write(response.content)
        else:
            print(f"Translate: FAILED ({response.status_code}) - {response.text}")

def test_summarize():
    print("Testing Summarize...")
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        response = requests.post(f"{BASE_URL}/summarize", files=files)
        if response.status_code == 200:
            print("Summarize: SUCCESS")
            with open("test_summarize_output.txt", "wb") as out:
                out.write(response.content)
        else:
            print(f"Summarize: FAILED ({response.status_code}) - {response.text}")

def test_workflow():
    print("Testing Workflow...")
    # Rotate 90, then compress (noop basically)
    actions = [
        {"tool": "rotate", "params": {"angle": "90"}},
        {"tool": "compress", "params": {}}
    ]
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        data = {"actions": json.dumps(actions)}
        response = requests.post(f"{BASE_URL}/workflow", files=files, data=data)
        if response.status_code == 200:
            print("Workflow: SUCCESS")
            with open("test_workflow_output.pdf", "wb") as out:
                out.write(response.content)
        else:
            print(f"Workflow: FAILED ({response.status_code}) - {response.text}")

if __name__ == "__main__":
    try:
        requests.get(BASE_URL)
        test_compare()
        test_translate()
        test_summarize()
        test_workflow()
    except Exception as e:
        print(f"Server not running or error: {e}")
