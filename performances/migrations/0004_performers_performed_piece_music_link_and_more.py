# Generated by Django 5.1.2 on 2024-10-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0003_performed_piece_arranger_performed_piece_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='performed_piece',
            name='music_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='performed_piece',
            name='performers',
            field=models.ManyToManyField(related_name='musical_pieces', to='performances.performers'),
        ),
    ]
