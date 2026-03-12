from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from Dog.models import Dog
from User.forms import ImageForm, EditProfileForm
import stripe
from django.conf import settings
from django.http import JsonResponse

User = get_user_model()


class ProfileView(DetailView):
    template_name = 'profile.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        context['dogs'] = Dog.objects.filter(owner_id=user.pk)
        context['image_form'] = ImageForm()
        context['user_roles'] = user.roles.all()
        context['edit_form'] = EditProfileForm(instance=user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if 'image' in request.FILES:
            image_form = ImageForm(request.POST, request.FILES, instance=self.object)
            if image_form.is_valid():
                image_form.save()
        else:
            edit_form = EditProfileForm(request.POST, instance=self.object)
            if edit_form.is_valid():
                edit_form.save()
            else:
                context = self.get_context_data()
                context['edit_form'] = edit_form
                return self.render_to_response(context)

        return redirect('profile', pk=self.object.pk)


stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_payment_intent(request):
    intent = stripe.PaymentIntent.create(
        amount=500,
        currency="usd",
        automatic_payment_methods={"enabled": True},
    )

    return JsonResponse({"clientSecret": intent.client_secret})