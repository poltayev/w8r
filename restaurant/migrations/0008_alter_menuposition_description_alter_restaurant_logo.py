# Generated by Django 4.1.7 on 2023-06-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_alter_menucategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuposition',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(default=None, upload_to='images/logos/'),
        ),
    ]
