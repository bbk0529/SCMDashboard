# Generated by Django 2.0.8 on 2018-09-19 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loteam', '0024_ycp4_mrp'),
    ]

    operations = [
        migrations.AddField(
            model_name='ycp4',
            name='MaterialType',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
