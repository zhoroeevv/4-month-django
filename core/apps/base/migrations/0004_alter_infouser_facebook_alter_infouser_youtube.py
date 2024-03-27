# Generated by Django 5.0.3 on 2024-03-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_infouser_email_infouser_facebook_infouser_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infouser',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='facebook ссылка'),
        ),
        migrations.AlterField(
            model_name='infouser',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='youtube ссылка'),
        ),
    ]
