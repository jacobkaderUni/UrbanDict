# Generated by Django 4.2.5 on 2023-09-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urbanwords', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='written_on',
            field=models.TextField(),
        ),
    ]
