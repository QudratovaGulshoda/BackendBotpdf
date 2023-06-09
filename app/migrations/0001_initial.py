# Generated by Django 4.1.7 on 2023-03-31 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, help_text='Enter name', max_length=150, null=True, verbose_name='First name')),
                ('username', models.CharField(blank=True, help_text='Enter username', max_length=150, null=True, unique=True, verbose_name='Username')),
                ('telegram_id', models.CharField(help_text='Enter telegram ID', max_length=20, unique=True, verbose_name='Telegram ID')),
                ('status', models.BooleanField(default=False)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'BotUser',
                'verbose_name_plural': 'BotUsers',
                'db_table': 'BotUser',
                'managed': True,
            },
        ),
    ]
