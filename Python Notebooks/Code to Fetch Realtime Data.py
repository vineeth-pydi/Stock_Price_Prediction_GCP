import os
import requests
import json
from google.cloud import pubsub_v1
from flask import abort
 
# Initialize Pub/Sub client
publisher = pubsub_v1.PublisherClient()
project_id = 'mgmt590-396517'
topic_name = 'final_project_topic'
topic_path = publisher.topic_path(project_id, topic_name)
 
# Alpha Vantage API configuration
api_key = '1MNW1NQ5CYSWCNVD'  # Consider using environment variables or secret manager
base_url = 'https://www.alphavantage.co/query'
 
# List of stock symbols
stock_symbols = ['MSFT', 'GOOG']
 
def fetch_stock_data(request):
    # Check for correct HTTP method
    if request.method != 'GET':
        return abort(405)
 
    for symbol in stock_symbols:
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': '5min',
            'apikey': api_key,
            'datatype': 'json'
        }
 
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            time_series = data.get('Time Series (5min)', {})
 
            for date, daily_data in time_series.items():
                # Extracting the required fields
                stock_data = {
                    'Date': date,
                    'Symbol': symbol,
                    'Open': daily_data['1. open'],
                    'High': daily_data['2. high'],
                    'Low': daily_data['3. low'],
                    'Close': daily_data['4. close'],
                    'Volume': daily_data['5. volume']
                }
 
                # Publish to Pub/Sub
                future = publisher.publish(topic_path, json.dumps(stock_data).encode('utf-8'))
                future.result()  # Confirm the publish succeeded
 
        else:
            return f'Error fetching stock data for {symbol}: {response.text}', response.status_code
 
    return 'Data fetched and published successfully for MSFT and GOOG', 200
 
# The line below is for local testing and should be removed in the deployed Cloud Function
# fetch_stock_data(None)