from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=260)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = '種類分類'

    def __str__(self):
        return self.name 


class Items(models.Model):
    name = models.CharField(max_length=260)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    # 告訴 Django 要將圖片放在哪一個資料夾
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural = '項目'



#ForeignKey(Category, related_name='items', on_delete=models.CASCADE):
#這表示Items模型中的category字段是一個外鍵，指向Category模型。這表示每個Items實例都會關聯到一個Category實例。

#related_name='items':
# 這個屬性設置了從Category實例反向查找關聯Items的名稱。也就是說，如果你有一個Category實例，你可以使用category.items.all()來獲取所有屬於該分類的Items。

# on_delete=models.CASCADE:
# 這表示當關聯的Category實例被刪除時，所有關聯的Items實例也會被自動刪除。

# 如以下的範例

# Category:

# 名稱：電子產品 (id=1)
# 名稱：家具 (id=2)
# Items:

# 名稱：筆記本電腦，分類：電子產品
# 名稱：手機，分類：電子產品
# 名稱：沙發，分類：家具
# python
# 複製程式碼
# # 首先，創建Category實例
# category_electronics = Category.objects.create(name='電子產品')
# category_furniture = Category.objects.create(name='家具')

# # 創建Items實例並關聯到對應的Category
# item_laptop = Items.objects.create(name='筆記本電腦', category=category_electronics, price=1000.0, created_by=user)
# item_phone = Items.objects.create(name='手機', category=category_electronics, price=800.0, created_by=user)
# item_sofa = Items.objects.create(name='沙發', category=category_furniture, price=500.0, created_by=user)

# # 使用category實例的related_name屬性來查詢所有關聯的Items
# electronics_items = category_electronics.items.all()
# furniture_items = category_furniture.items.all()
