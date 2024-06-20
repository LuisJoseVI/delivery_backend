from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    if not User.objects.filter(email='admin@email.com').exists():
        User.objects.create_superuser(
            email='admin@email.com',
            password='123456',
            username='admin',
            first_name='admin',
            last_name='admin',
            id_document=123456,
            role='admin',
        )
