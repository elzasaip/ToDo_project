# Generated by Django 4.0.6 on 2022-08-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal_for_month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=120)),
                ('month', models.FloatField()),
                ('difficulty', models.BooleanField(default=False)),
                ('reason_for_goal', models.TextField()),
            ],
        ),
    ]
