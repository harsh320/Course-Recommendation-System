# Generated by Django 2.2.7 on 2019-12-01 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=256)),
                ('course_name', models.CharField(max_length=256)),
                ('branch_name1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject123', to='course.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('url', models.URLField()),
                ('site', models.CharField(max_length=256)),
                ('percent_similar', models.CharField(max_length=256)),
                ('keywords1', models.CharField(default='', max_length=1000)),
                ('branch_name1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content57', to='course.Branch')),
                ('subject1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content56', to='course.Subjects')),
            ],
        ),
    ]
