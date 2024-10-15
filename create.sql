CREATE DATABASE SchoolNEW;
GO

USE SchoolNEW;
GO

CREATE TABLE Teachers (
    Teacher_ID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL CHECK(Name LIKE '%[A-Za-z ]%'),
    Surname VARCHAR(50) CHECK(Surname LIKE '%[A-Za-z ]%'),
    Gender VARCHAR(6) CHECK(Gender IN ('Male', 'Female')),
   Education_level VARCHAR(40) CHECK(Education_level IN ('High School', 'Associat Degree', 'Bachelor Degree', 'Master Degree', 'Doctorate Degree',
             'Vocational/Technical Training', 'Professional Certification')),
    Office_No VARCHAR(3) CHECK(Office_No BETWEEN '000' AND '999'),
	Teaching_method VARCHAR(1) CHECK(Teaching_method IN ('M', 'G', 'I'))
);

CREATE TABLE Classes (
    Class_ID INT PRIMARY KEY,
    Starting_Year INT,
    Profile VARCHAR(50)
);
GO
CREATE TABLE Subjects (
    Subject_ID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL CHECK(Name LIKE '%[A-Za-z ]%'),
    Syllabus VARCHAR(255) CHECK(Syllabus LIKE '%.pdf'),
    Level VARCHAR(9) NOT NULL CHECK(Level IN ('Basic', 'Expanded'))
);
GO
CREATE TABLE Courses (
    Course_ID INT PRIMARY KEY,
    Year INT NOT NULL ,
    Subject INT REFERENCES Subjects,
	Teacher INT REFERENCES Teachers,
	Class INT REFERENCES Classes
);
GO
CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL CHECK(Name LIKE '%[A-Za-z ]%'),
    Surname VARCHAR(50) CHECK(Surname LIKE '%[A-Za-z ]%'),
    Gender VARCHAR(6) CHECK(Gender IN ('Male', 'Female')),
    Birth_date DATE,
    Class INT REFERENCES Classes
);
GO
CREATE TABLE Exams (
    Exam_ID INT PRIMARY KEY,
    Date INT,
    Result INT CHECK(Result<=100),
    Type VARCHAR(1) CHECK(Type IN ('M', 'F')),
    Student INT REFERENCES Students,
    Course INT REFERENCES Courses
);

CREATE TABLE Lessons (
    Lesson_ID INT PRIMARY KEY,
    Month INT,
	YEAR INT,
    Hours INT CHECK(Hours > 0 ),
    Room_No VARCHAR(3) CHECK(Room_No BETWEEN '000' AND '999'),
    Course INT REFERENCES Courses
);
GO
CREATE TABLE Level_Of_Satisfaction (
    Student_ID INT REFERENCES Students,
    Year INT,
    Satisfaction_level INT CHECK(Satisfaction_level BETWEEN 0 AND 10),
    PRIMARY KEY (Student_ID, Year)
);
GO
CREATE TABLE Attendance (
    Student INT REFERENCES Students,
    Lesson INT  REFERENCES Lessons,
	HoursAttended INT
    PRIMARY KEY (Student, Lesson),
);
GO
