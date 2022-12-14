# Generated by Django 4.1.2 on 2022-11-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('nat_id', models.CharField(max_length=8, unique=True)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('user_type', models.CharField(choices=[('LD', 'Landlord'), ('TN', 'Tenant')], max_length=8)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
