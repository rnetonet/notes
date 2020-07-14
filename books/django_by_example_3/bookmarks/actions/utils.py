import datetime

from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from .models import Action


def create_action(user, verb, target=None):
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(
        user=user, verb=verb, created__gte=last_minute
    )

    if target:
        similar_actions = similar_actions.filter(
            target_ct=ContentType.objects.get_for_model(target), target_id=target.id
        )

    if similar_actions:
        return False
    else:
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
