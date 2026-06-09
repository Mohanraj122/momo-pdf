import requests
import json
import os

BASE_URL = "http://127.0.0.1:5000"
TEST_PDF = "test.pdf"

def test_pdf_extract():
    print("Testing PDF Extract...")
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        response = requests.post(f"{BASE_URL}/pdf-extract", files=files)
        if response.status_code == 200:
            print("PDF Extract: SUCCESS")
            with open("test_extract_output.zip", "wb") as out:
                out.write(response.content)
        else:
            print(f"PDF Extract: FAILED ({response.status_code}) - {response.text}")

def test_copy_pdf():
    print("Testing Copy PDF...")
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        data = {"copies": "3"}
        response = requests.post(f"{BASE_URL}/copy-pdf", files=files, data=data)
        if response.status_code == 200:
            print("Copy PDF: SUCCESS")
            with open("test_copy_output.zip", "wb") as out:
                out.write(response.content)
        else:
            print(f"Copy PDF: FAILED ({response.status_code}) - {response.text}")

if __name__ == "__main__":
    try:
        requests.get(BASE_URL)
        test_pdf_extract()
        test_copy_pdf()
    except Exception as e:
        print(f"Server not running or error: {e}")
