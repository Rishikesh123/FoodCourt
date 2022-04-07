# Generated by Django 3.0a1 on 2020-01-12 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_food_frestaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodpair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.food')),
            ],
        ),
    ]
