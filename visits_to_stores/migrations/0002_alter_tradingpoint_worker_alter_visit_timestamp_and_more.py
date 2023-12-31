# Generated by Django 4.2.7 on 2023-11-02 12:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('visits_to_stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradingpoint',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trading_points', to='visits_to_stores.worker'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='visit',
            name='trading_point',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visits', to='visits_to_stores.tradingpoint'),
        ),
    ]
