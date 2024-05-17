from django.shortcuts import render, redirect, get_object_or_404
from offer_app.models import RatesOfferModel, OffersModel
from .forms import RateForm
from main.models import MyUser


def offer_detail(request, offer_id):
    offer = get_object_or_404(OffersModel, pk=offer_id)
    rates = RatesOfferModel.objects.filter(offer=offer)
    user = request.user
    user_rate_exists = RatesOfferModel.objects.filter(offer=offer, student=user).exists()

    if request.method == 'POST':
        if hasattr(request.user, 'role'):
            if request.user.role == 'client':
                user_id = request.POST.get('user_id')

                print(f'FFFFFFFFFFFFFFF:  {user_id}   {offer_id}')
                offer = OffersModel.objects.get(id=offer_id)
                user_student = MyUser.objects.get(id=user_id)
                offer.user_student = user_student
                offer.save()
                return redirect('offer_detail', offer_id=offer_id)

            if request.user.role == 'student':
                if user_rate_exists:
                    return redirect('offer_detail', offer_id=offer_id)
                
                form = RateForm(request.POST)
                if form.is_valid():
                    rate = form.save(commit=False)
                    rate.student = request.user
                    rate.offer = offer
                    rate.save()
                    return redirect('offer_detail', offer_id=offer_id)
    else:
        if user_rate_exists:
            form = None
        else:
            form = RateForm()

    return render(request, 'offer/offer_detail.html', {'offer': offer, 'rates': rates, 'user': user, 'form': form, 'user_rate_exists':user_rate_exists})


def select_rate(request, rate_id):
    rate = get_object_or_404(RatesOfferModel, id=rate_id)
    offer = rate.offer
    if request.method == 'POST':
        if request.user.role == 'client':
            offer.user_student = rate.student
            offer.save()

    return redirect('offer_detail', offer_id=offer.id)


def offer_view(request, offer_id):
    offer = get_object_or_404(OffersModel, id=offer_id)
    user = request.user
    return render(request, 'offer/offer_view.html', {'offer':offer,'user':user})