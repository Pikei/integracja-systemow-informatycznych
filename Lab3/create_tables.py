import sqlite3


def tables():
    con = sqlite3.connect("Lab3/university.db")
    cur = con.cursor()
    cur.execute(create_university())
    cur.execute(create_department())
    cur.execute(create_subject())
    cur.execute(create_lecturer())
    cur.execute(create_grade())
    cur.execute(create_student())
    cur.execute(create_attends())
    cur.execute(create_studentGrade())
    cur.execute(create_studentGroup())


def create_university():
    return """
        CREATE TABLE university
        (
            universityID INT NOT NULL,
            name VARCHAR(100) NOT NULL,
            address VARCHAR(100) NOT NULL,
            university_type VARCHAR(50) NOT NULL,
            PRIMARY KEY (`universityID`)
        );
    """


def create_department():
    return """
        CREATE TABLE department
        (
            departmentID INT NOT NULL,
            name VARCHAR(100) NOT NULL,
            universityID INT NOT NULL,
            PRIMARY KEY (departmentID),
            FOREIGN KEY (universityID) REFERENCES university(universityID)
        );
    """


def create_studentGroup():
    return """
        CREATE TABLE `studentGroup` (
            `groupID` int(11) NOT NULL,
            `faculty` varchar(100) NOT NULL,
            `departmentID` int(11) NOT NULL,
            PRIMARY KEY (`groupID`),
            FOREIGN KEY (`departmentID`) REFERENCES `department` (`departmentID`)
        )
    """


def create_student():
    return """
       CREATE TABLE student
        (
            albumNumber INT NOT NULL,
            firstName VARCHAR(50) NOT NULL,
            lastName VARCHAR(100) NOT NULL,
            averageGrade FLOAT DEFAULT NULL,
            mail INT NOT NULL,
            groupID INT,
            PRIMARY KEY (`albumNumber`),
            FOREIGN KEY (`groupID`) REFERENCES `studentGroup` (`groupID`)
        );
    """


def create_subject():
    return """
        CREATE TABLE `subject` (
          `subjectID` int(11) NOT NULL,
          `name` varchar(100) NOT NULL,
          `hours` int(11) NOT NULL,
          `typeOfExam` varchar(50) NOT NULL,
          PRIMARY KEY (`subjectID`)
        );
    """


def create_lecturer():
    return """
        CREATE TABLE `lecturer` (
            `lecturerID` int(11) NOT NULL,
            `firstName` varchar(50) NOT NULL,
            `lastName` varchar(100) NOT NULL,
            `mail` varchar(100) NOT NULL,
            `scienceTitle` varchar(100) NOT NULL,
            `subjectID` int(11) NOT NULL,
            PRIMARY KEY (lecturerID),
            FOREIGN KEY (subjectID) REFERENCES subject(subjectID)
        );
    """


def create_grade():
    return """
        CREATE TABLE `grade` (
            `gradeID` int(11) NOT NULL,
            `grade` float NOT NULL,
            PRIMARY KEY (gradeID)
        );
    """


def create_attends():
    return """
       CREATE TABLE attends
        (
            subjectID INT NOT NULL,
            groupID INT NOT NULL,
            PRIMARY KEY (`groupID`,`subjectID`),
            FOREIGN KEY (`groupID`) REFERENCES `studentGroup` (`groupID`),
            FOREIGN KEY (`subjectID`) REFERENCES `subject` (`subjectID`)
        );
    """


def create_studentGrade():
    return """
        CREATE TABLE `studentGrade` (
          `studentGradeID` int(11) NOT NULL,
          `gradeID` int(11) NOT NULL,
          `albumNumber` int(11) NOT NULL,
          `lecturerID` int(11) NOT NULL,
          PRIMARY KEY (`studentGradeID`),
          FOREIGN KEY (`gradeID`) REFERENCES `grade` (`gradeID`),
          FOREIGN KEY (`albumNumber`) REFERENCES `student` (`albumNumber`),
          FOREIGN KEY (`lecturerID`) REFERENCES `lecturer` (`lecturerID`)
        )
    """
