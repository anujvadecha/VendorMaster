from functools import wraps

from django.core.exceptions import PermissionDenied
from django.utils.decorators import available_attrs


def user_passes_test_forbidden(test_func):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped_view
    return decorator


def is_member_of_groups(*group_names, strict=False):
    """
    Requires user membership in at least one of the groups passed in.
    from: https://djangosnippets.org/snippets/1703/
    """

    def in_groups(u):
        if u.is_authenticated():
            if u.is_superuser and not strict:
                return True
            if bool(u.groups.filter(name__in=group_names)):
                return True
        return False
    return user_passes_test_forbidden(in_groups)
