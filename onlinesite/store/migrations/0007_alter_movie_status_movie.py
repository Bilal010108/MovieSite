# Generated by Django 5.1.3 on 2024-11-20 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_profile_phone_number9_profile_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='status_movie',
            field=models.CharField(choices=[('pro', 'Pro'), ('simple', 'simple')], default='class', max_length=18),
        ),
    ]
