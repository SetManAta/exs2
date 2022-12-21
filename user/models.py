from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=20)
    month_to_learn = models.IntegerField()

    def save(self,*args, **kwargs):
        if self.name:
            self.name = self.name.title()

    def __str__(self):
        return self.name



class AbstractPerson(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        q = +99
        if self.phone_number[0] == 0:
            self.phone_number[0] = 6
        self.phone_number = ''.join(q,self.phone_number)
    def __str__(self):
        return self.name
    

class Student(AbstractPerson):
    choices = (('windows'),('mac'),('linux'))
    work_study_place = models.CharField(max_length=30,null=True, blank=True)
    has_own_notebook = models.BooleanField(default=True)
    preferred_os = models.CharField(max_length=20, choices=[])

    def __str__(self):
        return self.name
    

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
    
