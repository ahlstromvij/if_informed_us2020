from django import forms

GENDER_CHOICES= [
    (0, 'Female'),
    (1, 'Male'),
    ]

AGE_CHOICES= [
    ('1,0,0,0,0,0', 'Under 30'),
    ('0,1,0,0,0,0', '30-39'),
    ('0,0,1,0,0,0', '40-49'),
    ('0,0,0,1,0,0', '50-59'),
    ('0,0,0,0,1,0', '60-69'),
    ('0,0,0,0,0,1', '70 or over'),
    ]

EDUCATION_CHOICES= [
    ('1,0,0,0,0,0', 'No High School'),
    ('0,1,0,0,0,0', 'High School'),
    ('0,0,1,0,0,0', 'Some College'),
    ('0,0,0,1,0,0', '2-year College'),
    ('0,0,0,0,1,0', '4-year College'),
    ('0,0,0,0,0,1', 'Postgraduate'),
    ]

MARITAL_CHOICES= [
    ('1,0,0,0,0,0', 'Married'),
    ('0,1,0,0,0,0', 'Separated'),
    ('0,0,1,0,0,0', 'Divorced'),
    ('0,0,0,1,0,0', 'Widowed'),
    ('0,0,0,0,1,0', 'Single'),
    ('0,0,0,0,0,1', 'Civil partnership'),
    ]

ETHNICITY_CHOICES= [
    ('1,0,0,0,0,0,0', 'White'),
    ('0,1,0,0,0,0,0', 'Black'),
    ('0,0,1,0,0,0,0', 'Hispanic'),
    ('0,0,0,1,0,0,0', 'Asian'),
    ('0,0,0,0,1,0,0', 'Native american'),
    ('0,0,0,0,0,1,0', 'Mixed'),
    ('0,0,0,0,0,0,1', 'Other race'),
    ]

WORK_CHOICES= [
    ('1,0,0,0,0,0,0,0', 'Full-time work'),
    ('0,1,0,0,0,0,0,0', 'Part-time work'),
    ('0,0,1,0,0,0,0,0', 'Unemployed'),
    ('0,0,0,1,0,0,0,0', 'Retired'),
    ('0,0,0,0,1,0,0,0', 'Permanently disabled'),
    ('0,0,0,0,0,1,0,0', 'Homemaker'),
    ('0,0,0,0,0,0,1,0', 'Student'),
    ('0,0,0,0,0,0,0,1', 'Other employment'),
    ]

INCOME_CHOICES= [
    ('1,0,0,0,0,0', 'Less than $20,000'),
    ('0,1,0,0,0,0', '$20,000 - $29,000'),
    ('0,0,1,0,0,0', '$30,000 - $59,000'),
    ('0,0,0,1,0,0', '$60,000 - $119,000'),
    ('0,0,0,0,1,0', '$120,000 - $200,000'),
    ('0,0,0,0,0,1', 'Over $200,000'),
    ]

RELIGION_CHOICES= [
    ('1,0,0,0,0,0,0', 'Christian'),
    ('0,1,0,0,0,0,0', 'Mormon'),
    ('0,0,1,0,0,0,0', 'Jewish'),
    ('0,0,0,1,0,0,0', 'Muslim'),
    ('0,0,0,0,1,0,0', 'Buddhist'),
    ('0,0,0,0,0,1,0', 'No religion'),
    ('0,0,0,0,0,0,1', 'Other religion'),
    ]

REGION_CHOICES= [
    ('1,0,0,0', 'Northeast'),
    ('0,1,0,0', 'Midwest'),
    ('0,0,1,0', 'South'),
    ('0,0,0,1', 'West'),
    ]

class UserInputForm(forms.Form):
    gender = forms.CharField(label='Are you female or male?', widget=forms.Select(choices=GENDER_CHOICES))
    age = forms.CharField(label='What is your age?', widget=forms.Select(choices=AGE_CHOICES))
    education = forms.CharField(label='What is your highest level of education?', widget=forms.Select(choices=EDUCATION_CHOICES))
    marital_status = forms.CharField(label='Tell us your marital status', widget=forms.Select(choices=MARITAL_CHOICES))
    ethnicity = forms.CharField(label='Tell us your ethnicity', widget=forms.Select(choices=ETHNICITY_CHOICES))
    work = forms.CharField(label='What is your work status?', widget=forms.Select(choices=WORK_CHOICES))
    income = forms.CharField(label='What is your annual income (before tax)?', widget=forms.Select(choices=INCOME_CHOICES))
    religion = forms.CharField(label='Tell us what religion (if any) you identify with', widget=forms.Select(choices=RELIGION_CHOICES))
    region = forms.CharField(label='Tell us where you live', widget=forms.Select(choices=REGION_CHOICES))    
