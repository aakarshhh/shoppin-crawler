# **E-Commerce Product URL Scraper**

This repository contains a web scraping tool designed to identify and extract product URLs from a list of e-commerce websites. The solution leverages **Streamlit** to provide a user-friendly interface where users can input domains, view results in real-time, and download the discovered product URLs in a structured table format.

---

## **Features**
- **Domain Validation**: Ensures URLs belong to the specified domains.
- **Product Page Identification**: Uses pattern matching to identify product-related URLs based on common keywords like `/product/`, `/item/`, `/dp/`, etc.
- **Interactive Streamlit App**:
  - Upload a list of domains directly via the web interface.
  - Real-time URL discovery results displayed in a table.
  - Option to download the results as a CSV file.
- **Local Deployment Support**: Deploy the Streamlit app locally for personal use.

---

## **Approach**

### **1. URL Discovery**
The tool uses the following process to identify product URLs:
1. **Input Validation**:
   - The user provides a list of domains via the Streamlit app.
   - Each domain is sanitized to ensure it includes a valid HTTP/HTTPS scheme.
2. **Recursive Crawling**:
   - The tool crawls the given domains recursively, extracting all `<a>` tags for links.
   - Each link is validated to ensure it belongs to the domain and matches common product-related patterns.
3. **Pattern Matching**:
   - A predefined list of product-related patterns (e.g., `/product/`, `/item/`, `/dp/`) is used to identify potential product URLs.
4. **Domain Validation**:
   - Ensures URLs belong to the input domains and skips external links.

---

### **2. Streamlit App**
The Streamlit app (`app.py`) is designed to provide an intuitive interface for scraping and viewing results:
1. **Domain Input**:
   - Users can upload a text file containing domains or manually enter them in a text field.
2. **Real-Time Updates**:
   - The app displays discovered URLs in a table format as the scraper processes the domains.
3. **Downloadable Results**:
   - The app provides an option to download the results as a CSV file directly from the interface.

---

### **Usage**

#### **1. Online Deployment**
Once the app is deployed online, users can:
- Visit the public link (to be inserted later).
- Enter the list of domains in the provided input field or upload a `.txt` file.
- View the discovered product URLs in the results table.
- Download the results as a CSV file.

#### **2. Local Deployment**
To run the app locally:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aakarshhh/shoppin-crawler
   cd shoppin-crawler
   ```

2. **Install Python Dependencies**:
   Install all required Python packages using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:
   ```bash
   cd ecom_scrapper
   streamlit run app.py
   ```

4. **Access the App**:
   - Open your browser and navigate to `http://localhost:8501`.
   - Enter the list of domains or upload a text file.
   - View and download results from the interface.

---

### **Input Format**
- The input file should contain one domain per line.
- Example:
  ```
  amazon.in
  flipkart.com
  myntra.com
  ```

---

### **Example Output**
After entering the domains, the app will display a table of discovered product URLs. An example output:

| Domain       | ProductURL                                             |
|--------------|--------------------------------------------------------|
| amazon.in    | https://www.amazon.in/dp/B08L5W5GCX                    |
| flipkart.com | https://www.flipkart.com/item/12345                    |
| myntra.com   | https://www.myntra.com/product/56789                   |

The table can be downloaded as a CSV file.

---

### **Technical Details**
- **Language**: Python
- **Frameworks/Libraries**:
  - **Scrapy**: For web crawling and URL discovery.
  - **Streamlit**: For building the interactive user interface.
  - **tldextract**: For extracting domains from URLs.
  - **Pandas**: For handling tabular data.
- **Features**:
  - Recursive crawling for product URL discovery.
  - Real-time updates in the Streamlit interface.

---

### **Future Enhancements**
- Support for JavaScript-rendered pages using `playwright`.
- Enhanced error handling and retry mechanisms for failed requests.

---