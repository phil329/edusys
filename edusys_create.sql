# drop database edusys;
create database edusys;
use edusys;
show databases;
CREATE TABLE IF NOT EXISTS `AdminInfo` (
`AdminNo`  int(7)  NOT NULL AUTO_INCREMENT ,
`AdminName`  varchar(20) CHARACTER SET utf8mb4 NOT NULL ,
`AdminGender`  enum('女','男') CHARACTER SET utf8mb4 NOT NULL ,
`AdminBirthday`  date NOT NULL ,
`AdminPassword`  varchar(32) CHARACTER SET utf8mb4 NOT NULL DEFAULT '' COMMENT 'encrypted by base32' ,
PRIMARY KEY (`AdminNo`),
UNIQUE INDEX `AdminNo` (`AdminNo`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4
;


CREATE TABLE IF NOT EXISTS `CollegeInfo` (
`CollegeNo`  int(3) NOT NULL AUTO_INCREMENT,
`CollegeName`  varchar(40) CHARACTER SET utf8mb4 NOT NULL ,
PRIMARY KEY (`CollegeNo`, `CollegeName`),
UNIQUE INDEX `No` (`CollegeNo`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4
;

CREATE TABLE IF NOT EXISTS `SpecialityInfo` (
`SpecialityNo`  int(5) NOT NULL AUTO_INCREMENT ,
`SpecialityName`  varchar(40) CHARACTER SET utf8mb4 NOT NULL ,
`CollegeNo`  int(3) NOT NULL ,
PRIMARY KEY (`SpecialityNo`),
CONSTRAINT `SpeCollegeNo` FOREIGN KEY (`CollegeNo`) REFERENCES `CollegeInfo` (`CollegeNo`) ON DELETE RESTRICT ON UPDATE CASCADE,
UNIQUE INDEX `No` (`SpecialityNo`) USING BTREE 
)
;

CREATE TABLE IF NOT EXISTS `StudentInfo` (
`StudentNo`  int(7) NOT NULL AUTO_INCREMENT,
`StudentName`  varchar(20) CHARACTER SET utf8mb4 NOT NULL ,
`StudentGender`  enum('男','女') CHARACTER SET utf8mb4 NOT NULL ,
`StudentBirthday`  date NOT NULL ,
`CollegeNo`  int(3) NOT NULL ,
`SpecialityNo`  int(5) NOT NULL ,
`StudentPassword`  varchar(32) CHARACTER SET utf8mb4 NOT NULL DEFAULT '' COMMENT 'encrypted by base32' ,
PRIMARY KEY (`StudentNo`),
CONSTRAINT `StuCollegeNo` FOREIGN KEY (`CollegeNo`) REFERENCES `CollegeInfo` (`CollegeNo`) ON DELETE RESTRICT ON UPDATE CASCADE,
CONSTRAINT `StuSpecialityNo` FOREIGN KEY (`SpecialityNo`) REFERENCES `SpecialityInfo` (`SpecialityNo`) ON DELETE RESTRICT ON UPDATE CASCADE,
INDEX `StudentNo` (`StudentNo`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4
;

CREATE TABLE IF NOT EXISTS `TeacherInfo` (
`TeacherNo`  int(7) NOT NULL AUTO_INCREMENT,
`TeacherName`  varchar(20) NOT NULL ,
`TeacherGender`  enum('男','女') CHARACTER SET utf8mb4 NOT NULL ,
`TeacherBirthday`  date NOT NULL ,
`TeaCollegeNo`  int(3) NOT NULL ,
`TeacherPassword`  varchar(32) CHARACTER SET utf8mb4 NOT NULL DEFAULT '' COMMENT 'encrypted by base32' ,
PRIMARY KEY (`TeacherNo`),
CONSTRAINT `TeaCollegeNo` FOREIGN KEY (`TeaCollegeNo`) REFERENCES `CollegeInfo` (`CollegeNo`) ON DELETE RESTRICT ON UPDATE CASCADE,
INDEX `TeacherNo` (`TeacherNo`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4
;

CREATE TABLE IF NOT EXISTS `StartCourseApplication` (
`TeacherNo`  int(7) NOT NULL ,
`CourseName`  varchar(10) CHARACTER SET utf8mb4 NOT NULL ,
`Reason`  varchar(300) CHARACTER SET utf8mb4 NULL ,
`Status` enum('waiting','dismissed','passed') NOT NULL,
CONSTRAINT `StartCourseTeacherNo` FOREIGN KEY (`TeacherNo`) REFERENCES `TeacherInfo` (`TeacherNo`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `TeacherNo` (`TeacherNo`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4
;

CREATE TABLE IF NOT EXISTS `ClassroomInfo` (
`ClassroomNo`  int(4) NOT NULL AUTO_INCREMENT,
`ClassroomPosition`  varchar(40) NOT NULL ,
PRIMARY KEY (`ClassroomNo`),
INDEX `ClassroomNo` (`ClassroomNo`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4
;

CREATE TABLE IF NOT EXISTS `CourseInfo` (
`CourseNo`  int(9) NOT NULL AUTO_INCREMENT ,
`CourseName`  varchar(40) NOT NULL ,
`TeacherNo`  int(7) NULL ,
`CourseDay`  enum('1','2','3','4','5','6','7')  NULL ,
`CourseBeginNo`  int(2)  NULL ,
`CourseNums`  int(2)  NULL ,
`ClassroomNo`  int(4) NULL ,
PRIMARY KEY (`CourseNo`),
CONSTRAINT `CouTeacherNo` FOREIGN KEY (`TeacherNo`) REFERENCES `TeacherInfo` (`TeacherNo`) ON DELETE SET NULL ON UPDATE CASCADE,
CONSTRAINT `CouClassroomNo` FOREIGN KEY (`ClassroomNo`) REFERENCES `ClassroomInfo` (`ClassroomNo`) ON DELETE SET NULL ON UPDATE CASCADE,
INDEX `CourseNo` (`CourseNo`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4
;

CREATE TABLE IF NOT EXISTS `TeachCourseApplication` (
`TeacherNo`  int(7) NOT NULL ,
`CourseNo`  int(9) NOT NULL ,
`Reason`  varchar(300) NOT NULL ,
`Status` enum('waiting','dismissed','passed') NOT NULL,
CONSTRAINT `TeaTeacherNo` FOREIGN KEY (`TeacherNo`) REFERENCES `TeacherInfo` (`TeacherNo`) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT `TeaCourseNo` FOREIGN KEY (`CourseNo`) REFERENCES `CourseInfo` (`CourseNo`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `TeacherNo` (`TeacherNo`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4
;

CREATE TABLE IF NOT EXISTS `SpecialityCurriculum` (
`SpecialityNo`  int(5) NOT NULL ,
`CourseNo`  int(9) NOT NULL ,
CONSTRAINT `SpeCurSpecialityNo` FOREIGN KEY (`SpecialityNo`) REFERENCES `SpecialityInfo` (`SpecialityNo`) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT `SpeCurCourseNo` FOREIGN KEY (`CourseNo`) REFERENCES `CourseInfo` (`CourseNo`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `SpecialityNo` (`SpecialityNo`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4
;

CREATE TABLE IF NOT EXISTS `StudentCurriculum` (
`StudentNo`  int(7) NOT NULL ,
`CourseNo`  int(9) NOT NULL ,
CONSTRAINT `StuCurStudentNo` FOREIGN KEY (`StudentNo`) REFERENCES `StudentInfo` (`StudentNo`) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT `StuCurCourseNo` FOREIGN KEY (`CourseNo`) REFERENCES `CourseInfo` (`CourseNo`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `StudentNo` (`StudentNo`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4
;

CREATE TABLE IF NOT EXISTS `ExamInfo` (
`CourseNo`  int(9) NOT NULL ,
`ExamDay`  date NOT NULL ,
`ExamBeginTime`  time NOT NULL ,
`ExamEndTime`  time NOT NULL ,
`ClassroomNo`  int(4) NULL ,
`TeacherNo`  int(7) NULL ,
PRIMARY KEY (`CourseNo`),
CONSTRAINT `ExaCourseNo` FOREIGN KEY (`CourseNo`) REFERENCES `CourseInfo` (`CourseNo`) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT `ExaClassroomNo` FOREIGN KEY (`ClassroomNo`) REFERENCES `ClassroomInfo` (`ClassroomNo`) ON DELETE SET NULL ON UPDATE CASCADE,
CONSTRAINT `ExaTeacherNo` FOREIGN KEY (`TeacherNo`) REFERENCES `TeacherInfo` (`TeacherNo`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `CourseNo` (`CourseNo`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4
;

CREATE TABLE IF NOT EXISTS `ScoreInfo`(
`CourseNo`  int(9) NOT NULL ,
`StudentNo`  int(7) NOT NULL ,
`Score`  enum('A','B','C','D','E') CHARACTER SET utf8mb4 NOT NULL ,
PRIMARY KEY (`CourseNo`,`StudentNo`),
CONSTRAINT `ScoCourseNo` FOREIGN KEY (`CourseNo`) REFERENCES `CourseInfo` (`CourseNo`) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT `ScoStudentNo` FOREIGN KEY (`StudentNo`) REFERENCES `StudentInfo` (`StudentNo`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `StudentNo` (`StudentNo`) USING BTREE ,
INDEX `CourseNo` (`CourseNo`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4
;

CREATE TABLE IF NOT EXISTS `EvaluationInfo` (
`CourseNo`  int(9) NOT NULL ,
`TeacherNo`  int(7) NOT NULL ,
`TeaContent`  varchar(300) NULL ,
`StuContent`  varchar(300) NULL ,
`StudentNo`  int(7) NULL ,
CONSTRAINT `EvaCourseNo` FOREIGN KEY (`CourseNo`) REFERENCES `CourseInfo` (`CourseNo`) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT `EvaTeacherNo` FOREIGN KEY (`TeacherNo`) REFERENCES `TeacherInfo` (`TeacherNo`) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT `EvaStudentNo` FOREIGN KEY (`StudentNo`) REFERENCES `StudentInfo` (`StudentNo`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `TeacherNo` (`TeacherNo`) USING BTREE ,
INDEX `CourseNo` (`CourseNo`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8mb4
;


