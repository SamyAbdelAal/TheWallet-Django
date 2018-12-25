# Generated by Django 2.1 on 2018-12-25 12:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20181216_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Health', 'Health'), ('Personal', 'Personal'), ('Emergency', 'Emergency'), ('Entertainment', 'Entertainment'), ('Transportation', 'Transportation'), ('Others', 'Others')], max_length=20),
        ),
        migrations.AlterField(
            model_name='budget',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='savings',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10, null=True),
        ),
    ]
