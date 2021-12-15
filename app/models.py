from django.db import models
from django.utils.timezone import now


class Profile(models.Model):
    name = models.CharField('名前', max_length=100)
    day_kcal = models.IntegerField('１日の摂取カロリー',
                                    blank=False,
                                    null=True,
                                    default=0,
                                    )
    #age = models.IntegerField(required=False,label='年齢',max_value=200,min_value=0)
    target = models.TextField('目標', max_length=300)
    created = models.DateTimeField('作成日')
    twitter = models.CharField('twitter', max_length=100, null=True, blank=True)
    facebook = models.CharField('facebook', max_length=100, null=True, blank=True)
    instagram = models.CharField('instagram', max_length=100, null=True, blank=True)
    #topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
    #subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')

    def __str__(self):
        return self.name

# 親カテゴリー
class ParentCategory(models.Model):
    name = models.CharField('主食・副食・飲み物', max_length=255)

    def __str__(self):
        return self.name

# 子カテゴリー
class Category(models.Model):
    name = models.CharField('メニュー名', max_length=255)
    parent = models.ForeignKey(ParentCategory, verbose_name='主食・副食・飲み物', on_delete=models.CASCADE)

    def __str_(self):
        return self.name

class Post(models.Model):
    meal_no = models.CharField('食事_No.', max_length=255)
    category = models.ForeignKey(Category, verbose_name='メニュー名', on_delete=models.CASCADE)

    def __str__(self):
        return self.meal_no

# class menu(models.Model):
#     menu = models.CharField('メニュー', max_length=100, null=True, blank=True)
#     volume = models.IntegerField(required=False,label='量',max_value=200,min_value=0)
#     kcal = models.IntegerField(required=False,label='カロリー',max_value=200,min_value=0)

#     models.ChoiceFiled()