from django import forms

AGE_CHOICES= [
    (18, '18'),
    (19, '19'),
    (20, '20'),
    (21, '21'),
    (22, '22'),
    (23, '23'),
    (24, '24'),
    (25, '25'),
    (26, '26'),
    (27, '27'),
    (28, '28'),
    (29, '29'),
    (30, '30'),
    (31, '31'),
    (32, '32'),
    (33, '33'),
    (34, '34'),
    (35, '35'),
    (36, '36'),
    (37, '37'),
    (38, '38'),
    (39, '39'),
    (40, '40'),
    (41, '41'),
    (42, '42'),
    (43, '43'),
    (44, '44'),
    (45, '45'),
    (46, '46'),
    (47, '47'),
    (48, '48'),
    (49, '49'),
    (50, '50'),
    (51, '51'),
    (52, '52'),
    (53, '53'),
    (54, '54'),
    (55, '55'),
    (56, '56'),
    (57, '57'),
    (58, '58'),
    (59, '59'),
    (60, '60'),
    (61, '61'),
    (62, '62'),
    (63, '63'),
    (64, '64'),
    (65, '65'),
    (66, '66'),
    (67, '67'),
    (68, '68'),
    (69, '69'),
    (70, '70'),
    (71, '71'),
    (72, '72'),
    (73, '73'),
    (74, '74'),
    (75, '75'),
    (76, '76'),
    (77, '77'),
    (78, '78'),
    (79, '79'),
    (80, '80'),
    (81, '81'),
    (82, '82'),
    (83, '83'),
    (84, '84'),
    (85, '85'),
    (86, '86'),
    (87, '87'),
    (88, '88'),
    (89, '89'),
    (90, '90'),
    ]

GENDER_CHOICES= [
    (0, 'Female'),
    (1, 'Male'),
    ]

INCOME_CHOICES= [
    (0, 'less than $10,000 per year'),
    (1, '$10,000 to $19,999 per year'),
    (2, '$20,000 to $29,999 per year'),
    (3, '$30,000 to $39,999 per year'),
    (4, '$40,000 to $49,999 per year'),
    (5, '$50,000 to $59,999 per year'),
    (6, '$60,000 to $69,999 per year'),
    (7, '$70,000 to $79,999 per year'),
    (8, '$80,000 to $99,999 per year'),
    (9, '$100,000 to $119,999 per year'),
    (10, '$120,000 to $149,999 per year'),
    (11, '$150,000 to $199,999 per year'),
    (12, '$200,000 to $249,999 per year'),
    (13, '$250,000 to $349,999 per year'),
    (14, '$350,000 to $499,999 per year'),
    (14, '$500,000 or more per year'),
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

REGION_CHOICES= [
    ('1,0,0,0', 'Northeast'),
    ('0,1,0,0', 'Midwest'),
    ('0,0,1,0', 'South'),
    ('0,0,0,1', 'West'),
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

IMMIGRATION_CHOICES= [
    ('1,0,0,0', 'Immigrated citizen'),
    ('0,1,0,0', 'First generation'),
    ('0,0,1,0', 'Second generation'),
    ('0,0,0,1', 'Third generation'),
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


class UserInputForm(forms.Form):
    age = forms.CharField(label='What is your age?', widget=forms.Select(choices=AGE_CHOICES))
    gender = forms.CharField(label='Are you female or male?', widget=forms.Select(choices=GENDER_CHOICES))
    income = forms.CharField(label='What is your annual income (before tax)?', widget=forms.Select(choices=INCOME_CHOICES))
    education = forms.CharField(label='What is your highest level of education?', widget=forms.Select(choices=EDUCATION_CHOICES))
    marital_status = forms.CharField(label='Tell us your marital status', widget=forms.Select(choices=MARITAL_CHOICES))
    work = forms.CharField(label='What is your work status?', widget=forms.Select(choices=WORK_CHOICES))
    region = forms.CharField(label='Tell us where you live', widget=forms.Select(choices=REGION_CHOICES))
    religion = forms.CharField(label='Tell us what religion (if any) you identify with', widget=forms.Select(choices=RELIGION_CHOICES))
    immigration = forms.CharField(label='What is your immigration background?', widget=forms.Select(choices=IMMIGRATION_CHOICES))
    ethnicity = forms.CharField(label='Tell us your ethnicity', widget=forms.Select(choices=ETHNICITY_CHOICES))
