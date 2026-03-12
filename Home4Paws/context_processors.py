from User.forms import LoginForm, SignUpForm

def auth_forms(request):
    return {
        "login_form": LoginForm(),
        "signup_form": SignUpForm(),
    }