# Generated by Django 4.1 on 2022-08-29 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayname', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='slTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=20)),
                ('end_time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sportname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.day')),
                ('bookslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.sltime')),
                ('booksport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.sport')),
                ('bookuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.myuser')),
            ],
        ),
    ]
