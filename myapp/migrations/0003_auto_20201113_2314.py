# Generated by Django 3.1.2 on 2020-11-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='Pricing_max',
            new_name='Pricing',
        ),
        migrations.RemoveField(
            model_name='service',
            name='Pricing_min',
        ),
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.CharField(default='', max_length=1000),
        ),
    ]