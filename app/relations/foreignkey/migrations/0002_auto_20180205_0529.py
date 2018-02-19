# Generated by Django 2.0.2 on 2018-02-05 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foreignkey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foreignkey.Manufacturer', verbose_name='모델명'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=50, verbose_name='제조사명'),
        ),
    ]