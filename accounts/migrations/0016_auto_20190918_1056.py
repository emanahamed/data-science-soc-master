# Generated by Django 2.1.7 on 2019-09-18 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20190829_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(help_text='Name of the course', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='course',
            field=models.ForeignKey(blank=True, help_text='Type down and/or select your course from the list', on_delete=django.db.models.deletion.CASCADE, to='accounts.Course'),
        ),
    ]