CREATE OR REPLACE MODEL `mgmt-59000bd.Final_Project.Stocks_Price_model_v3`
OPTIONS(
  MODEL_TYPE='ARIMA_PLUS',
  TIME_SERIES_TIMESTAMP_COL='Date',
  TIME_SERIES_DATA_COL='Close',
  TIME_SERIES_ID_COL='Symbol',
  HOLIDAY_REGION = "US"
) AS
SELECT
  Date,
  Symbol,
  Close
FROM
  `mgmt-59000bd.Final_Project.Stocks`
  
  
SELECT
  *
FROM
  ML.EVALUATE(MODEL `mgmt-59000bd.Final_Project.Stocks_Price_model_v3`)
  
SELECT
  *
FROM
  ML.FORECAST(MODEL `mgmt-59000bd.Final_Project.Stocks_Price_model_v3`, STRUCT(30 AS horizon, 0.8 AS confidence_level))