# Generated by Django 2.1.7 on 2019-08-31 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0007_proposal'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='active',
            field=models.BooleanField(default=True, help_text='Proposal actively displayed'),
            preserve_default=False,
        ),
    ]
