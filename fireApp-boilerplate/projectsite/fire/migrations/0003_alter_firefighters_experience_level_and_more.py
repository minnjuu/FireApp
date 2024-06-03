# Generated by Django 5.0.3 on 2024-06-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fire', '0002_alter_firefighters_experience_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firefighters',
            name='experience_level',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='firefighters',
            name='rank',
            field=models.CharField(choices=[('Probationary Firefighter', 'Probationary Firefighter'), ('Firefighter I', 'Firefighter I'), ('Firefighter II', 'Firefighter II'), ('Firefighter III', 'Firefighter III'), ('Driver', 'Driver'), ('Captain', 'Captain'), ('Battalion Chief', 'Battalion Chief')], max_length=45),
        ),
    ]