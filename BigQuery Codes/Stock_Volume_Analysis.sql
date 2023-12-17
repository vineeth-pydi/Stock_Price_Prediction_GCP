WITH VolumeAnalysis AS (
  SELECT 
    Symbol,
    Date,
    Close,
    Volume,
    LAG(Volume, 1) OVER (PARTITION BY Symbol ORDER BY Date) AS PreviousDayVolume,
    (Volume - LAG(Volume, 1) OVER (PARTITION BY Symbol ORDER BY Date)) AS VolumeChange,
    (Volume - LAG(Volume, 1) OVER (PARTITION BY Symbol ORDER BY Date)) / LAG(Volume, 1) OVER (PARTITION BY Symbol ORDER BY Date) * 100 AS VolumeChangePercent
  FROM 
    `mgmt-59000bd.Final_Project.Stocks`
)

SELECT 
  Symbol,
  Date,
  Close,
  Volume,
  PreviousDayVolume,
  VolumeChange,
  VolumeChangePercent
FROM 
  VolumeAnalysis
ORDER BY 
  Symbol, 
  Date;