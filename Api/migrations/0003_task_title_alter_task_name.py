# Generated by Django 5.0.4 on 2024-04-26 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_rename_drink_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]