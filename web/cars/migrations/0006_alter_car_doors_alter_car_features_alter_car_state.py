# Generated by Django 4.0.3 on 2022-04-04 16:12

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_doors_alter_car_features_alter_car_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('4', '4'), ('5', '5'), ('6', '6'), ('3', '3')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Direct Fuel Injection', 'Direct Fuel Injection'), ('Seat Heating', 'Seat Heating'), ('Wind Deflector', 'Wind Deflector'), ('Reversing Camera', 'Reversing Camera'), ('ParkAssist', 'ParkAssist'), ('Bluetooth Handset', 'Bluetooth Handset'), ('Cruise Control', 'Cruise Control'), ('Air Conditioning', 'Air Conditioning'), ('Alarm System', 'Alarm System'), ('Power Steering', 'Power Steering'), ('Audio Interface', 'Audio Interface'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Airbags', 'Airbags')], max_length=195),
        ),
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('AZ', 'Arizona'), ('CA', 'California'), ('MO', 'Missouri'), ('MT', 'Montana'), ('PA', 'Pennsylvania'), ('DC', 'District Of Columbia'), ('AL', 'Alabama'), ('CT', 'Connecticut'), ('UT', 'Utah'), ('MA', 'Massachusetts'), ('NM', 'New Mexico'), ('SC', 'South Carolina'), ('HI', 'Hawaii'), ('MI', 'Michigan'), ('NJ', 'New Jersey'), ('LA', 'Louisiana'), ('SD', 'South Dakota'), ('GA', 'Georgia'), ('NE', 'Nebraska'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('NH', 'New Hampshire'), ('OH', 'Ohio'), ('FL', 'Florida'), ('MN', 'Minnesota'), ('OK', 'Oklahoma'), ('KY', 'Kentucky'), ('WA', 'Washington'), ('AK', 'Alaska'), ('WY', 'Wyoming'), ('TX', 'Texas'), ('ND', 'North Dakota'), ('NC', 'North Carolina'), ('OR', 'Oregon'), ('NY', 'New York'), ('ME', 'Maine'), ('IL', 'Illinois'), ('MD', 'Maryland'), ('WI', 'Wisconsin'), ('VT', 'Vermont'), ('DE', 'Delaware'), ('ID', 'Idaho'), ('VA', 'Virginia'), ('TN', 'Tennessee'), ('MS', 'Mississippi'), ('WV', 'West Virginia'), ('NV', 'Nevada'), ('IA', 'Iowa'), ('CO', 'Colorado'), ('RI', 'Rhode Island'), ('AR', 'Arkansas')], max_length=100),
        ),
    ]