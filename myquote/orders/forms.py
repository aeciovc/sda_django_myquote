from django.forms import forms
from .models import Order, Product
from django import forms


class CreateOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['date_for_product', 'product', 'comment']

    date_for_product = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={
                'class': '',
                'placeholder': 'Select a date'
            }
        ),
        required=True,
    )
    product = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                'class': '',
                'placeholder': 'Select a product'
            }
        ),
        queryset=Product.objects.order_by('name'),
        required=True
    ),
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': '',
                'placeholder': 'Leave a comment'
            }
        )
    )
    quantity = forms.IntegerField(
            widget=forms.NumberInput(
                attrs={
                    'class': '',
                    'placeholder': 'Select a quantity'
                }
            )
        )


