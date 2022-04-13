# Generated by Django 4.0.3 on 2022-04-05 12:12

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_alter_car_doors_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('5', '5'), ('2', '2'), ('3', '3'), ('6', '6'), ('4', '4')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Klima', 'Klima'), ('Tempomat', 'Tempomat'), ('Servo', 'Servo'), ('Alarm', 'Alarm'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Airbags', 'Airbags'), ('Audio interfejs', 'Audio interfejs'), ('Direktno ubrizgavanje goriva', 'Direktno ubrizgavanje goriva'), ('Bluetooth', 'Bluetooth'), ('Grejanje sedista', 'Grejanje sedista'), ('Rikverc kamera', 'Rikverc kamera'), ('Pomoć prilikom parkiranja', 'Pomoć prilikom parkiranja')], max_length=163),
        ),
    ]