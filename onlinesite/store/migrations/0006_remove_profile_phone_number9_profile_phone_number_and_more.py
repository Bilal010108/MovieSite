from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_phone_number_profile_phone_number9'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_number9',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
