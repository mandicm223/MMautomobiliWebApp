# Generated by Django 4.0.3 on 2022-04-05 11:43

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_alter_car_doors_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('6', '6'), ('4', '4'), ('3', '3'), ('5', '5')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Alarm', 'Alarm'), ('Airbags', 'Airbags'), ('Klima', 'Klima'), ('Grejanje sedista', 'Grejanje sedista'), ('Rikverc kamera', 'Rikverc kamera'), ('Pomoć prilikom parkiranja', 'Pomoć prilikom parkiranja'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Tempomat', 'Tempomat'), ('Direktno ubrizgavanje goriva', 'Direktno ubrizgavanje goriva'), ('Audio interfejs', 'Audio interfejs'), ('Bluetooth', 'Bluetooth'), ('Servo', 'Servo')], max_length=163),
        ),
    ]