# Generated by Django 5.1.4 on 2024-12-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_message_options_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectedYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
