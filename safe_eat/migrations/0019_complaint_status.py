# Generated by Django 5.0.2 on 2024-11-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_eat', '0018_complaint_image1_complaint_image2_complaint_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('resolved', 'Resolved'), ('in_process', 'In Process'), ('fake', 'Fake')], default='in_process', max_length=20),
        ),
    ]
