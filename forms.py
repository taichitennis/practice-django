from django import forms

class FormA(forms.Form):
    name=forms.CharField(label='学籍番号')
    undergraduate=forms.CharField(label='学部')

