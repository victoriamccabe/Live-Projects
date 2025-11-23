from django import forms
from .models import PlaceRecommendation


# Form for recommending a new place (with photo)
class PlaceRecommendationForm(forms.ModelForm):
    class Meta:
        model = PlaceRecommendation
        fields = ['place_name', 'province', 'description', 'your_name','score']
        widgets = {
            'score': forms.RadioSelect(attrs={'class': 'horizontal-radio'}),
        }


