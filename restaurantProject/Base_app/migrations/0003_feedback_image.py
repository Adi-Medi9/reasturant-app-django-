# Generated by Django 5.1.4 on 2025-01-05 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_app', '0002_alter_booktable_name_alter_feedback_user_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='Image',
            field=models.ImageField(blank=True, upload_to='Items/'),
        ),
    ]