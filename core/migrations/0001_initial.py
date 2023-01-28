# Generated by Django 4.0.5 on 2023-01-27 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockSentiment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=100)),
                ('stock_symbol', models.CharField(max_length=50)),
                ('sentiment', models.FloatField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('session_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StockOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0)),
                ('stock_symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.stocksentiment')),
            ],
        ),
    ]