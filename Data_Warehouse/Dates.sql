Use DW
Declare @StartDate date; 
Declare @EndDate date;

-- Step b:  Fill the variable with values for the range of years needed
SELECT @StartDate = '2014-01-01', @EndDate = '2024-06-01';

-- Step c:  Use a while loop to add dates to the table
Declare @DateInProcess datetime = @StartDate;

While @DateInProcess <= @EndDate
	Begin
	--Add a row into the date dimension table for this date
		Insert Into [dbo].[DimDate] 
		( [Date]
		, [Year]
		, [Month]
		, [MonthNo]
		, [Semester]
		, [SemesterNo]
		)
		Values ( 
		  @DateInProcess -- [Date]
		  , Cast( Year(@DateInProcess) as varchar(4)) -- [Year]
		  , Cast( DATENAME(month, @DateInProcess) as varchar(10)) -- [Month]
		  ,FORMAT(@DateInProcess, 'MM') -- [MonthNo]
		  , CASE
		  		WHEN Month(@DateInProcess) IN (09,10,11,12,01) THEN 'Winter'
				ELSE 'Summer'
			END
		  , CASE
				WHEN Month(@DateInProcess) IN (09,10,11,12,01) THEN 1
				ELSE 2
			END
		);  
		-- Add a day and loop again
		Set @DateInProcess = DateAdd(month, 1, @DateInProcess);
	End
go
