# Generated by Django 4.1.2 on 2022-10-20 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0004_alter_form_account_alter_form_branches_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
