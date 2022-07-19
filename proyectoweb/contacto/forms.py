from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.CharField(label="E-mail", required=True)
    contenido=forms.CharField(widget=forms.Textarea,label="Contenido")
    
 

