# Generated by Django 3.1.6 on 2021-02-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('position_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('requirement', models.TextField()),
            ],
        ),
    ]
