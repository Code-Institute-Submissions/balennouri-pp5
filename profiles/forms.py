from django import forms
from .models import UserProfile, ContactForm
from products.models import Review
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                # Set the label for each field
                self.fields[field].label = placeholders[field]  # Set label here
            self.fields[field].widget.attrs['class'] = (
                'border-black rounded-0 profile-form-input')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        help_texts = {
            'rating': 'Rating should be between 0 and 5',
        }

    def __init__(self, *args, **kwargs):
        self.product_name = kwargs.pop('product_name', None)
        super(ReviewForm, self).__init__(*args, **kwargs)

        if self.product_name:
            self.fields['product_name'] = (
                forms.CharField(initial=self.product_name,
                                widget=forms.HiddenInput())
                                )


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactFormForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(
            Submit('submit', 'Submit', css_class='btn-primary'))
