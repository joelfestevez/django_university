# Generated by Django 3.2.5 on 2021-07-29 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrer',
            fields=[
                ('carrer_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('duration', models.PositiveSmallIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('credits', models.PositiveSmallIntegerField()),
                ('teacher', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('lastname1', models.CharField(max_length=35)),
                ('lastname2', models.CharField(max_length=35)),
                ('name', models.CharField(max_length=35)),
                ('birthday', models.DateField()),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1)),
                ('vigency', models.BooleanField(default=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.carrer')),
            ],
        ),
        migrations.CreateModel(
            name='identificationNumber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dateIN', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.student')),
            ],
        ),
    ]