WITH DailyVolatility AS (
  SELECT 
    Symbol,
    Date,
    High,
    Low,
    Close,
    ABS(High - Low) AS DailyVolatility,
    ABS(High - Low) / Close * 100 AS DailyVolatilityPercent
  FROM 
    `mgmt-59000bd.Final_Project.Stocks`
)

SELECT 
  DV.Symbol,
  DV.Date,
  DV.High,
  DV.Low,
  DV.Close,
  DV.DailyVolatility,
  DV.DailyVolatilityPercent,
  LAG(DV.DailyVolatility, 1) OVER (PARTITION BY DV.Symbol ORDER BY DV.Date) AS PreviousDayVolatility,
  (DV.DailyVolatility - LAG(DV.DailyVolatility, 1) OVER (PARTITION BY DV.Symbol ORDER BY DV.Date)) / LAG(DV.DailyVolatility, 1) OVER (PARTITION BY DV.Symbol ORDER BY DV.Date) * 100 AS VolatilityChangePercent
FROM 
  DailyVolatility AS DV
ORDER BY 
  DV.Symbol, 
  DV.Date;
