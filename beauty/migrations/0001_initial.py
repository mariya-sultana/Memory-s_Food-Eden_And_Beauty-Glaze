# Generated by Django 3.1.7 on 2021-06-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beauty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('PhoneNum', models.PositiveIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Payment', models.CharField(choices=[('Bkash(01869537592)', 'Bkash(01869537592)'), ('Rocket(01869537592)', 'Rocket(01869537592)'), ('Cash On Delivery', 'Cash On Delivery')], max_length=50)),
                ('Textarea', models.TextField()),
            ],
        ),
    ]
