from django.db import models

# Create your models here.
class Student(models.Model):
    SEX_ITEMS =[
        (1, 'male'),
        (2,'female'),
        (0,'no idea'),
    ]
    STATUS_ITEMS=[
        (0,'apply'),
        (1,'pass'),
        (2,'refuse'),
    ]
    name=models.CharField(max_length=100,verbose_name='name')
    sex=models.IntegerField(choices=SEX_ITEMS,default=0,verbose_name='sex')
    profession=models.CharField(max_length=100,verbose_name='profession')
    email=models.EmailField(max_length=100,verbose_name='email')
    qq=models.CharField(max_length=100,verbose_name='qq')
    phone=models.CharField(max_length=100,verbose_name='phone')
    
    status=models.IntegerField(choices=STATUS_ITEMS,default=0,verbose_name='审核状态')
    create_time=models.DateTimeField(auto_now_add=True,editable=False,verbose_name='创建时间')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name=verbose_name_plural='学生'