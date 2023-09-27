# Generated by Django 3.0 on 2023-09-27 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aplicatie1', '0004_location_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=50)),
                ('company_type', models.CharField(choices=[('SRL', 'S.R.L.'), ('SA', 'S.A.')], max_length=5)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicatie1.Location')),
            ],
        ),
    ]
