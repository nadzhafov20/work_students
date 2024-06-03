from django.shortcuts import redirect
from functools import wraps


def user_is_authenticated(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return function(request, *args, **kwargs)
    return wrap

def email_verified_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.email_verified:
            return redirect('success_url')
        return function(request, *args, **kwargs)
    return wrap

def role_required(role):
    def decorator(function):
        @wraps(function)
        def wrap(request, *args, **kwargs):
            if not hasattr(request.user, 'role') or request.user.role != role:
                return redirect('index')
            return function(request, *args, **kwargs)
        return wrap
    return decorator