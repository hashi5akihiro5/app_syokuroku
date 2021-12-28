from django.db import models
import datetime
from django.utils import timezone




# プロフィール
class Profile(models.Model):
    name = models.CharField('名前', max_length=100)
    age = models.IntegerField('年齢', blank=False, null=True, default=30)
    day_kcal = models.IntegerField('１日の摂取カロリー',
                                    blank=False,
                                    null=True,
                                    default=0,
                                    )
    target = models.TextField('目標', max_length=300)
    created = models.DateField('作成日', default=datetime.date.today)
    twitter = models.CharField('twitter', max_length=100, null=True, blank=True)
    facebook = models.CharField('facebook', max_length=100, null=True, blank=True)
    instagram = models.CharField('instagram', max_length=100, null=True, blank=True)
    #topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
    #subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')

    def __str__(self):
        return self.name

# 親カテゴリー
# カテゴリー種類:主食・副食・飲み物
class ParentCategory(models.Model):
    name = models.CharField(verbose_name='主食・副食・飲み物', max_length=100)

    def __str__(self):
        return self.name

# 子カテゴリー
# 主食
class MainCategory(models.Model):
    name = models.CharField(verbose_name='主食', max_length=100)
    parent = models.ForeignKey(ParentCategory, verbose_name='主食・副食・飲み物', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

# 副食
class SubCategory(models.Model):
    name = models.CharField(verbose_name='副食', max_length=100)
    parent = models.ForeignKey(ParentCategory, verbose_name='主食・副食・飲み物', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

# 飲み物
class DrinkCategory(models.Model):
    name = models.CharField(verbose_name='飲み物', max_length=100)
    parent = models.ForeignKey(ParentCategory, verbose_name='主食・副食・飲み物', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Post(models.Model):
    date = models.DateField('作成日', default=datetime.date.today)
    time = models.TimeField('作成時間', default=timezone.datetime.now())
    main_category = models.ForeignKey(MainCategory, verbose_name='主食', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, verbose_name='副食', on_delete=models.CASCADE)
    drink_category = models.ForeignKey(DrinkCategory, verbose_name='飲み物', on_delete=models.CASCADE)

    def __str__(self):
        return self.meals
