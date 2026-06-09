import requests
import json
from PIL import Image

BASE_URL = "http://127.0.0.1:5000"
TEST_PDF = "test.pdf"

# Create larger dummy image
img = Image.new('RGB', (500, 500), color = 'red')
img.save('test_sig.png')

def test_repair():
    print("Testing Repair...")
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        response = requests.post(f"{BASE_URL}/repair", files=files)
        if response.status_code == 200:
            print("Repair: SUCCESS")
            with open("test_repair_output.pdf", "wb") as out:
                out.write(response.content)
        else:
            print(f"Repair: FAILED ({response.status_code}) - {response.text}")

def test_sign():
    print("Testing Sign...")
    with open(TEST_PDF, "rb") as f:
        with open("test_sig.png", "rb") as sig:
            files = {"file": f, "signature": sig}
            data = {"x": "100", "y": "100", "page": "1", "scale": "0.5"}
            response = requests.post(f"{BASE_URL}/sign", files=files, data=data)
            if response.status_code == 200:
                print("Sign: SUCCESS")
                with open("test_sign_output.pdf", "wb") as out:
                    out.write(response.content)
            else:
                print(f"Sign: FAILED ({response.status_code}) - {response.text}")

def test_redact():
    print("Testing Redact...")
    # This might fail if "PDF" text not found, but it should return a PDF anyway
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        data = {"text": "PDF"}
        response = requests.post(f"{BASE_URL}/redact", files=files, data=data)
        if response.status_code == 200:
            print("Redact: SUCCESS")
            with open("test_redact_output.pdf", "wb") as out:
                out.write(response.content)
        else:
            print(f"Redact: FAILED ({response.status_code}) - {response.text}")

def test_scan_to_pdf():
    print("Testing Scan to PDF (Alias)...")
    with open("test_sig.png", "rb") as f:
        # requests list of tuples for multiple files
        files = [("files", ("image.png", f, "image/png"))]
        response = requests.post(f"{BASE_URL}/scan-to-pdf", files=files)
        if response.status_code == 200:
            print("Scan to PDF: SUCCESS")
            with open("test_scan_output.pdf", "wb") as out:
                out.write(response.content)
        else:
            print(f"Scan to PDF: FAILED ({response.status_code}) - {response.text}")

if __name__ == "__main__":
    try:
        requests.get(BASE_URL)
        test_repair()
        test_sign()
        test_redact()
        # Skipped fill form as it needs specific PDF
        test_scan_to_pdf()
    except Exception as e:
        print(f"Server not running or error: {e}")
