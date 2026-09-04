from django.db import migrations
from django.contrib.auth.models import User

def create_superuser(apps, schema_editor):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_superuser),
    ]
