from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Create default and moderator user groups"

    def handle(self, *args, **kwargs):
        default_group, created = Group.objects.get_or_create(name="default")
        moderator_group, created = Group.objects.get_or_create(name="moderators")

        # Moderators can delete any news/comment
        delete_news = Permission.objects.get(codename="delete_news")
        delete_comment = Permission.objects.get(codename="delete_comment")

        moderator_group.permissions.add(delete_news, delete_comment)

        self.stdout.write(self.style.SUCCESS("User groups created successfully!"))
