import email
from django.db import models

# Create your models here.
class slTime(models.Model):
    start_time=models.CharField(max_length=20)
    end_time=models.CharField(max_length=20)
    def __str__(self) :
        return self.start_time + ' to ' + self.end_time

class Day(models.Model):
    dayname=models.CharField(max_length=15)
    def __str__(self) :
        return self.dayname

class Sport(models.Model):
    sportname=models.CharField(max_length=20)
    def __str__(self) :
        return self.sportname

class myUser(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    def __str__(self) :
        return self.username


class Booking(models.Model):
    bookname=models.CharField(max_length=30,default='')
    booknumber=models.CharField(max_length=12,default='')
    bookuser=models.ForeignKey(myUser,on_delete=models.CASCADE)
    booksport=models.ForeignKey(Sport,on_delete=models.CASCADE)
    bookday=models.ForeignKey(Day,on_delete=models.CASCADE)
    bookslot=models.ForeignKey(slTime,on_delete=models.CASCADE)
    
    def isBooked(self,sport,day,slot):

        if Booking.objects.filter(booksport=sport,bookday=day,bookslot=slot).exists():
            return True
        else:
            return False
    # def printdata(self):

    #     books=Booking.objects.all()
    #     dict={'ex':books}
    #     print(dict['ex'])

# Booking.printdata()




