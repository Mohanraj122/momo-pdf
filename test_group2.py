import requests

BASE_URL = "http://127.0.0.1:5000"
TEST_PDF = "test.pdf"

def test_web_to_pdf():
    print("Testing Web to PDF...")
    data = {"url": "https://example.com"}
    response = requests.post(f"{BASE_URL}/web-to-pdf", data=data)
    if response.status_code == 200:
        print("Web to PDF: SUCCESS")
        with open("test_web_output.pdf", "wb") as out:
            out.write(response.content)
    else:
        print(f"Web to PDF: FAILED ({response.status_code}) - {response.text}")

def test_pdf_to_pdfa():
    print("Testing PDF to PDF/A...")
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        response = requests.post(f"{BASE_URL}/pdf-to-pdfa", files=files)
        if response.status_code == 200:
            print("PDF to PDF/A: SUCCESS")
            with open("test_pdfa_output.pdf", "wb") as out:
                out.write(response.content)
        else:
            print(f"PDF to PDF/A: FAILED ({response.status_code}) - {response.text}")

def test_pdf_to_excel():
    print("Testing PDF to Excel...")
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        response = requests.post(f"{BASE_URL}/pdf-to-excel", files=files)
        if response.status_code == 200:
            print("PDF to Excel: SUCCESS")
            with open("test_excel_output.xlsx", "wb") as out:
                out.write(response.content)
        else:
            print(f"PDF to Excel: FAILED ({response.status_code}) - {response.text}")

if __name__ == "__main__":
    try:
        requests.get(BASE_URL)
        test_web_to_pdf()
        test_pdf_to_pdfa()
        test_pdf_to_excel()
    except Exception as e:
        print(f"Server not running or error: {e}")
