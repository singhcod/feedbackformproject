from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label = 'Enter Your name :',
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'

            }
        )

    )
    rating = forms.IntegerField(
        label='Enter your Rating:',
        widget = forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label = 'Enter your feedback',
        widget = forms.Textarea(
            attrs = {
                'class':'form-control',
                'placeholder':'enter your feedback'
            }
        )
    )