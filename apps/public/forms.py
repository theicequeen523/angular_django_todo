from .models import Recipe
from django.forms import ModelForm


class AddRecipeForm(ModelForm):
    class Meta:
        model = Recipe

    def __init__(self, *args, **kwargs):
        super(AddRecipeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Recipe Name'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Recipe Description'})
        self.fields['link'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Recipe Link'})
        self.fields['prep_time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Preparation Time'})
        self.fields['ingredient'].widget.attrs.update({'class': 'form-control'})
        self.fields['instruction'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Instructions'})
        self.fields['temp'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Temperature'})
        self.fields['time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Cook Time'})
        self.fields['serv_size'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Serving Size'})
        self.fields['tag'].widget.attrs.update({'class': 'form-control'})
        self.fields['public_recipe'].widget.attrs.update({'class': 'form-control'})


class EditRecipeForm(ModelForm):
    class Meta:
        model = Recipe

    def __init__(self, *args, **kwargs):
        super(EditRecipeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Recipe Name'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Recipe Description'})
        self.fields['link'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Recipe Link'})
        self.fields['prep_time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Preparation Time'})
        self.fields['ingredient'].widget.attrs.update({'class': 'form-control'})
        self.fields['instruction'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Instructions'})
        self.fields['temp'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Temperature'})
        self.fields['time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Cook Time'})
        self.fields['serv_size'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Serving Size'})
        self.fields['tag'].widget.attrs.update({'class': 'form-control'})
        self.fields['public_recipe'].widget.attrs.update({'class': 'form-control'})