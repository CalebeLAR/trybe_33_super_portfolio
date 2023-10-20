# Generated by Django 4.2.3 on 2023-10-20 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0004_certifyinginstitution_certificate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="certifying_institution",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="certificates",
                to="projects.certifyinginstitution",
            ),
        ),
    ]
