# Generated by Django 2.0.2 on 2023-05-26 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestioncliente', '0002_auto_20230508_2116'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestioncliente.Cliente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]