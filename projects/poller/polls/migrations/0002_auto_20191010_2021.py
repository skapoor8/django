# Generated by Django 2.2.6 on 2019-10-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionproposal',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
