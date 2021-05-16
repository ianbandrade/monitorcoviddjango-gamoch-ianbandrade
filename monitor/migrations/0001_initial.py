import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
  initial = True

  dependencies = [
  ]

  operations = [
    migrations.CreateModel(
      name='Country',
      fields=[
        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('name', models.CharField(max_length=255)),
      ],
      options={
        'verbose_name_plural': 'countries',
      },
    ),
    migrations.CreateModel(
      name='Covid',
      fields=[
        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('cases', models.IntegerField()),
        ('deaths', models.IntegerField()),
        ('recovered', models.IntegerField()),
        ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='monitor.country')),
      ],
      options={
        'verbose_name_plural': 'covid',
      },
    ),
  ]
