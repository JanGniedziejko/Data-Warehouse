USE DW;
GO

If (object_id('dbo.TeacherTemp') is not null) DROP TABLE dbo.TeacherTemp;  
CREATE TABLE dbo.TeacherTemp (
    Teacher_ID INT PRIMARY KEY,
    Salary INT ,
    Adress VARCHAR(400),
    phone VARCHAR(12) CHECK (phone LIKE '[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]'),
    school VARCHAR(255),
	employment date 
 );
BULK INSERT dbo.TeacherTemp
FROM 'C:\Users\domin\OneDrive\Desktop\ex\Excel\Sheet2-TS1.csv'
WITH (
    FIELDTERMINATOR = '|',  
    ROWTERMINATOR = '\n',
	FIRSTROW = 2
);
BULK INSERT dbo.TeacherTemp
FROM 'C:\Users\domin\OneDrive\Desktop\ex\Excel\Sheet2-TS2.csv'
WITH (
    FIELDTERMINATOR = '|',  
    ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

IF OBJECT_ID('vETLDimTeachersData') IS NOT NULL DROP VIEW vETLDimTeachersData;
GO 

CREATE VIEW vETLDimTeachersData
AS
SELECT
	d1.Teacher_ID, d1.Name, d1.Surname, d1.Gender, d1.Education_level,
    Teaching_method = CASE
                            WHEN d1.Teaching_method = 'M' THEN 'Mass'
                            WHEN d1.Teaching_method = 'I' THEN 'Individual'
                            WHEN d1.Teaching_method = 'G' THEN 'Group'
                        END,
	Salary_range= CASE 
                            WHEN d2.Salary<5000 THEN 'low salary'
                            WHEN d2.Salary>=5000 AND d2.Salary<6000 THEN 'medium salary'
                            WHEN d2.Salary>=6000 THEN 'high salary'
                        END,
	Year_of_Employment = YEAR(d2.employment)
FROM db.dbo.Teachers as d1
JOIN dbo.TeacherTemp as d2 ON d1.Teacher_ID = d2.Teacher_ID;
go


MERGE INTO DimTeachers AS TT
USING vETLDimTeachersData AS ST
ON TT.Name = ST.Name
   AND TT.Surname = ST.Surname
WHEN NOT MATCHED THEN
    INSERT (Name, Surname, Gender, Education_level, Teaching_method, Salary_range, Year_of_Employment,Is_current)
	VALUES (ST.Name, ST.Surname, ST.Gender, ST.Education_level, ST.Teaching_method,  ST.Salary_range, ST.Year_of_Employment,1)
	WHEN Not Matched By Source
				Then
					DELETE;

Drop View vETLDimTeachersData;

If (object_id('dbo.TeacherTemp') is not null) DROP TABLE dbo.TeacherTemp
