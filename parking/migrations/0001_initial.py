# Generated by Django 3.1.5 on 2021-02-25 00:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_code', models.CharField(max_length=3)),
                ('block_photo', models.ImageField(default='media/defaultblock.jpeg', upload_to='blocks/')),
                ('is_block_full', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('is_accessible', models.CharField(max_length=1)),
                ('number_of_slots', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('location_pic', models.ImageField(default='media/auca.jpeg', upload_to='building/')),
                ('latitude', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('longitude', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_number', models.PositiveIntegerField()),
                ('is_slot_available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('slot_photo', models.ImageField(default='media/defaultslot.jpeg', upload_to='slots/')),
                ('block_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.block')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='No email', max_length=254)),
                ('phone_No', models.CharField(max_length=10)),
                ('plate_No', models.CharField(max_length=10)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('Entry_time', models.TimeField()),
                ('Exit_time', models.TimeField()),
                ('duration_in_minutes', models.PositiveIntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.location')),
                ('parking_slot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.parkingslot')),
                ('plate_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.profile')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSlip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.TimeField()),
                ('exit_time', models.TimeField()),
                ('slot_reservation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.reservation')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.location'),
        ),
    ]
