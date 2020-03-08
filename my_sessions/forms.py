from django import forms



from django.forms import ModelForm
from .models import Session
# from django.forms import Input

class DateInput(forms.DateInput):
	input_type = 'date'

class TimeInput(forms.TimeInput):
	input_type = 'time'

# class NotesInput(forms.Input):
	# input_type='textarea'

class AddSessionForm(ModelForm):
	class Meta:
		model = Session
		fields = ('title', 'venue', 'date', 'start_time', 'end_time', 'notes','open_student_registrations', 'open_student_registrations')		
		widgets = {'date':DateInput(), 'start_time':TimeInput(), 'end_time':TimeInput(), 'notes':forms.Textarea()}

