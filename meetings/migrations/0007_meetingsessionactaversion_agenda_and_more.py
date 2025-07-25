# Generated by Django 4.2.5 on 2025-07-02 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0006_meetingsessionactaversion'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingsessionactaversion',
            name='agenda',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name='meetingsessionactaversion',
            name='centro',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='meetingsessionactaversion',
            name='ciudad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='meetingsessionactaversion',
            name='comite',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='meetingsessionactaversion',
            name='conclusiones',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meetingsessionactaversion',
            name='desarrollo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meetingsessionactaversion',
            name='enlace',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meetingsessionactaversion',
            name='fecha',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='meetingsessionactaversion',
            name='hora_fin',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='meetingsessionactaversion',
            name='hora_inicio',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='meetingsessionactaversion',
            name='lugar',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='meetingsessionactaversion',
            name='numero',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='meetingsessionactaversion',
            name='objetivos',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='meetingsessionactaversion',
            name='content_html',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ActaCompromiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad', models.CharField(max_length=400)),
                ('fecha', models.CharField(blank=True, max_length=40, null=True)),
                ('responsable', models.CharField(blank=True, max_length=100, null=True)),
                ('firma', models.CharField(blank=True, max_length=100, null=True)),
                ('acta_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compromisos', to='meetings.meetingsessionactaversion')),
            ],
        ),
        migrations.CreateModel(
            name='ActaAsistente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('dependencia', models.CharField(blank=True, max_length=150, null=True)),
                ('aprueba', models.CharField(blank=True, max_length=10, null=True)),
                ('observacion', models.CharField(blank=True, max_length=400, null=True)),
                ('firma', models.CharField(blank=True, max_length=100, null=True)),
                ('acta_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistentes', to='meetings.meetingsessionactaversion')),
            ],
        ),
    ]
