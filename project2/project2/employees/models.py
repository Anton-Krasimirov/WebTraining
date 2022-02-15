from django.db import models
from django.urls import reverse
from django.core import validators


class AuditEntity(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, )
    update_on = models.DateTimeField(auto_now=True,)

    class Meta: # прави клсът абстрактен , тези колони ще се добавят към таблицата на Department
        abstract = True


class Department(AuditEntity):
    name = models.CharField(max_length=20, )

    def get_absolute_url(self):# връща url на апликейшъна където това нещо се случва
        return reverse('department_details', kwargs={'id': self.id})

    def __str__(self):# метод на модела , можем да правим каквито си искаме , нямат нишо общо с базата ,в случая визуазилизира
        #имената на департаментите в администрацията
        return self.name



class Employee(models.Model):
    SOFTWARE_DEVELOPER = 1
    QA_ENGINIEER = 2
    DEVOPS_SPECIALIST = 3

    SOFT_UNI = 'SoftUni'
    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'
    COMPANIES = [SOFT_UNI, GOOGLE, FACEBOOK]

    first_name = models.CharField(max_length=30, )
    last_name = models.CharField(max_length=40, null=True, blank=True,
                                 default='NO NAME')  # null i blank вървят заедно в този случай plank
    # дава възможносд да слагаме празен стринг и да го маркира като null

    egn = models.CharField(max_length=10, unique=True, verbose_name='EGN', validators=(validators.MinLengthValidator(10),))

    job_title = models.IntegerField(choices=(
        (SOFTWARE_DEVELOPER, 'Software Developer'),
        (QA_ENGINIEER, 'QA Engineer'),
        (DEVOPS_SPECIALIST, 'DEVOPS Engineer'),
    ))

    companies = models.CharField(
        max_length=max(len(c) for c in COMPANIES),
        choices=((c, c) for c in COMPANIES),
    )

    department = models.ForeignKey(Department, on_delete=models.CASCADE,)  # миграция един към много

    image = models.ImageField(null=True, blank=True, upload_to='profiles')

    class Meta:
        ordering = ('companies', '-first_name',)# сортираме във администрацията


class User(models.Model):
    email = models.EmailField()

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True,)  # миграция един към един


class Project(models.Model):
    name = models.CharField(max_length=30, )
    dead_line = models.DateField(null=True, blank=True, )

    employees = models.ManyToManyField(to=Employee, )  # миграция много към много
