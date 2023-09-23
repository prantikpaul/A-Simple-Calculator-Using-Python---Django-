from django.db import models
# from phone_field import PhoneField
# # Create your models here.

# class profile (models.Model):
#     GENDER = (
#     ('Male','Male'),
#     ('Female','Female'),
#     ('Other','Other')
# )
#     RELIGION= (
#         ('Islam','Islam'),
#         ('Hindu','Hindu'),
#         ('Buddha','Buddha'),
#         ('Other','Other')
        
#     )



#     name= models.CharField(max_length=15)
    
#     image=models.ImageField(upload_to='prof_pic/')
    
#     email =models.TextField(max_length=20)
    
#     phone = PhoneField(blank=True, help_text='Contact phone number')
#     # phone = models.TextField(max_length=15)
    
#     gender=models.CharField(choices=GENDER,max_length=15)
    
#     adress =models.TextField(max_length=40)
    
#     adress_2 = models.TextField(max_length=40,null=True,blank=True,help_text='Optional')

#     religion=models.CharField(choices=RELIGION,max_length=10)

#     date_of_birth=models.DateField()
#     is_alive = models.BooleanField(default=True, null=True,blank=True)
#     def __str__(self):
#         return self.name
