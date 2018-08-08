# Generated by Django 2.0.5 on 2018-08-08 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Excercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('rounds_count', models.PositiveIntegerField(default=0)),
                ('max_rep', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('continuity', models.PositiveIntegerField(default=0)),
                ('source', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rounds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_rep', models.PositiveIntegerField(default=0)),
                ('excercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Excercises')),
            ],
        ),
        migrations.AddField(
            model_name='excercises',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Program'),
        ),
    ]