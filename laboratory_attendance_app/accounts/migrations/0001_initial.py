# Generated by Django 4.1.5 on 2023-01-27 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('fp_index', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('grd_average', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('is_teacher', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]