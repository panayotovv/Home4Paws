from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.shortcuts import redirect, render
from User.forms import SignUpForm, LoginForm, AdoptionForm
from .models import Dog, Adoption
from django.contrib.auth import login


class IndexView(ListView):
    template_name = "index.html"
    model = Dog

    def get_queryset(self):
        return Dog.objects.all().order_by("name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["login_form"] = LoginForm()
        context["signup_form"] = SignUpForm()

        return context



class DogDetailView(DetailView):
    template_name = 'detail.html'
    model = Dog

    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dog = self.object
        context["vaccinated_text"] = "Yes" if dog.health_status.filter(name="Vaccinated").exists() else "No"
        context["adoption_form"] = AdoptionForm()
        context["show_success"] = self.request.GET.get("success") == "true"
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(request.META.get('HTTP_REFERER', '/') + '?login_required=1')

        self.object = self.get_object()
        adoption_form = AdoptionForm(request.POST)

        if adoption_form.is_valid():
            dog = self.object
            Adoption.objects.create(
                dog=dog,
                owner=request.user,
                **adoption_form.cleaned_data
            )
            dog.owner = request.user
            dog.save()
            return redirect(f"/dog/{dog.name}/?success=true")

        else:
            context = self.get_context_data(adoption_form=adoption_form, show_success=True)
            return self.render_to_response(context)

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            next_url = request.POST.get('next', '/')
            return redirect(next_url)

        messages.error(request, "Invalid username or password", extra_tags="login")

    return redirect(request.META.get("HTTP_REFERER", "/") + "?login_error=1")


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            form.save_m2m()
            login(request, user)
            return redirect("index")

        messages.error(request, "Signup failed. Please check the form.", extra_tags="signup")

    return redirect(request.META.get("HTTP_REFERER", "index") + "?signup_error=1")

def donate_view(request):
    return render(request, "donate.html", {
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY
    })




