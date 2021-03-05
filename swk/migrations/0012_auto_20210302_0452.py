# Generated by Django 3.1.6 on 2021-03-02 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swk', '0011_swkattendants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracksheet',
            name='date',
            field=models.DateField(help_text='Enter Date'),
        ),
        migrations.AlterField(
            model_name='tracksheet',
            name='num_houses_reached',
            field=models.IntegerField(default=20, help_text='Enter Houses Reached'),
        ),
    ]