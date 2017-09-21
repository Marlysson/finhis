from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    total_amount = models.DecimalField(max_digits=6,decimal_places=2,default=0)
    user = models.OneToOneField(User)
    categories = models.ManyToManyField('Category')
    limit_spending_monthly = models.DecimalField(max_digits=6,decimal_places=2)

    @property
    def username(self):
        return self.user.username

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def email(self):
        return self.user.email

    @property
    def password(self):
        return self.user.password

    @property
    def last_name(self):
        return self.user.last_name


class Tranfer(models.Model):
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    sender = models.ForeignKey(Profile,related_name="shipments")
    receiver = models.ForeignKey(Profile,related_name="receipts")


class Movement(models.Model):

    OPERATIONS = (
        ("IN","INCREASE"),
        ("OUT","DECREASE")
    )

    description = models.CharField(max_length=25)
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)
    category = models.ForeignKey('Category')
    date = models.DateTimeField()
    type_operation = models.CharField(max_length=3,choices=OPERATIONS)


class Frequence(models.Model):
    description = models.CharField(max_length=15)
    quant_days = models.PositiveIntegerField()


class Recurrence(models.Model):

    '''
        After first movement is asked to user if he want create a recurrence to this movement
    '''
    
    movement = models.ForeignKey(Movement,related_name="recurrence")
    start_in = models.DateTimeField()
    frequence = models.ForeignKey(Frequence)
    next_action = models.DateTimeField()

    def save(self,*args,**kwargs):
        self.next_action += timedelta(days=self.frequence.quant_days)
        self.save()


class Notification(models.Model):

    message = models.CharField(max_length=25)
    movement = models.ForeignKey(Movement,related_name="notifications")


class Category(models.Model):

    name = models.CharField(max_length=10)
    icon = models.CharField(max_length=20)


class RequestCategory(models.Model):

    '''
        When approved generating a notification and associate category to user requested.
    '''

    name = models.CharField(max_length=15)
    profile = models.ForeignKey(Profile)
    approved = models.BooleanField(default=False)
