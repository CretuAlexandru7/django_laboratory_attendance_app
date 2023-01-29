# Generated by Django 4.1.5 on 2023-01-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('lecture_title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('short_description', models.CharField(max_length=500, null=True)),
                ('status', models.CharField(choices=[('Upcoming', 'Upcoming'), ('Done', 'Done')], max_length=200, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('students', models.ManyToManyField(to='accounts.student')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]
