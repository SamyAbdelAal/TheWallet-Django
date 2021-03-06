# Generated by Django 2.1 on 2018-12-12 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181211_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='budgets', to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
