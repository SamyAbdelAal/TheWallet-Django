# Generated by Django 2.1 on 2018-12-11 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20181210_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=120)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='api.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('label', models.CharField(max_length=120)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='budget',
        ),
        migrations.AlterField(
            model_name='budget',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Health', 'Health'), ('Emergency', 'Emergency'), ('Entertainment', 'Entertainment'), ('Others', 'Others')], max_length=13),
        ),
        migrations.DeleteModel(
            name='Expenses',
        ),
        migrations.AddField(
            model_name='transaction',
            name='budget',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='api.Budget'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL),
        ),
    ]
