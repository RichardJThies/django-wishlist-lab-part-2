from django import forms
from .models import Place#pulling class from other module
"""Form to add new places. Enters data in db"""

class NewPlaceForm(forms.ModelForm):#subclass(?) because it is related to the model
    class Meta:
        model = Place
        fields = ('name', 'visited')#Tuple of the model fields. These are the fields that will be displayed in the html form to the user. 
        #^^Pk is NOT included because there is no reason for user to see it, and it is autogenerated anyways by db^^




