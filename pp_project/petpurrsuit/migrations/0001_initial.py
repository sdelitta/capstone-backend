# Generated by Django 4.0.4 on 2022-05-15 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelterName', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shelters', to='petpurrsuit.state')),
            ],
        ),
        migrations.CreateModel(
            name='Feline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=2)),
                ('photo_url', models.CharField(default='no dice!', max_length=400)),
                ('shelter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='felines', to='petpurrsuit.shelter')),
            ],
        ),
        migrations.CreateModel(
            name='Canine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dogName', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=2)),
                ('photo_url', models.CharField(default='no dice!', max_length=400)),
                ('shelter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='canines', to='petpurrsuit.shelter')),
            ],
        ),
    ]