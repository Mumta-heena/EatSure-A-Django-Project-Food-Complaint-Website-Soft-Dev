# Generated by Django 5.1.2 on 2024-10-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_eat', '0009_rename_status_complaint_complaintstatus_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='restaurantName',
            new_name='restaurant_Name',
        ),
        migrations.RenameField(
            model_name='complaint',
            old_name='userName',
            new_name='user_Name',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='complaintStatus',
        ),
        migrations.AddField(
            model_name='complaint',
            name='complaint_Description',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
