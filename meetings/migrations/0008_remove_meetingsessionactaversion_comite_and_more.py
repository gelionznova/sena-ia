# Generated by Django 4.2.5 on 2025-07-02 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0007_meetingsessionactaversion_agenda_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingsessionactaversion',
            name='comite',
        ),
        migrations.RemoveField(
            model_name='meetingsessionactaversion',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='meetingsessionactaversion',
            name='hora_fin',
        ),
        migrations.RemoveField(
            model_name='meetingsessionactaversion',
            name='hora_inicio',
        ),
    ]
