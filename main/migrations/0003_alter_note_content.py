# Generated by Django 4.1.3 on 2022-11-21 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_note_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(max_length=280),
        ),
    ]
