# Generated by Django 4.0.2 on 2022-03-11 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_alter_allergies_allergy_alter_allergies_medhistory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergies',
            name='medhistory',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allergies', to='myapi.medhistory'),
        ),
        migrations.AlterField(
            model_name='device',
            name='uid',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device', to='myapi.user'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='measurements',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='measurement', to='myapi.measurements'),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='did',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.device'),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='medhistory',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='myapi.medhistory'),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='uid',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.user'),
        ),
        migrations.AlterField(
            model_name='medhistory',
            name='uid',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medHistory', to='myapi.user'),
        ),
        migrations.AlterField(
            model_name='medications',
            name='medhistory',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medications', to='myapi.medhistory'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='medhistory',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operations', to='myapi.medhistory'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='performedBy',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.user'),
        ),
    ]
