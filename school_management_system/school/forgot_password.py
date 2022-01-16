from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from project.decorators import check_recaptcha, unauthenticated_required
from project.tokens import password_reset_token
from project.forms import UserForgotPasswordForm
from project.settings import config

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from django.contrib.auth import get_user_model
User = get_user_model()


@check_recaptcha
@require_http_methods(["GET", "POST"])
@unauthenticated_required(home_url='/', redirect_field_name='')
def password_reset(request):
    """User forgot password form view."""
    msg = ''
    if request.method == "POST":
        form = UserForgotPasswordForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            email = request.POST.get('email')
            qs = User.objects.filter(email=email)
            site = get_current_site(request)

            if len(qs) > 0:
                user = qs[0]
                user.is_active = False  # User needs to be inactive for the reset password duration
                user.profile.reset_password = True
                user.save()

                message = render_to_string('account/password_reset_mail.html', {
                    'user': user,
                    'protocol': 'http',
                    'domain': site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })

                message = Mail(
                    from_email='noreply@domain.com',
                    to_emails=email,
                    subject='Reset password for domain.com',
                    html_content=message)
                try:
                    sg = SendGridAPIClient(config['SENDGRID_API_KEY'])
                    response = sg.send(message)
                except Exception as e:
                    print(e)

            messages.add_message(request, messages.SUCCESS, 'Email {0} submitted.'.format(email))
            msg = 'If this mail address is known to us, an email will be sent to your account.'
        else:
            messages.add_message(request, messages.WARNING, 'Email not submitted.')
            return render(request, 'account/password_reset_req.html', {'form': form})

    return render(request, 'account/password_reset_req.html', {'form': UserForgotPasswordForm, 'msg': msg})