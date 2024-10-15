USE DW;
GO


If (object_id('dbo.StudentTemp') is not null) DROP TABLE dbo.StudentTemp
; 
CREATE TABLE dbo.StudentTemp (
    Student_ID INT PRIMARY KEY,
    Adress VARCHAR(400),
    school VARCHAR(400),
    avg_exam INT,
    avg_grade DECIMAL(2,1),
    phone VARCHAR(12) CHECK (phone LIKE '[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]'),
    phone2 VARCHAR(12) CHECK (phone2 LIKE '[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]'),
	Family_Status VARCHAR(20)
);
BULK INSERT dbo.StudentTemp
FROM 'C:\Users\domin\OneDrive\Desktop\ex\Excel\Sheet1-TS1.csv'
WITH (
    FIELDTERMINATOR = '|',  
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

BULK INSERT dbo.StudentTemp
FROM 'C:\Users\domin\OneDrive\Desktop\ex\Excel\Sheet1-TS2.csv'
WITH (
    FIELDTERMINATOR = '|',  
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

IF OBJECT_ID('vETLDimStudentsData') IS NOT NULL DROP VIEW vETLDimStudentsData;
GO

CREATE VIEW vETLDimStudentsData
AS
SELECT DISTINCT
    d1.Student_ID, d1.Name, d1.Surname, d1.Gender, d1.Birth_date, d2.Family_Status
FROM db.dbo.Students as d1
JOIN dbo.StudentTemp as d2 ON d1.Student_ID = d2.Student_ID;
GO

MERGE INTO DimStudents AS TT
USING vETLDimStudentsData AS ST
ON TT.Name = ST.Name
   AND TT.Surname = ST.Surname
   AND TT.Gender = ST.Gender
   AND TT.Birth_date = ST.Birth_date
   AND TT.Family_Status=ST.Family_Status
WHEN NOT MATCHED THEN
    INSERT (Name, Surname, Gender,Birth_date, Family_Status)
    VALUES (ST.Name, ST.Surname, ST.Gender, ST.Birth_date, ST.Family_Status);

DROP VIEW vETLDimStudentsData;
GO
If (object_id('dbo.StudentTemp') is not null) DROP TABLE dbo.StudentTemp
; 
--update 
