# Generated by Django 2.0.8 on 2018-11-20 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0012_auto_20181119_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='assay',
            name='changeDocOptions',
            field=models.CharField(default='신규등록', max_length=30),
        ),
    ]
