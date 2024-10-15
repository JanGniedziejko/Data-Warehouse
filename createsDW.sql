USE DW
GO

CREATE TABLE DimTeachers (
    Teacher_ID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(255) NOT NULL CHECK(Name LIKE '%[A-Za-z ]%'),
    Surname VARCHAR(255) CHECK(Surname LIKE '%[A-Za-z ]%'),
    Gender VARCHAR(6) CHECK(Gender IN ('Male', 'Female')),
    Education_level VARCHAR(30),
    Teaching_method VARCHAR(10) CHECK(Teaching_method IN ('Mass', 'Group', 'Individual')),
    Salary_range VARCHAR(15) CHECK (Salary_range IN ('low salary','medium salary','high salary')),
    Year_of_Employment VARCHAR(4),
	Is_current BIT
);
GO
CREATE TABLE DimSubjects (
    Subject_ID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(255) NOT NULL CHECK(Name LIKE '%[A-Za-z ]%'),
    Syllabus VARCHAR(255) CHECK(Syllabus LIKE '%.pdf'),
    Level VARCHAR(9) NOT NULL CHECK(Level IN ('Basic', 'Expanded'))
);
GO
CREATE TABLE DimCourses (
    Course_ID INT IDENTITY(1,1) PRIMARY KEY,
	CID VARCHAR(12),
    Year_range VARCHAR(24) NOT NULL,
	End_year int
);
GO
CREATE TABLE DimClasses (
    Class_ID INT IDENTITY(1,1) PRIMARY KEY,
    Starting_Year_Range VARCHAR(40),
    Profile VARCHAR(40)
);
GO
CREATE TABLE DimStudents (
    Student_ID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(255) NOT NULL CHECK(Name LIKE '%[A-Za-z ]%'),
    Surname VARCHAR(255) CHECK(Surname LIKE '%[A-Za-z ]%'),
    Gender VARCHAR(10) CHECK(Gender IN ('Male', 'Female')),
	Birth_date DATE,
    Family_Status VARCHAR(20) CHECK(Family_Status IN ('Full family','Separated family','One parent','No parents'))
 );
GO
CREATE TABLE DimDate(
    Date_ID INT IDENTITY(1,1) PRIMARY KEY,
    Date Date,
    Year VARCHAR(4),
    Month VARCHAR(10) CHECK (Month IN ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')),
    MonthNo INT CHECK(MonthNo<13),
    Semester VARCHAR(7) CHECK (SEMESTER IN ('Winter','Summer')),
    SemesterNo INT CHECK(SemesterNo = 1 OR SemesterNo = 2)
);
GO

CREATE TABLE FaMonitoring (
	Studentkey INT FOREIGN KEY REFERENCES DimStudents,
    Coursekey INT FOREIGN KEY REFERENCES DimCourses,
    Subjectkey INT FOREIGN KEY REFERENCES DimSubjects,
    Teacherkey INT FOREIGN KEY REFERENCES DimTeachers,
    Classkey INT FOREIGN KEY REFERENCES DimClasses,
    Datekey INT FOREIGN KEY REFERENCES DimDate,
    Time_taken INT CHECK (Time_taken >= 0 AND Time_taken <=360),
	Hours_conducted INT,
    Hours_attended INT,
    Attendance_rate DECIMAL(3,2),
    Result FLOAT,
    CONSTRAINT composite_pk PRIMARY KEY (
		Studentkey,
		Coursekey, 
		Subjectkey, 
		Teacherkey, 
		Classkey, 
		Datekey
		)
);
GO
CREATE TABLE FaSatisfaction(
    Studentkey INT FOREIGN KEY REFERENCES DimStudents,
    Coursekey INT FOREIGN KEY REFERENCES DimCourses,
    Satisfaction_level INT,
	CONSTRAINT satisfaction_pk PRIMARY KEY (Studentkey, Coursekey)
);