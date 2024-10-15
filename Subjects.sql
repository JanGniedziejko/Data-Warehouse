USE DW;
GO

IF OBJECT_ID('vETLDimSubjectsData') IS NOT NULL DROP VIEW vETLDimSubjectsData;
GO 

CREATE VIEW vETLDimSubjectsData
AS
SELECT
	Subject_ID,
    Name,
    Syllabus,
    Level
FROM db.dbo.Subjects;
GO

MERGE INTO DimSubjects AS TT
USING vETLDimSubjectsData AS ST
ON TT.Name=ST.Name
   AND TT.Syllabus = ST.Syllabus
   AND TT.Level = ST.Level
WHEN NOT MATCHED THEN
	INSERT(Name, Syllabus, Level)
	VALUES (ST.Name, ST.Syllabus, ST.Level);


DROP VIEW vETLDimSubjectsData;
