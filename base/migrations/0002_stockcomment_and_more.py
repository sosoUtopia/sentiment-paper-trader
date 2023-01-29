# Generated by Django 4.0.5 on 2023-01-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=500)),
                ('symbol', models.CharField(max_length=50)),
                ('sentiment', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='stocksentiment',
            old_name='stock_symbol',
            new_name='symbol',
        ),
    ]