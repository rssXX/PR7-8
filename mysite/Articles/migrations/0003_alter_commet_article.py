# Generated by Django 4.1.1 on 2022-09-29 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_commet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commet',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Articles.article'),
        ),
    ]
