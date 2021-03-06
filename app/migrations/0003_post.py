# Generated by Django 2.2.24 on 2021-12-24 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211222_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('drink_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.DrinkCategory', verbose_name='飲み物')),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.MainCategory', verbose_name='主食')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SubCategory', verbose_name='副食')),
            ],
        ),
    ]
