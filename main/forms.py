from django import forms


class ProductFilterForm(forms.Form):

    CATEGORY_CHOICES = [
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
        ('category3', 'Category 3'),
        ('category3', 'Category 3'),

    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)
    discount_price_min = forms.DecimalField(min_value=0, max_value=10000, required=False)
    discount_price_max = forms.DecimalField(min_value=0, max_value=10000, required=False)
    discount_percent_min = forms.IntegerField(min_value=0, max_value=100, required=False)
    discount_percent_max = forms.IntegerField(min_value=0, max_value=100, required=False)