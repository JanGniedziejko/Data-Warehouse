USE DW;
GO

IF OBJECT_ID('vETLDimClassesData') IS NOT NULL 
    DROP VIEW vETLDimClassesData;
GO 

CREATE VIEW vETLDimClassesData
AS
SELECT DISTINCT
	Class_ID,
    Starting_Year = 'Between '+ CAST([Starting_Year] AS varchar(4)) + ' and '+ CAST(([Starting_Year] + 1) AS varchar(4)),
    Profile
FROM db.dbo.Classes;
GO



MERGE INTO DimClasses AS TT
USING vETLDimClassesData AS ST
ON TT.Starting_Year_Range = ST.Starting_Year
   AND TT.Profile = ST.Profile
WHEN NOT MATCHED THEN
    INSERT (Starting_Year_Range, Profile)
    VALUES (ST.Starting_Year, ST.Profile);

DROP VIEW vETLDimClassesData;
GO
