# Generated by Django 2.0.8 on 2018-11-15 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0009_delete_changelog'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SA_No', models.IntegerField(blank=True, null=True)),
                ('DateTime', models.DateTimeField(blank=True, null=True)),
                ('User', models.CharField(blank=True, max_length=30, null=True)),
                ('Field', models.CharField(blank=True, max_length=30, null=True)),
                ('Before', models.CharField(blank=True, max_length=50, null=True)),
                ('After', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
