# Generated by Django 4.1.2 on 2022-10-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0002_alter_form_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
