#A class that defines the shape of our form
#and the different inputs we want
#and the validation rules for those inputs.

from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name= forms.CharField(label="Your name", max_length=30, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Please enter a shorter name!"
#     })
#     review_text = forms.CharField(label = "Your Feedback!", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating",min_value=1,max_value=5)

# using ModelForm
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__' #Receive All fields or properties in the model received from render
        # exclude = ['owner_comment'] # Render everything except one fromat
        labels = {
            "user_name":"Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }

        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!"
            }
        }