from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=20)
    month_to_learn = models.IntegerField()

    def save(self,*args, **kwargs):
        if self.name:
            self.name = self.name.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class AbstractPerson(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.phone_number[0] == '0':
            self.phone_number = '+996' + self.phone_number[1:10]
        super().save(*args, **kwargs)
    

class Student(AbstractPerson):
    os = (('windows','Windows'),('mac','MacOS'),('linux','Linux'))
    work_study_place = models.CharField(max_length=30,null=True, blank=True)
    has_own_notebook = models.BooleanField(default=True)
    preferred_os = models.CharField(max_length=20, choices=os)

    def __str__(self):
        return self.preferred_os
    

class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=20,null=True, blank=True)
    experience = models.DateField()
    members = models.ManyToManyField(Student,related_name='members', through='Course')

    def __str__(self):
        return self.name
    


class Course(models.Model):
    name = models.CharField(max_length=20)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    


    def __str__(self):
        return self.name
    