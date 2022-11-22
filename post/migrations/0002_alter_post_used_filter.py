# Generated by Django 4.1.3 on 2022-11-22 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("filter", "0001_initial"),
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="used_filter",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_filter",
                to="filter.filterimage",
            ),
        ),
    ]
