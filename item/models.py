from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
      name=models.CharField(max_length=260)
      
      class Meta:
            ordering=('name',)
            verbose_name_plural='種類分類'
      
      def __str__(self):
            return self.name

class Items(models.Model):
      name=models.CharField(max_length=260)
      category=models.ForeignKey(Category,related_name='item',on_delete=models.CASCADE)
      description=models.TextField(blank=True,null=True)
      price=models.FloatField()
      image=models.ImageField(upload_to='item_images',blank=True,null=True)
      is_sold=models.BooleanField(default=False)
      crated_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
      created_at=models.DateTimeField(auto_now_add=True)