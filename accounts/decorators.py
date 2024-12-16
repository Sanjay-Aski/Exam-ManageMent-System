from django.http import Http404
from .constants import Group


def check_user_able_to_see_page(*groups: Group):
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(
                name__in=[group.name for group in groups]
            ).exists():
                print("Exist")
                return function(request, *args, **kwargs)
            print("Does Not Exist")
            raise Http404

        return wrapper

    return decorator
