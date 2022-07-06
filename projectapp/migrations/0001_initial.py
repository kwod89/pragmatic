# Generated by Django 4.0.4 on 2022-06-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_created=True, null=True)),
                ('title', models.CharField(max_length=20, null=True, unique=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='project/')),
            ],
        ),
    ]
