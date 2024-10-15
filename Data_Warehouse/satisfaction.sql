USE DW;
GO

IF OBJECT_ID('vETLSatisfaction') IS NOT NULL 
    DROP VIEW vETLSatisfaction;
GO

CREATE VIEW vETLSatisfaction
AS
SELECT dbsatisfaction.Satisfaction_level,
       Studentkey = dimStudents.Student_ID, 
       Coursekey = dimcourses.Course_ID,
	   year=CONVERT(INT, SUBSTRING(dimcourses.Year_range, 9, 4))
FROM db.dbo.Level_Of_Satisfaction as dbsatisfaction
JOIN db.dbo.Students as dbstudents on dbsatisfaction.Student = dbstudents.Student_ID
JOIN db.dbo.Courses as dbcourses on dbsatisfaction.Course = dbcourses.Course_ID
JOIN dbo.DimStudents as dimStudents on dbstudents.Name = dimStudents.Name 
                                     and dbstudents.Gender = dimStudents.Gender 
                                     and dbstudents.Surname = dimStudents.Surname
									 and dbstudents.Birth_date=dimStudents.Birth_date
JOIN dbo.DimCourses as dimcourses  ON 'C'+CAST(dbcourses.Course_ID AS varchar(8))+'-'+CAST(dbcourses.Year AS varchar(4)) = dimcourses.CID --and dimcourses.Year_range = 'Between ' + CAST(dbcourses.Year AS varchar(4)) + ' and ' + CAST((dbcourses.Year + 1) AS varchar(4))
GO


MERGE INTO FaSatisfaction as TT
	USING vETLSatisfaction as ST
		ON 	
			TT.Studentkey = ST.Studentkey
		AND TT.Coursekey = ST.Coursekey
		AND TT.Satisfaction_level = ST.Satisfaction_level
			WHEN Not Matched
				THEN
					INSERT(Studentkey, Coursekey, Satisfaction_level)
					Values (
					ST.Studentkey, ST.Coursekey, ST.Satisfaction_level)
			;

Drop view vETLSatisfaction;

-- select * from FBookSales;

