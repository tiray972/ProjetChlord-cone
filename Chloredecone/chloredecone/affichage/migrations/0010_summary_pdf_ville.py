# Generated by Django 4.0.3 on 2022-06-01 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affichage', '0009_alter_summary_pdf_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary_pdf',
            name='ville',
            field=models.CharField(default='', max_length=200),
        ),
    ]
