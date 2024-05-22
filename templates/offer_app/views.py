from django.shortcuts import render, redirect, get_object_or_404
from offer_app.models import RatesOfferModel, OffersModel, MessagesOfferModel
from .forms import RateForm, MessagesOfferForm
from main.models import MyUser
from django.http import JsonResponse


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
            offer.status = 'launched'
            offer.save()

    return redirect('offer_detail', offer_id=offer.id)


def offer_view(request, offer_id):
    offer = get_object_or_404(OffersModel, id=offer_id)
    user = request.user

    if request.method == 'POST':
        form = MessagesOfferForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.from_user = user
            message.offer = offer
            message.save()
            return redirect('offer_view', offer_id=offer_id)
    else:
        form_message = MessagesOfferForm()
    
    messages = MessagesOfferModel.objects.filter(offer=offer)

    return render(request, 'offer/offer_view.html', {'offer':offer,'user':user,'form_message':form_message, 'messages':messages})

def api_client_offer_status(request, offer_id):
    print(f"OFFER DELETE {offer_id}")
    offer = OffersModel.objects.get(id=offer_id)
    offer.status = 'completed'
    offer.save()
    return redirect('client_my_offers')

def api_client_offer_delete(request, offer_id):
    offer = OffersModel.objects.get(id=offer_id)
    if offer.user_student:
        return redirect('client_my_offers')
    else:
        offer.delete()
        return redirect('client_my_offers')

def api_get_message(request, offer_id):
    last_displayed_message = request.GET.get('last_displayed_message')
    print(last_displayed_message)
    messages = MessagesOfferModel.objects.filter(offer_id=offer_id, id__gt=last_displayed_message)
    
    messages_data = []
    for message in messages:
        message_data = {
            'id': message.id,
            'from_user': {
                'id': message.from_user.id,
                'first_name': message.from_user.first_name,
                'last_name': message.from_user.last_name,
                'image': message.from_user.image.url if message.from_user.image else ''
            },
            'message': message.message,
            'date_sent': message.date_sent.strftime('%Y-%m-%d %H:%M:%S')
        }
        messages_data.append(message_data)

    return JsonResponse({'messages': messages_data})