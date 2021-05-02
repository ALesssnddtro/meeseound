import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()
conn.execute("PRAGMA foreign_keys = 1")

# Create table
c.execute('''CREATE TABLE Users
             (UserID int PRIMARY KEY,
             LastName text,
             FirstName text, 
             DoB text, 
             Weight int, 
             Height int,
             Gender text)''')

c.execute('''CREATE TABLE Sessions
             (SessionID int PRIMARY KEY,
             UserID time,
             StartDate date,
             StartTime time,
             EndDate date,
             EndTime int,
             FOREIGN KEY (UserID) REFERENCES Users(UserID))''')

#text 0 is false 1 is true
c.execute('''CREATE TABLE SessionDetails
             (SessionDetailsID int PRIMARY KEY,
             SessionID int,
             ExerciseID int,
             Sets int,
             Reps int,
             IsPlanned text,
             Place text,
             FOREIGN KEY (SessionID) REFERENCES Sessions(SessionID),
             FOREIGN KEY (ExerciseID) REFERENCES Exercises(ExerciseID))''')



c.execute('''CREATE TABLE Exercises
             (ExerciseID int PRIMARY KEY,
             ExerciseName text,
             Type text)''')

#users
c.execute('''INSERT INTO Users(UserID, LastName, FirstName, DoB, Weight, Height, Gender) 
VALUES (1, 'Davila', 'Nancy', '2003-01-02', 56, 126, 'Female')''')

c.execute('''INSERT INTO Users(UserID, LastName, FirstName, DoB, Weight, Height, Gender) 
VALUES (2, 'Fuller', 'Andrew', '2001-12-01', 47, 134, 'Male')''')

c.execute('''INSERT INTO Users(UserID, LastName, FirstName, DoB, Weight, Height, Gender) 
VALUES (3, 'Buchanan', 'Steven', '2006-11-31', 78, 141, 'Male')''')

#sessions
c.execute('''INSERT INTO Sessions(SessionID, UserID, StartDate, StartTime, EndDate, EndTime)
VALUES (1, 1, "2018-05-26", "06:45:00", "2018-05-26", "07:45:00")''')
c.execute('''INSERT INTO Sessions(SessionID, UserID, StartDate, StartTime, EndDate, EndTime)
VALUES (2, 1, "2016-11-11", "02:15:00", "2016-11-11", "02:45:00")''')

c.execute('''INSERT INTO Sessions(SessionID, UserID, StartDate, StartTime, EndDate, EndTime)
VALUES (3, 2, "2016-11-11", "02:15:00", "2016-11-11", "02:45:00")''')
c.execute('''INSERT INTO Sessions(SessionID, UserID, StartDate, StartTime, EndDate, EndTime)
VALUES (4, 2, "2016-11-11", "02:15:00", "2016-11-11", "02:45:00")''')

c.execute('''INSERT INTO Sessions(SessionID, UserID, StartDate, StartTime, EndDate, EndTime)
VALUES (5, 3, "2014-07-30", "11:55:00", "2014-07-30", "02:55:00")''')
c.execute('''INSERT INTO Sessions(SessionID, UserID, StartDate, StartTime, EndDate, EndTime)
VALUES (6, 3, "2016-11-11", "02:15:00", "2016-11-11", "02:45:00")''')

#exercises
c.execute('''INSERT INTO Exercises(ExerciseID, ExerciseName, Type)
VALUES (1, "Incline Bench", "Push-day")''')

c.execute('''INSERT INTO Exercises(ExerciseID, ExerciseName, Type)
VALUES (2, "Pullovers", "Pull-day")''')

c.execute('''INSERT INTO Exercises(ExerciseID, ExerciseName, Type)
VALUES (3, "Squats", "Leg-day")''')

#sessiondetails
c.execute('''INSERT INTO SessionDetails(SessionDetailsID, SessionID, ExerciseID, Sets, Reps, IsPlanned, Place)
VALUES (1, 2, 3, 3, 12, "True", "home")''')

c.execute('''INSERT INTO SessionDetails(SessionDetailsID, SessionID, ExerciseID, Sets, Reps, IsPlanned, Place)
VALUES (2, 3, 1, 4, 10, "True", "gym")''')

c.execute('''INSERT INTO SessionDetails(SessionDetailsID, SessionID, ExerciseID, Sets, Reps, IsPlanned, Place)
VALUES (3, 1, 2, 2, 8, "False", "home")''')

c.execute('''INSERT INTO SessionDetails(SessionDetailsID, SessionID, ExerciseID, Sets, Reps, IsPlanned, Place)
VALUES (4, 4, 3, 3, 12, "True", "macdonalds")''')

c.execute('''INSERT INTO SessionDetails(SessionDetailsID, SessionID, ExerciseID, Sets, Reps, IsPlanned, Place)
VALUES (5, 5, 1, 4, 10, "True", "kfc")''')

c.execute('''INSERT INTO SessionDetails(SessionDetailsID, SessionID, ExerciseID, Sets, Reps, IsPlanned, Place)
VALUES (6, 6, 2, 2, 8, "False", "street")''')

c.execute('''INSERT INTO SessionDetails(SessionDetailsID, SessionID, ExerciseID, Sets, Reps, IsPlanned, Place)
VALUES (7, 6, 3, 3, 3, "False", "floor")''')




conn.commit()

for row in c.execute('SELECT * FROM Users'):
        print(row)

print("#----------------------------------------------------------------------------#")

for row in c.execute('SELECT * FROM Sessions'):
        print(row)

print("#----------------------------------------------------------------------------#")

for row in c.execute('SELECT * FROM SessionDetails'):
        print(row)

print("#----------------------------------------------------------------------------#")

for row in c.execute('SELECT * FROM Exercises'):
        print(row)

        

test1 = ("SELECT Sessions.SessionID, Sessions.StartTime, Sessions.EndTime, SessionDetails.Sets, SessionDetails.Reps, SessionDetails.Sets, SessionDetails.Place, SessionDetails.IsPlanned, Exercises.ExerciseName FROM Sessions INNER JOIN SessionDetails ON Sessions.SessionID = SessionDetails.SessionID INNER JOIN Exercises ON SessionDetails.ExerciseID = Exercises.ExerciseID")

c.execute(test1)
rows = c.fetchall()
print(rows[0])
print(rows[1])