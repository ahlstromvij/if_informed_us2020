from django import forms

OK_CHOICES= [
    (1, 'OK'),
    ]

GENDER_CHOICES= [
    (0, 'Female'),
    (1, 'Male'),
    ]

AGE_CHOICES= [
    ('0,0,0,0,0,1', 'Under 30'),
    ('1,0,0,0,0,0', '30-39'),
    ('0,1,0,0,0,0', '40-49'),
    ('0,0,1,0,0,0', '50-59'),
    ('0,0,0,1,0,0', '60-69'),
    ('0,0,0,0,1,0', '70 or over'),
    ]

EDUCATION_CHOICES= [
    ('0,0,1,0,0,0', 'No High School'),
    ('0,1,0,0,0,0', 'High School'),
    ('0,0,0,0,1,0', 'Some College'),
    ('0,0,0,0,0,1', '2-year College'),
    ('1,0,0,0,0,0', '4-year College'),
    ('0,0,0,1,0,0', 'Postgraduate'),
    ]

MARITAL_CHOICES= [
    ('0,0,1,0,0,0', 'Married'),
    ('0,0,0,0,1,0', 'Separated'),
    ('0,1,0,0,0,0', 'Divorced'),
    ('0,0,0,0,0,1', 'Widowed'),
    ('0,0,0,1,0,0', 'Single'),
    ('1,0,0,0,0,0', 'Civil partnership'),
    ]

ETHNICITY_CHOICES= [
    ('1,0,0,0,0,0,0', 'Asian'),
    ('0,1,0,0,0,0,0', 'Black'),
    ('0,0,1,0,0,0,0', 'Hispanic'),
    ('0,0,0,1,0,0,0', 'Mixed'),
    ('0,0,0,0,1,0,0', 'Native american'),
    ('0,0,0,0,0,0,1', 'White'),
    ('0,0,0,0,0,1,0', 'Other race'),
    ]

INCOME_CHOICES= [
    ('0,0,0,0,1,0', 'Less than $20,000'),
    ('0,1,0,0,0,0', '$20,000 - $29,000'),
    ('0,0,1,0,0,0', '$30,000 - $59,000'),
    ('0,0,0,1,0,0', '$60,000 - $119,000'),
    ('1,0,0,0,0,0', '$120,000 - $200,000'),
    ('0,0,0,0,0,1', 'Over $200,000'),
    ]

RELIGION_CHOICES= [
    ('1,0,0,0,0,0,0', 'Buddhist'),
    ('0,1,0,0,0,0,0', 'Christian'),
    ('0,0,1,0,0,0,0', 'Jewish'),
    ('0,0,0,1,0,0,0', 'Mormon'),
    ('0,0,0,0,1,0,0', 'Muslim'),
    ('0,0,0,0,0,1,0', 'No religion'),
    ('0,0,0,0,0,0,1', 'Other religion'),
    ]

class UserInputForm(forms.Form):
    gender = forms.CharField(label='OK, great. So, first question: are you female or male?', widget=forms.Select(choices=GENDER_CHOICES))
    age = forms.CharField(label='Thank you! What is your age?', widget=forms.Select(choices=AGE_CHOICES))
    education = forms.CharField(label='And what is your highest level of education?', widget=forms.Select(choices=EDUCATION_CHOICES))
    marital_status = forms.CharField(label='And your marital status?', widget=forms.Select(choices=MARITAL_CHOICES))
    ethnicity = forms.CharField(label='What is your ethnicity?', widget=forms.Select(choices=ETHNICITY_CHOICES))
    income = forms.CharField(label='What is your annual household income (before tax)?', widget=forms.Select(choices=INCOME_CHOICES))
    religion = forms.CharField(label='And the final question: What religion (if any) do you identify with?', widget=forms.Select(choices=RELIGION_CHOICES))
