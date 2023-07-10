from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='obrisan',
            field=models.BooleanField(default=False),
        ),
    ]
