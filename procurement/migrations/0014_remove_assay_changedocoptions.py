# Generated by Django 2.0.8 on 2018-11-20 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0013_assay_changedocoptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assay',
            name='changeDocOptions',
        ),
    ]
