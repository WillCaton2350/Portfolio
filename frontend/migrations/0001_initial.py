# Generated by Django 4.2.5 on 2023-09-05 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portfolioModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=225)),
                ('email_address', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('msg', models.TextField()),
            ],
            options={
                'db_table': 'portfolio_Table',
            },
        ),
    ]
