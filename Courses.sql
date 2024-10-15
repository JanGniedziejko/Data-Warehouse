USE DW;
GO

IF OBJECT_ID('vETLDimCoursesData') IS NOT NULL 
    DROP VIEW vETLDimCoursesData;
GO 

CREATE VIEW vETLDimCoursesData
AS
SELECT DISTINCT
	CID = 'C'+CAST([Course_ID] AS varchar(8))+'-'+CAST([Year] AS varchar(4)),
    Year_range = 'Between '+ CAST([Year] AS varchar(4)) + ' and '+ CAST(([Year] + 1) AS varchar(4)),
	End_year=[Year] + 1
FROM db.dbo.Courses;
GO


MERGE INTO DimCourses AS TT
USING vETLDimCoursesData AS ST
ON TT.CID=ST.CID
WHEN NOT MATCHED THEN
    INSERT (CID, Year_range,End_year)
    VALUES (ST.CID, ST.Year_range,ST.End_year);

DROP VIEW vETLDimCoursesData;
GO
