# Stock Price Prediction and Anomaly Detection

## Project Overview
This project aims to leverage Google Cloud Platform (GCP) technologies to analyze historical and real-time stock data for predicting stock price movements and detecting anomalies. Using BigQuery, Cloud Pub/Sub, Dataflow, and Data Studio, and Vertex AI workbench we provide insights for informed investment decisions.

### Key Features
- Real-time stock price prediction using historical and streamed data.
- Anomaly detection in stock price movements.
- Interactive dashboards for data visualization and analysis.

## Repository Structure

### `/data`
Contains raw and processed data files used in the project.
- `historical_stock_data.csv` - Historical stock data from Alpha Vantage.
- `real_time_stock_data.csv` - Real-time stock data streamed via Alpha Vantage API.

### `/notebooks`
Jupyter notebooks for detailed data analysis and modeling.
- `stock_price_analysis.ipynb` - Notebook for initial data exploration and visualization.
- `anomaly_detection_model.ipynb` - Notebook detailing the anomaly detection modeling process.

![image](https://github.com/vineeth-pydi/Stock_Price_Prediction_GCP/assets/124265210/8ee3fb97-18ae-4b7b-9fe7-986940ba0db3)

### `/code`
Source code and scripts for data processing and machine learning models.
- `data_ingestion.py` - Script for data ingestion from Alpha Vantage API.
- `ml_model_training.py` - Script for training the stock price prediction model.

### `/reports`
Markdown documents for project reports and summaries.
- `project_summary.md` - Executive summary of the project.
- `data_analysis_report.md` - Detailed report on data analysis findings.

### `/queries`
SQL queries and BigQuery related files for data processing and analytics.
- `stock_data_query.sql` - Query for extracting stock data from BigQuery.
- `anomaly_detection_query.sql` - Query for anomaly detection analysis.

### `README.md`
A comprehensive guide to navigating and understanding the repository.

## Getting Started
To get started with this project, clone the repository and install the required dependencies listed in `requirements.txt`.

### Prerequisites
- Python 3.8+
- Access to Google Cloud Platform

### Installation
1. Clone the repository:
   ```
   git clone [repository-url]
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Details on how to use the scripts, notebooks, and SQL queries for data analysis and machine learning.

### Running the Notebooks
```
jupyter notebook notebooks/stock_price_analysis.ipynb
```

### Executing the Scripts
```
python code/data_ingestion.py
python code/ml_model_training.py
```

## Acknowledgments
We extend our deepest gratitude to Professor Alok Chaturvedi, whose expertise and guidance in Big Data have been invaluable to this project. Professor Chaturvedi's extensive knowledge and passion for teaching have greatly enhanced our understanding and application of Big Data technologies. His commitment to academic excellence and his ability to make complex concepts accessible to all students have been instrumental in the success of our project.

We are thankful for the insights, constructive feedback, and unwavering support provided by Professor Chaturvedi throughout the duration of this project. His dedication to fostering a deep understanding of AI Assisted Big Data in the Cloud and its real-world applications has not only contributed to the success of this project but has also prepared us for future challenges in the field of data analytics.
