# Generated by Django 4.1.7 on 2023-10-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryApp', '0003_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, unique=True),
        ),
    ]