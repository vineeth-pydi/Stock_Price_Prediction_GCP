# Stock Price Prediction and Anomaly Detection

## Project Overview
This project aims to leverage Google Cloud Platform (GCP) technologies to analyze historical and real-time stock data for predicting stock price movements and detecting anomalies. Using BigQuery, Cloud Pub/Sub, Dataflow, and Data Studio, we provide insights for informed investment decisions.

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

![image](https://github.com/vineeth-pydi/Stock_Price_Prediction_GCP/assets/124265210/35ce202a-01c7-4f8b-a567-2456eae79d67)


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

## Contributing
Instructions for how to contribute to the project.

## License
Details about the project's licensing.

## Acknowledgments
Credits to team members, advisors, and any third-party resources used.
