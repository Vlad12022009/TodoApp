# Generated by Django 3.2.8 on 2024-09-01 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createtask',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
