
SELECT
  *
FROM
  ML.FORECAST(MODEL `mgmt-59000bd.Final_Project.Stocks_Price_model_v3`, STRUCT(30 AS horizon, 0.9 AS confidence_level))


SELECT
  *
FROM
  ML.EVALUATE(MODEL `mgmt-59000bd.Final_Project.Stocks_Price_model_v3`)