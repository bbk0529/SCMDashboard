# Generated by Django 2.0.8 on 2018-09-04 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loteam', '0011_auto_20180904_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='id',
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(default=1, max_length=30, primary_key=True, serialize=False),
        ),
    ]
