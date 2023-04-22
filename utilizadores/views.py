from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, Q, F
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .tokens import account_activation_token


def activateEmail(request, user, to_email):
    mail_subject = 'Activar a sua conta.'
    message = render_to_string('utilizadores/template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')
        return redirect('inicio')


def registar(request):
    if request.method == 'POST':
        uform = NewUserForm(request.POST)
        if uform.is_valid():
            username = uform.cleaned_data.get('username')
            user = uform.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, uform.cleaned_data.get('email'))
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
        else:
            messages.error(request, 'Formulário com erros')
            messages.error(request, uform.errors)
    else:
        uform = NewUserForm()
        context = {'uform': uform,}
    return render(request, 'utilizadores/registo.html', context)


@login_required
def perfil(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = PerfilForm(request.POST,
                                   request.FILES,
                                   instance=request.user.perfil)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()

            messages.success(request, 'Perfil atualizado com sucesso.')
        else:
            messages.error(request, 'Formulário com erros')
            messages.error(request, uform.errors)
            messages.error(request, pform.errors)
        return redirect('perfil') # Redirect back to profile page

    else:
        uform = UserUpdateForm(instance=request.user)
        pform = PerfilForm(instance=request.user.perfil)

        context = {
            'uform': uform,
            'pform': pform
        }

        return render(request, 'utilizadores/perfil.html', context)

