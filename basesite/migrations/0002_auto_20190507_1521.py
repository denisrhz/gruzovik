# Generated by Django 2.2.1 on 2019-05-07 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basesite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='type_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='basesite.TypeWork'),
        ),
    ]
