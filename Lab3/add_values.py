import sqlite3


def values():
    con = sqlite3.connect("Lab3/university.db")
    cur = con.cursor()
    cur.execute(values_department())
    cur.execute(values_grade())
    cur.execute(values_lecturer())
    cur.execute(values_attends())
    cur.execute(values_student())
    cur.execute(values_studentGrade())
    cur.execute(values_studentGroup())
    cur.execute(values_subject())
    cur.execute(values_university())


def values_department():
    return """
        INSERT INTO `department` (`departmentID`, `name`, `universityID`) VALUES
            (877769, 'Wydział Mechaniczno Elektryczny', 657787),
            (877883, 'Wydział Nauk Społecznych', 657787);

    """


def values_grade():
    return """
        INSERT INTO `grade` (`gradeID`, `grade`) VALUES
            (1, 2),
            (2, 3),
            (3, 3.5),
            (4, 4),
            (5, 4.5),
            (6, 5);
    """


def values_lecturer():
    return """
        INSERT INTO `lecturer` (`lecturerID`, `firstName`, `lastName`, `mail`, `scienceTitle`, `subjectID`) VALUES
            (1, 'Jan', 'Kowalski', 'j.kowalski@amw.gdynia.pl', 'dr.', 2147483647),
            (2, 'Jerzy', 'Plusik', 'j.plusik@amw.gdynia.pl', 'prof.', 10997116),
            (3, 'Adam', 'Nowak', 'a.nowak@amw.gdynia.pl', 'prof. ', 102105122),
            (4, 'Elliot', 'Alderson', 'e.alderson@amw.gdynia.pl', 'mgr. inż.', 8079),
            (5, 'Włodzimierz', 'Myśliwy', 'w.mysliwy@amw.gdynia.pl', 'dr.', 70105108),
            (6, 'Filip', 'Razer', 'f.razer@amw.gdynia.pl', 'prof.', 658375),
            (7, 'Damian', 'Doker', 'd.doker@amw.gdynia.pl', 'mgr. inż', 738373),
            (8, 'Renata', 'Jabłkowska', 'r.jablkowska@amw.gdynia.pl', 'dr.', 8080);
    """


def values_attends():
    return """
        INSERT INTO `attends` (`groupID`, `subjectID`) VALUES
            (210, 10997116),
            (210, 102105122),
            (211, 8080),
            (211, 70105108),
            (211, 97110103),
            (212, 97110103),
            (212, 2147483647),
            (215, 8079),
            (215, 658375),
            (215, 738373),
            (220, 102105122);
    """


def values_student():
    return """
        INSERT INTO `student` (`albumNumber`, `firstName`, `lastName`, `averageGrade`, `mail`, `groupID`) VALUES
            (2137, 'Papież', 'Polak', 4.75, 'p.polak@student.amw.gdynia.pl', 211),
            (20000, 'Karol', 'Wojtyła', 3.5, 'k.wojtyla@student.amw.gdynia.pl', 211),
            (20001, 'Jadwiga', 'Hymel', 3, 'j.hymel@student.amw.gdynia.pl', 211),
            (20002, 'Mariusz', 'Pudzianowski', 3.5, 'm.pudzianowski@student.amw.gdynia.pl', 215),
            (20003, 'Kamil', 'Ślimak', 4.33333, 'k.slimak@student.amw.gdynia.pl', 215),
            (20004, 'Anna Maria', 'Wesołowska', 3.5, 'a.wesolowska@student.amw.gdynia.pl', 211),
            (20005, 'Korneliusz', 'Kołodziej', NULL, 'k.kolodziej@student.amw.gdynia.pl', 212),
            (20006, 'Natan', 'Mróz', 2.83333, 'n.mroz@student.amw.gdynia.pl', 215),
            (20007, 'Andrzej', 'Wójcik', 3.33333, 'a.wojcik@student.amw.gdynia.pl', 215);
    """


def values_studentGrade():
    return """
        INSERT INTO `studentGrade` (`studentGradeID`, `gradeID`, `albumNumber`, `lecturerID`) VALUES
            (1, 3, 20002, 6),
            (2, 4, 20002, 4),
            (3, 2, 20002, 7),
            (4, 6, 20003, 6),
            (5, 3, 20003, 7),
            (6, 5, 20003, 4),
            (7, 1, 20006, 4),
            (8, 2, 20006, 6),
            (9, 3, 20006, 7),
            (10, 1, 20007, 7),
            (11, 3, 20007, 6),
            (12, 5, 20007, 4),
            (13, 5, 2137, 5),
            (14, 6, 2137, 8),
            (15, 1, 20000, 8),
            (16, 6, 20000, 5),
            (17, 4, 20001, 8),
            (18, 1, 20001, 5),
            (19, 4, 20004, 8),
            (20, 2, 20004, 5);
    """


def values_studentGroup():
    return """
        INSERT INTO `studentGroup` (`groupID`, `faculty`, `departmentID`) VALUES
            (210, 'Elektronika', 877769),
            (211, 'Psychologia', 877883),
            (212, 'Pedagogika', 877883),
            (215, 'Informatyka', 877769),
            (220, 'Mechatronika', 877769);
    """


def values_subject():
    return """
        INSERT INTO `subject` (`subjectID`, `name`, `hours`, `typeOfExam`) VALUES
            (8079, 'Programowanie Obiektowe', 80, 'egzamin pisemny'),
            (8080, 'Podstawy Psychologii', 35, 'egzamin ustny'),
            (658375, 'Architektura Systemów Komputerowych', 75, 'egzamin ustny'),
            (738373, 'Integracja Systemów Informatycznych', 80, 'kolokwium zaliczeniowe'),
            (10997116, 'Matematyka', 60, 'egzamin pisemny'),
            (70105108, 'Filozofia', 35, 'egzamin ustny'),
            (97110103, 'język angielski', 30, 'kolokwium zaliczeniowe'),
            (102105122, 'Fizyka', 60, 'egzamin pisemny'),
            (2147483647, 'Statystyka', 45, 'kolokwium zaliczeniowe');
    """


def values_university():
    return """
        INSERT INTO `university` (`universityID`, `name`, `address`, `university_type`) VALUES
            (8071, 'Politechnika Gdańska', 'Gdańsk, ul. Gabriela Narutowicza 11/12', 'Politechnika'),
            (8571, 'Uniwersytet Gdański', 'Gdańsk, ul. Jana Bażyńskiego 8', 'Uniwersytet'),
            (657787, 'Akademia Marynarki Wojennej', 'Gdynia, ul. Śmidowicza 69', 'Akademia');
    """
