# momopdf 📄✨

**momopdf** is a complete, lightweight, and high-performance suite of premium PDF tools. Built with a Flask backend and a modern vanilla CSS responsive frontend, it enables users to merge, split, compress, convert, sign, redact, and translate PDFs with zero third-party cloud service fees.

It also includes a companion Android mobile application (`momopdf-android`) to interface with the PDF toolchain natively.

---

## Features 🚀

### 1. Organize PDF
*   **Merge PDF:** Combine multiple PDFs into a single document. Malformed or fake PDF files (like renamed text or HTML documents) are automatically repaired or converted.
*   **Split PDF:** Split documents by page extraction, custom range, or fixed-size chunks. Outputs a single PDF or a clean ZIP.
*   **Remove Pages:** Instantly delete specific page numbers or ranges (e.g. `1,3,5-7`).
*   **Organize PDF:** Rearrange, duplicate, or delete pages dynamically in any order.
*   **Scan to PDF:** Compile captured images directly into a clean, unified PDF document.

### 2. Convert PDF
*   **JPG to PDF:** Convert image collections to PDF using Fit, A4, or A3 layouts.
*   **Word / PPT / Excel to PDF:** Build PDF documents directly from `.docx`, `.pptx`, and `.xlsx` files with layout, image, and table extraction.
*   **PDF to Word / PPT / Excel:** Export PDF pages into editable office formats. Falls back to image extraction for scanned documents.
*   **Web to PDF:** Render live websites to PDF using headless Chrome/Edge, WeasyPrint, or xhtml2pdf.
*   **PDF to JPG:** High-DPI page extraction to images, zipped automatically if multi-page.
*   **PDF to PDF/A:** Convert to standard long-term archival formats using Ghostscript or linearized PDF engine.

### 3. Edit & Security
*   **Rotate PDF:** Rotate pages by 90, 180, or 270 degrees.
*   **Add Page Numbers:** Apply custom-aligned headers or footers (`Page X`) across the document.
*   **Crop PDF:** Crop custom margin offsets from the top, bottom, left, and right.
*   **Watermark PDF:** Overlay custom text at any rotation on all pages.
*   **Sign PDF:** Merge signature images into documents at precise pages, coordinates, and scales.
*   **Redact PDF:** Permanently black out sensitive text using keyword searches.
*   **PDF Filler:** Dynamically fill interactive AcroForm PDF fields using JSON key-value inputs.
*   **Repair PDF:** Fix malformed or truncated PDFs automatically using pikepdf and qpdf engines.
*   **Protect / Unlock PDF:** Encrypt/decrypt PDFs using secure passwords.

### 4. Advanced & AI
*   **Compare PDF:** Generate HTML side-by-side diff views highlighting text additions and removals.
*   **Translate PDF:** Translate entire documents into target languages (using `deep-translator`) and export as formatted PDFs.
*   **AI Summarizer:** Extractive frequency-based summaries of document contents.
*   **Workflow Chains:** Queue multiple PDF tasks together (e.g. Rotate -> Watermark -> Compress) to run sequentially.
*   **Extract Assets:** Download all embedded images, raw text content, and metadata as a structured ZIP.

---

## Tech Stack 🛠️

*   **Frontend:** HTML5, Vanilla CSS3 (with custom responsive design layouts and smooth animations), FontAwesome icons.
*   **Backend:** Python 3, Flask, Flask-CORS.
*   **PDF Manipulation Libraries:** PyMuPDF (`fitz`), `pypdf`, `pikepdf`, `pdfplumber`, `reportlab`, `img2pdf`.
*   **Office Documents Parser:** `python-docx`, `openpyxl`, `python-pptx`.
*   **Translation & OCR:** `deep-translator`, `pytesseract` (Tesseract OCR wrapper).
*   **External Engines (Optional):** Tesseract OCR, Ghostscript, Headless Web Browser.

---

## Installation & Setup 💻

### Prerequisites
Make sure you have Python 3.8+ installed. 

For full feature compatibility, install:
*   [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (for OCR/scanned text extraction)
*   [Ghostscript](https://www.ghostscript.com/) (for PDF/A conversion)
*   Google Chrome or Microsoft Edge (for Web-to-PDF conversion)

### Setup Backend & Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Mohanraj122/momo-pdf.git
   cd momo-pdf
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate

   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python single_file_app.py
   ```
   The application will start on `http://localhost:5000` and automatically serve the frontend page (`index.html`).

---

## Android App Setup 📱
The companion Android wrapper codebase is located under the `momopdf-android` directory. 
1. Open the folder in **Android Studio**.
2. Sync the project with Gradle.
3. Build and run the app on an emulator or physical device.
4. Modify `MainActivity.kt` or config files to point to your hosted/local backend URL.

---

## License 📄
This project is open-source. Feel free to modify and build upon it!
