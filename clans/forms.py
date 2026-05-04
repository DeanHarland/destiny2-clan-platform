from django import forms
from .models import Clan

class ClanForm(forms.ModelForm):
    class Meta:
        model = Clan
        fields = ['name', 'tag', 'description', 'clan_type']
        