from django.db import models

# import datetime
# from django.utils import timezone


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_data = models.DateTimeField("date published")
    
#     def __str__(self):
#         return self.question_text
    
#     def wes_published_recently(self):
#         return self.pub_data >= timezone.now() - datetime.timedelta(days=1)
    
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
    
#     def __str__(self):
#         return self.choice_text

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    hindi = models.IntegerField(default=0)
    english = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    perecent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name