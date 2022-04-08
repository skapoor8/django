from django import forms


class EditPostForm(forms.Form):
	title = forms.CharField(label="Title:", max_length=200)
	body = forms.CharField(label="Body:", widget=forms.Textarea)
	pub_date = forms.DateTimeField(label="Date Published:", widget=forms.TextInput(attrs={'readonly': 'readonly'}))