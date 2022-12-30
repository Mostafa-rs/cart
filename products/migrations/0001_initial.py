# Generated by Django 4.1.4 on 2022-12-30 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('unit_price', models.PositiveIntegerField(default=0)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('none', 'None'), ('color', 'Color'), ('size', 'Size')], max_length=10)),
            ],
        ),
    ]
