WITH CorrelationAnalysis AS (
  SELECT 
    Symbol,
    Date,
    Close,
    Volume,
    LAG(Close, 1) OVER (PARTITION BY Symbol ORDER BY Date) AS PreviousDayClose,
    Close - LAG(Close, 1) OVER (PARTITION BY Symbol ORDER BY Date) AS PriceChange,
    Volume - LAG(Volume, 1) OVER (PARTITION BY Symbol ORDER BY Date) AS VolumeChange
  FROM 
    `mgmt-59000bd.Final_Project.Stocks`
)

SELECT 
  Symbol,
  Date,
  Close,
  Volume,
  PreviousDayClose,
  PriceChange,
  VolumeChange,
  CASE
    WHEN PriceChange > 0 AND VolumeChange > 0 THEN 'Positive Correlation'
    WHEN PriceChange < 0 AND VolumeChange < 0 THEN 'Negative Correlation'
    ELSE 'No Clear Correlation'
  END AS CorrelationIndicator
FROM 
  CorrelationAnalysis
ORDER BY 
  Symbol, 
  Date;
