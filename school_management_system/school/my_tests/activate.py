from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from project.tokens import account_activation_token
from django.contrib.auth import get_user_model
User = get_user_model()


@require_http_methods(["GET"])
def activate(request, uidb64, token):
    """Check the activation token sent via mail."""
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        messages.add_message(request, messages.WARNING, str(e))
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True  # now we're activating the user
        user.profile.email_confirmed = True  # and we're changing the boolean field so that the token link becomes invalid
        user.save()
        login(request, user)  # log the user in
        messages.add_message(request, messages.INFO, 'Hi {0}.'.format(request.user))
    else:
        messages.add_message(request, messages.WARNING, 'Account activation link is invalid.')

    return redirect('home')