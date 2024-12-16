from enum import Enum


class Group(Enum):
    InstituteAdmin = "InstituteAdmin"
    UniversityAdmin = "UniversityAdmin"
    SuperAdmin = "SuperAdmin"
    Chancellor = "Chancellor"
    ViceChancellor = "ViceChancellor"
    Principal = "Principal"
    AttendanceAdmin = "AttendanceAdmin"
    ExamAdmin = "ExamAdmin"
    HeadOfDepartment = "HeadOfDepartment"
    DeputyHeadOfDepartment = "DeputyHeadOfDepartment"
    Teacher = "Teacher"
    Student = "Student"
    Parent = "Parent"
    Assistant = "Assistant"
