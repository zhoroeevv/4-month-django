# Generated by Django 5.0.3 on 2024-03-20 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_infouser_facebook_alter_infouser_youtube'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secondary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Secondary/', verbose_name='Фотография пользователя')),
                ('title', models.CharField(max_length=255, verbose_name='коротко о себе')),
                ('descriptions', models.TextField(verbose_name='О себе')),
            ],
            options={
                'verbose_name': 'О пользователе',
                'verbose_name_plural': 'О пользователей',
            },
        ),
        migrations.AddField(
            model_name='infouser',
            name='age',
            field=models.IntegerField(default=1, verbose_name='Возрасть'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='infouser',
            name='froms',
            field=models.CharField(default=1, max_length=255, verbose_name='Место рождение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infouser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='infouser',
            name='image',
            field=models.ImageField(upload_to='Info_user/', verbose_name='Фотография пользователя'),
        ),
        migrations.AlterField(
            model_name='infouser',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='Youtube ссылка'),
        ),
    ]
