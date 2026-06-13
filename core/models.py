from django.db import models


class Student(models.Model):
    reg_no = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, default="Male")
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, default="Uganda")
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    program = models.CharField(max_length=100)
    year_of_entry = models.IntegerField(default=2026)
    current_year_of_study = models.IntegerField(default=1)
    semester = models.CharField(max_length=20, default="1")
    status = models.CharField(max_length=20, default="Active")
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)

    def __str__(self):
        return self.reg_no


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.code


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)

    marks = models.IntegerField()

    grade = models.CharField(max_length=5, blank=True)
    grade_point = models.FloatField(default=0.0)

    academic_year = models.CharField(max_length=20, default="2026/2027")
    semester = models.CharField(max_length=20, default="1")

    def calculate_grade(self):
        if self.marks >= 80:
            return "A", 5.0
        elif self.marks >= 75:
            return "B+", 4.5
        elif self.marks >= 70:
            return "B", 4.0
        elif self.marks >= 65:
            return "C+", 3.5
        elif self.marks >= 60:
            return "C", 3.0
        elif self.marks >= 55:
            return "D+", 2.5
        elif self.marks >= 50:
            return "D", 2.0
        else:
            return "F", 0.0

    def save(self, *args, **kwargs):
        self.grade, self.grade_point = self.calculate_grade()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.reg_no} - {self.course_code}"