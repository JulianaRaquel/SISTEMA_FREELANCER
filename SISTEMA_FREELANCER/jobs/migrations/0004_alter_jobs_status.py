# Generated by Django 4.1.1 on 2022-10-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_jobs_arquivo_final'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('C', 'Em criação'), ('AA', 'Aguardando aprovação'), ('F', 'Finalizado')], default='C', max_length=3),
        ),
    ]
