from django import template
from ..models import AdModel


register = template.Library()

@register.inclusion_tag('ad/home_page.html')
def display_ad_homepage(placement):
    ads = AdModel.objects.filter(placement=placement)
    return {'ads': ads}

@register.inclusion_tag('ad/bottom.html')
def display_ad_bottom(placement):
    ads = AdModel.objects.filter(placement=placement)
    return {'ads': ads}

@register.inclusion_tag('ad/block.html')
def display_ad_block(placement):
    ads = AdModel.objects.filter(placement=placement)
    return {'ads': ads}

@register.inclusion_tag('ad/ad_template.html')
def display_ad(placement):
    ads = AdModel.objects.filter(placement=placement)
    return {'ads': ads}

@register.inclusion_tag('ad/header.html')
def display_header_ad(placement):
    ads = AdModel.objects.filter(placement=placement)
    return {'ads': ads}

@register.inclusion_tag('ad/right_block.html')
def display_right_block_ad(placement):
    ads = AdModel.objects.filter(placement=placement)
    return {'ads': ads}

@register.inclusion_tag('ad/sticky_right.html')
def display_sticky_ad(placement):
    ads = AdModel.objects.filter(placement=placement)
    return {'ads': ads}

@register.inclusion_tag('ad/popup.html')
def display_popup_ad(placement):
    ads = AdModel.objects.filter(placement='popup')
    return {'ads': ads}
