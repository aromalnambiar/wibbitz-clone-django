# Generated by Django 4.1.1 on 2022-10-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_customers_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='image',
            field=models.FileField(upload_to='promoters/'),
        ),
    ]
