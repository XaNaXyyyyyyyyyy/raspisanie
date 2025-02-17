from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Weekday(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Event(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)
    number = models.IntegerField()
    day_of_week = models.CharField(
        max_length=15,
        choices=[
            ("ПОНЕДЕЛЬНИК", "Понедельник"),
            ("ВТОРНИК", "Вторник"),
            ("СРЕДА", "Среда"),
            ("ЧЕТВЕРГ", "Четверг"),
            ("ПЯТНИЦА", "Пятница"),
            # ... other days of the week
        ]
    )
    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    weekday = models.ForeignKey(Weekday, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    nomer = models.IntegerField()

    
    
    def __str__(self):
        return str(self.weekday)
