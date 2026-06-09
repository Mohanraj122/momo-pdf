import requests
import os

BASE_URL = "http://127.0.0.1:5000"
TEST_PDF = "test.pdf"

def test_rotate():
    print("Testing Rotate...")
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        data = {"angle": "90"}
        response = requests.post(f"{BASE_URL}/rotate", files=files, data=data)
        if response.status_code == 200:
            print("Rotate: SUCCESS")
            with open("test_rotate_output.pdf", "wb") as out:
                out.write(response.content)
        else:
            print(f"Rotate: FAILED ({response.status_code}) - {response.text}")

def test_remove_pages():
    print("Testing Remove Pages...")
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        data = {"pages": "1"} # Remove page 1
        response = requests.post(f"{BASE_URL}/remove-pages", files=files, data=data)
        if response.status_code == 200:
            print("Remove Pages: SUCCESS")
            with open("test_remove_output.pdf", "wb") as out:
                out.write(response.content)
        else:
            print(f"Remove Pages: FAILED ({response.status_code}) - {response.text}")

def test_organize():
    print("Testing Organize Pages...")
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        data = {"pages": "1,1"} # Duplicate page 1
        response = requests.post(f"{BASE_URL}/organize", files=files, data=data)
        if response.status_code == 200:
            print("Organize Pages: SUCCESS")
            with open("test_organize_output.pdf", "wb") as out:
                out.write(response.content)
        else:
            print(f"Organize Pages: FAILED ({response.status_code}) - {response.text}")

def test_page_numbers():
    print("Testing Add Page Numbers...")
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        data = {"position": "bottom-right"}
        response = requests.post(f"{BASE_URL}/add-page-numbers", files=files, data=data)
        if response.status_code == 200:
            print("Page Numbers: SUCCESS")
            with open("test_numbers_output.pdf", "wb") as out:
                out.write(response.content)
        else:
            print(f"Page Numbers: FAILED ({response.status_code}) - {response.text}")

def test_crop():
    print("Testing Crop...")
    with open(TEST_PDF, "rb") as f:
        files = {"file": f}
        data = {"left": "50", "right": "50", "top": "50", "bottom": "50"}
        response = requests.post(f"{BASE_URL}/crop", files=files, data=data)
        if response.status_code == 200:
            print("Crop: SUCCESS")
            with open("test_crop_output.pdf", "wb") as out:
                out.write(response.content)
        else:
            print(f"Crop: FAILED ({response.status_code}) - {response.text}")

if __name__ == "__main__":
    # Ensure server is running before running this
    try:
        requests.get(BASE_URL)
        test_rotate()
        test_remove_pages()
        test_organize()
        test_page_numbers()
        test_crop()
    except Exception as e:
        print(f"Server not running or error: {e}")
