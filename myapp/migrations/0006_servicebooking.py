# Generated by Django 3.1.2 on 2020-11-19 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_Name', models.CharField(max_length=150)),
                ('Your_Name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100)),
                ('Mobile_Number', models.CharField(max_length=50)),
                ('message', models.CharField(default='', max_length=400)),
            ],
        ),
    ]
