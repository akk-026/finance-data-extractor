# 🧾 Finance Data Extractor

This is a simple **Streamlit web app** that extracts structured financial data (like Revenue and EPS) from unstructured text paragraphs.

---

## 🚀 Features

- Extracts:
  - 📈 Estimated Revenue
  - 📉 Actual Revenue
  - 💰 Estimated EPS (Earnings Per Share)
  - 🧮 Actual EPS
- Takes plain-text financial reports or earnings call summaries as input
- Displays extracted data in a clean table
- Built with:
  - `streamlit`
  - `pandas`
  - Custom NLP extractor (`extract()` from `data_extractor.py`)

---

## 🧪 Example

Input:
> Apple reported revenue of $100B vs estimated $95B. EPS came in at $1.50, beating estimates of $1.40.

Output table:

| Measure | Estimated | Actual |
|---------|-----------|--------|
| Revenue | $95B      | $100B  |
| EPS     | $1.40     | $1.50  |

---

## 🛠️ How to Run

```bash
git clone https://github.com/YOUR_USERNAME/finance-data-extractor.git
cd finance-data-extractor
pip install -r requirements.txt
streamlit run main.py