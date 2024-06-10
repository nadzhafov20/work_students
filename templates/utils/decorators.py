from django.shortcuts import redirect
from functools import wraps


def user_is_authenticated(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            print("User is not authenticated. Redirecting to login.")
            return redirect('login')
        print("User is authenticated. Proceeding with the view.")
        return function(request, *args, **kwargs)
    return wrap

def email_verified_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.email_verified:
            print("Email is not verified. Redirecting to success_url.")
            return redirect('success_url')
        print("Email is verified. Proceeding with the view.")
        return function(request, *args, **kwargs)
    return wrap

def role_required(role):
    def decorator(function):
        @wraps(function)
        def wrap(request, *args, **kwargs):
            if not hasattr(request.user, 'role') or request.user.role != role:
                print(f"User does not have the required role ({role}). Redirecting to index.")

                return redirect('index')
            print(f"User has the required role ({role}). Proceeding with the view.")

            return function(request, *args, **kwargs)
        return wrap
    return decorator