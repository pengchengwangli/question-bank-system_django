# Generated by Django 5.0.6 on 2024-07-13 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_bank', '0004_alter_question_stem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='stem',
            field=models.TextField(verbose_name='题干'),
        ),
    ]
