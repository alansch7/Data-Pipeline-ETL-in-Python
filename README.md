# Data Pipeline ETL in Python

A modular ETL (Extract, Transform, Load) pipeline built in Python to automate data processing workflows and apply basic data quality checks.

---

## Features

- Data extraction from CSV files
- Data transformation and cleaning
- Data quality validation
- Automated loading process
- Modular project structure

---

## Project Structure

```bash
Data-Pipeline-ETL-in-Python/
│
├── data/
├── extract.py
├── transform.py
├── quality.py
├── load.py
├── main.py
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- CSV Processing

---

## Pipeline Flow

```text
Extract → Transform → Quality Checks → Load
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Data-Pipeline-ETL-in-Python.git
```

### 2. Install dependencies

```bash
pip install pandas
```

### 3. Run the pipeline

```bash
python main.py
```

---

## Example Output

```text
data extracted
data transformed
running quality checks
data loaded successfully
```

---

## Future Improvements

- Add logging system
- Docker support
- SQL database integration
- API data extraction
- Workflow orchestration with Airflow

---

## Author

Alan Schaefer
