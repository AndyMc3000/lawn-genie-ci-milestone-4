# Generated by Django 3.2.7 on 2021-09-19 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmailTitle', models.CharField(max_length=200, null=True)),
                ('EmailBody', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsletterSubscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]