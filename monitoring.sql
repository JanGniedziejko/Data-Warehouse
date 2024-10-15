USE DW;
GO

DROP PROCEDURE IF EXISTS MergeETLFMonitoring;
GO



IF OBJECT_ID('vETLFMonitoring') IS NOT NULL 
    DROP VIEW vETLFMonitoring;
GO

CREATE VIEW vETLFMonitoring
AS
SELECT 
    *
FROM (
    SELECT 
		CourseKey = dimcourses.Course_ID,
		StudentKey = dimstudents.Student_ID,
		DateKey = dimdate.Date_ID,
		ClassKey = dimclass.Class_ID,
		TeacherKey = dimteachers.Teacher_ID,
		SubjectKey = dimsubjects.Subject_ID,
        Time_taken = dbexams.Time_taken,
        Result = dbexams.Result,
		Hours_conducted = dblessons.Hours_conducted,
		Hours_attended = dbattendance.HoursAttended,
		Attendance_rate = ROUND(CAST(HoursAttended AS float) / CAST(Hours_conducted AS float),2)
		

    FROM 
        db.dbo.Exams AS dbexams
	JOIN db.dbo.Students AS dbstudents ON dbstudents.Student_ID = dbexams.Student
	JOIN db.dbo.Courses AS dbcourses ON dbcourses.Course_ID = dbexams.Course
	JOIN db.dbo.Lessons AS dblessons ON dblessons.Course = dbcourses.Course_ID
	JOIN db.dbo.Attendance AS dbattendance ON dbattendance.Student = dbstudents.Student_ID and dbattendance.Lesson = dblessons.Lesson_ID
	JOIN db.dbo.Classes AS dbclasses ON dbclasses.Class_ID = dbstudents.Class
	JOIN db.dbo.Teachers AS dbteachers ON dbteachers.Teacher_ID = dbcourses.Teacher
	JOIN db.dbo.Subjects AS dbsubjects ON dbsubjects.Subject_ID = dbcourses.Subject
	
	JOIN dbo.DimClasses AS dimclass ON dbclasses.Profile = dimclass.Profile AND 'Between '+ CAST(dbclasses.Starting_Year AS varchar(4)) + ' and '+ CAST((dbclasses.Starting_Year + 1) AS varchar(4)) = dimclass.[Starting_Year_Range]
    JOIN dbo.DimCourses as dimcourses  ON 'C'+CAST(dbcourses.Course_ID AS varchar(8))+'-'+CAST(dbcourses.Year AS varchar(4)) = dimcourses.CID
	JOIN dbo.DimStudents AS dimstudents ON dimstudents.Name = dbstudents.Name AND dimstudents.Surname = dbstudents.Surname AND dimstudents.Gender = dbstudents.Gender AND dimstudents.Birth_date = dbstudents.Birth_date
    JOIN dbo.DimTeachers AS dimteachers ON dimteachers.Name = dbteachers.Name AND dimteachers.Surname = dbteachers.Surname AND SUBSTRING(dimteachers.Teaching_method, 1, 1) = dbteachers.Teaching_method AND dimteachers.Gender = dbteachers.Gender AND dimteachers.Education_level = dbteachers.Education_level  
    JOIN dbo.DimSubjects AS dimsubjects ON dimsubjects.Name = dbsubjects.Name AND dimsubjects.Level = dbsubjects.Level AND dimsubjects.Syllabus = dbsubjects.Syllabus
	JOIN dbo.DimDate AS dimdate ON dimdate.MonthNo = dbexams.Date AND dimdate.Year = dbcourses.Year
	WHERE dbexams.Date = dblessons.Month AND dimteachers.Is_current=1
) AS Subquery;

GO


CREATE PROCEDURE MergeETLFMonitoring
AS
BEGIN
    MERGE INTO FaMonitoring AS TT
    USING vETLFMonitoring AS ST
    ON 
        TT.Studentkey = ST.Studentkey
        AND TT.Coursekey = ST.Coursekey
        AND TT.Subjectkey = ST.Subjectkey
        AND TT.Teacherkey = ST.Teacherkey
        AND TT.Classkey = ST.Classkey
		AND TT.Datekey=ST.Datekey
        AND TT.Time_taken = ST.Time_taken
        AND TT.Hours_conducted = ST.Hours_conducted
        AND TT.Hours_attended = ST.Hours_attended
        AND TT.Attendance_rate = ST.Attendance_rate
        AND TT.Result = ST.Result
    WHEN NOT MATCHED THEN
        INSERT (Studentkey, Coursekey, Subjectkey, Teacherkey, Classkey,Datekey, Time_taken, Hours_conducted, Hours_attended, Attendance_rate, Result)
        VALUES (ST.Studentkey, ST.Coursekey, ST.Subjectkey, ST.Teacherkey, ST.Classkey, ST.Datekey, ST.Time_taken, ST.Hours_conducted, ST.Hours_attended, ST.Attendance_rate, ST.Result);
END;
GO

EXEC MergeETLFMonitoring;
GO
