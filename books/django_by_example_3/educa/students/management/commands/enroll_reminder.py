from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mass_mail
from django.core.management.base import BaseCommand
from django.db.models import Count


class Command(BaseCommand):
    help = "Remind students to enroll in more courses"

    def add_arguments(self, parser) -> None:
        parser.add_argument("--max-students", dest="max_students", type=int)

    def handle(self, *args, **options):
        users_to_remind = User.objects.annotate(
            total_courses=Count("courses_joined")
        ).filter(total_courses=0)

        emails = []
        subject = "Enroll!"
        message = "Enroll in some course!"

        for user in users_to_remind:
            emails.append((subject, message, settings.DEFAULT_FROM_EMAIL, [user.email]))

        send_mass_mail(emails)
        self.stdout.write(self.style.SUCCESS(f"Sent {len(emails)} reminders"))
