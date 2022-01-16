from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.views.decorators.http import require_http_methods

from project.tokens import account_activation_token
from project.decorators import check_recaptcha
from project.forms import UserSignUpForm
from project.settings import config

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from django.contrib.auth import get_user_model
User = get_user_model()


@check_recaptcha
@require_http_methods(["GET", "POST"])
def register(request):
    """Register new users and send verification mails to their email addresses."""
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:  # checking the form and RECAPTCHA with decorator
            email = request.POST.get('email')

            site = get_current_site(request) # for the domain
            
            user = form.save(commit=False) # add all information from the form in the User model
            user.is_active = False  # user is only active after confirming the email!
            user.save() # save the User model 

            message = render_to_string('account/activate_account_mail.html', {
                'user': user,
                'protocol': 'http',
                'domain': site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })  # filling the  activation mail template w/ all the variables 

            # This part can be found in the SendGrid setup guide as well
            message = Mail(
                from_email='noreply@domain.com',
                to_emails=email,
                subject='Activate account for domain.com',
                html_content=message)
            try:
                sg = SendGridAPIClient(config['SENDGRID_API_KEY']) # config file where I keep my keys
                response = sg.send(message)  # .status_code, .body, .headers
                messages.add_message(request, messages.SUCCESS, 'A verification email has been sent.')
                messages.add_message(request, messages.WARNING, 'Please also check your SPAM inbox!')
            except Exception as e:
                print(e)  # e.message
                messages.add_message(request, messages.WARNING, str(e))
        else:
            return render(request, 'account/register.html', {'form': form})

    return render(request, 'account/register.html', {'form': UserSignUpForm()})