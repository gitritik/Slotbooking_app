# Generated by Django 4.1 on 2022-12-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bookname',
            field=models.CharField(default='Naam', max_length=30),
        ),
        migrations.AddField(
            model_name='booking',
            name='booknumber',
            field=models.CharField(default='Number', max_length=12),
        ),
    ]
