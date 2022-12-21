import datetime
from user.models import Student, Mentor, Language, Course

# teacher = Teacher( user=User.objects.create( username='vin_diesel',password='family'),name='Vin Diesel', email='family_forever@mail.kg')
# # # teacher.save()

lang = Language(name= 'Python', month_to_learn =  6)
lang2 = Language(name='Java Script',month_to_learn= 6)
lang3 = Language(name ='UX-UI',month_to_learn  = 2)

stud = Student(name='Amanov Aman',email= 'aman@mail.ru',phone_number='+996700989898',work_study_place= 'School №13',has_own_notebook= True,preferred_os ='windows')
stud2 = Student(name='Apina Alena',email= 'aapina@bk.ru',phone_number='0550888888',work_study_place= 'TV',has_own_notebook= True, preferred_os ='mac')
# ment = Mentor('name': 'Ilona Maskova',
#         'email': 'imask@gmail.com',
#         'phone_number': '0500545454',
#         'main_work': None,
#         'experience': datetime.date(year=2021, month=10, day=23))

lang.save()
lang2.save()
lang3.save()
stud.save()
stud2.save()


students = [
    {
        'name': 'Amanov Aman',
        'email': 'aman@mail.ru',
        'phone_number': '+996700989898',
        'work_study_place': 'School №13',
        'has_own_notebook': True,
        'preferred_os': 'windows'
    },
    {
        'name': 'Apina Alena',
        'email': 'aapina@bk.ru',
        'phone_number': '0550888888',
        'work_study_place': 'TV',
        'has_own_notebook': True,
        'preferred_os': 'mac'
    },
]

mentors = [
    {
        'name': 'Ilona Maskova',
        'email': 'imask@gmail.com',
        'phone_number': '0500545454',
        'main_work': None,
        'experience': datetime.date(year=2021, month=10, day=23)
    },
    {
        'name': 'Halil Nurmuhametov',
        'email': 'halil@gmail.com',
        'phone_number': '0709989876',
        'main_work': 'University of Fort Collins',
        'experience': datetime.date(year=2010, month=9, day=18)
    }
]