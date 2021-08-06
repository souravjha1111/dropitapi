# Generated by Django 3.2.3 on 2021-08-06 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_gender',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.CreateModel(
            name='DropperProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dropper_age', models.IntegerField()),
                ('dropper_gender', models.CharField(max_length=8, null=True)),
                ('dropper_profile_photo', models.ImageField(blank=True, upload_to='profile_pics')),
                ('dropper_authentication_number', models.IntegerField()),
                ('dropper_authentication_photo', models.ImageField(upload_to='dropper_security')),
                ('dropper_vehicle_type', models.CharField(max_length=10)),
                ('dropper_rc_photo', models.ImageField(upload_to='dropper_security')),
                ('dropper_driving_liscence_photo', models.ImageField(upload_to='dropper_security')),
                ('dropper', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dropper', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]