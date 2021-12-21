from django.db import models
from django.utils.timezone import now


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
    created = models.DateTimeField('作成日')
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
    name = models.CharField(verbose_name='親カテゴリー', max_length=100)

    def __str__(self):
        return self.name

# 子カテゴリー
# 主食
class MainCategory(models.Model):
    name = models.CharField('主食', max_length=100)

    def __str__(self):
        return self.name

# 副食
class SubCategory(models.Model):
    name = models.CharField('副食', max_length=100)

    def __str__(self):
        return self.name

# 飲み物
class DrinkCategory(models.Model):
    name = models.CharField('飲み物', max_length=100)

    def __str__(self):
        return self.name


# class Post(models.Model):
#     meal_no = models.CharField('食事_No.', max_length=255)
#     category = models.ForeignKey(MainCategory, verbose_name='メニュー名', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.meal_no
