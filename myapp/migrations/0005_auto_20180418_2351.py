# Generated by Django 2.0.1 on 2018-04-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_course_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(max_length=100, verbose_name='图标'),
        ),
        migrations.DeleteModel(
            name='Icon',
        ),
    ]
