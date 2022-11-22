# Generated by Django 2.1.7 on 2019-09-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0008_proposal_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='attachment',
            field=models.FileField(blank=True, help_text='File attached to the material', upload_to='materials/'),
        ),
    ]