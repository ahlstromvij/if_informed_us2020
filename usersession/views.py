from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserInputForm
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from joblib import load
from django.templatetags.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
import os
from django.conf import settings

class HomePageView(TemplateView):
	template_name = 'home.html'

class IntroPageView(TemplateView):
	template_name = 'intro.html'

def questions(request):
    form = UserInputForm()
    return render(request, 'userinputform.html', {'form':form});

class ResultsView(TemplateView):
    template_name = 'results.html'

    def post(self, request):
        context = {}

        user_input_raw = [
            request.POST['age'],
            request.POST['gender'],
            request.POST['income'],
			'0.824027',
            request.POST['education'],
            request.POST['marital_status'],
            request.POST['work'],
            request.POST['region'],
            request.POST['religion'],
            request.POST['immigration'],
            request.POST['ethnicity']
        ]

        user_input = [float(x) for item in user_input_raw for x in item.split(',')]

        user_series = pd.Series(user_input,index=['birthyr',
                            'gender',
                            'faminc_new',
                            'ability',
                            'no_hs',
                            'high_school',
                            'some_college',
                            'two_yr_college',
                            'four_yr_college',
                            'post_grad',
                            'married',
                            'separated',
                            'divorced',
                            'widowed',
                            'never_married',
                            'civil',
                            'full_time',
                            'part_time',
                            'unemployed',
                            'retired',
                            'disabled',
                            'homemaker',
                            'student',
                            'other_empl',
                            'northeast',
                            'midwest',
                            'south',
                            'west',
                            'christian',
                            'mormon',
                            'jewish',
                            'muslim',
                            'buddhist',
                            'no_rel',
                            'other_rel',
                            'immig_citizen',
                            'first_gen',
                            'second_gen',
                            'third_gen',
                            'white',
                            'black',
                            'hispanic',
                            'asian',
                            'native_american',
                            'mixed',
                            'other_race'])

        file1 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_immig.joblib'),'rb')
        log_reg_immig = load(file1)
        probs_imm = log_reg_immig.predict_proba([user_series])
        probs_formatted_imm = [round(elem, 2) for elem in probs_imm.tolist()[0]]
        context["immigration_probs"] = round(probs_formatted_imm[1] * 100, 0)

        if probs_formatted_imm[1] <= 0.2:
            context['imm_position'] = "highly unlikely"
        if probs_formatted_imm[1] > 0.2 and probs_formatted_imm[1] < 0.5:
            context['imm_position'] = "unlikely"
        if probs_formatted_imm[1] >= 0.5 and probs_formatted_imm[1] < 0.8:
            context['imm_position'] = "likely"
        if probs_formatted_imm[1] >= 0.8:
            context['imm_position'] = "highly likely"

        file2 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_illimcrime.joblib'),'rb')
        log_reg_illimcrime = load(file2)
        probs_ill = log_reg_illimcrime.predict_proba([user_series])
        probs_formatted_ill = [round(elem, 2) for elem in probs_ill.tolist()[0]]
        context["illimcrime_probs"] = round(probs_formatted_ill[1] * 100, 0)

        if probs_formatted_ill[1] <= 0.2:
            context['illimcrime_position'] = "highly unlikely"
        if probs_formatted_ill[1] > 0.2 and probs_formatted_ill[1] < 0.5:
            context['illimcrime_position'] = "unlikely"
        if probs_formatted_ill[1] >= 0.5 and probs_formatted_ill[1] < 0.8:
            context['illimcrime_position'] = "likely"
        if probs_formatted_ill[1] >= 0.8:
            context['illimcrime_position'] = "highly likely"

        file3 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_imigcit.joblib'),'rb')
        log_reg_imigcit = load(file3)
        probs_imigcit = log_reg_imigcit.predict_proba([user_series])
        probs_formatted_imigcit = [round(elem, 2) for elem in probs_imigcit.tolist()[0]]
        context["imigcit_probs"] = round(probs_formatted_imigcit[1] * 100, 0)

        if probs_formatted_imigcit[1] <= 0.2:
            context['imigcit_position'] = "highly unlikely"
        if probs_formatted_imigcit[1] > 0.2 and probs_formatted_imigcit[1] < 0.5:
            context['imigcit_position'] = "unlikely"
        if probs_formatted_imigcit[1] >= 0.5 and probs_formatted_imigcit[1] < 0.8:
            context['imigcit_position'] = "likely"
        if probs_formatted_imigcit[1] >= 0.8:
            context['imigcit_position'] = "highly likely"

        file4 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_ice.joblib'),'rb')
        log_reg_ice = load(file4)
        probs_ice = log_reg_ice.predict_proba([user_series])
        probs_formatted_ice = [round(elem, 2) for elem in probs_ice.tolist()[0]]
        context["ice_probs"] = round(probs_formatted_ice[1] * 100, 0)

        if probs_formatted_ice[1] <= 0.2:
            context['ice_position'] = "highly unlikely"
        if probs_formatted_ice[1] > 0.2 and probs_formatted_ice[1] < 0.5:
            context['ice_position'] = "unlikely"
        if probs_formatted_ice[1] >= 0.5 and probs_formatted_ice[1] < 0.8:
            context['ice_position'] = "likely"
        if probs_formatted_ice[1] >= 0.8:
            context['ice_position'] = "highly likely"

        file5 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_acarepeal.joblib'),'rb')
        log_reg_acarepeal = load(file5)
        probs_aca = log_reg_acarepeal.predict_proba([user_series])
        probs_formatted_aca = [round(elem, 2) for elem in probs_aca.tolist()[0]]
        context["aca_probs"] = round(probs_formatted_aca[1] * 100, 0)

        if probs_formatted_aca[1] <= 0.2:
            context['aca_position'] = "highly unlikely"
        if probs_formatted_aca[1] > 0.2 and probs_formatted_aca[1] < 0.5:
            context['aca_position'] = "unlikely"
        if probs_formatted_aca[1] >= 0.5 and probs_formatted_aca[1] < 0.8:
            context['aca_position'] = "likely"
        if probs_formatted_aca[1] >= 0.8:
            context['aca_position'] = "highly likely"

        file6 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_diversity.joblib'),'rb')
        log_reg_diversity = load(file6)
        probs_diversity = log_reg_diversity.predict_proba([user_series])
        probs_formatted_diversity = [round(elem, 2) for elem in probs_diversity.tolist()[0]]
        context["diversity_probs"] = round(probs_formatted_diversity[1] * 100, 0)

        if probs_formatted_diversity[1] <= 0.2:
            context['diversity_position'] = "highly unlikely"
        if probs_formatted_diversity[1] > 0.2 and probs_formatted_diversity[1] < 0.5:
            context['diversity_position'] = "unlikely"
        if probs_formatted_diversity[1] >= 0.5 and probs_formatted_diversity[1] < 0.8:
            context['diversity_position'] = "likely"
        if probs_formatted_diversity[1] >= 0.8:
            context['diversity_position'] = "highly likely"

        file7 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_gunsar.joblib'),'rb')
        log_reg_gunsar = load(file7)
        probs_gunsar = log_reg_gunsar.predict_proba([user_series])
        probs_formatted_gunsar = [round(elem, 2) for elem in probs_gunsar.tolist()[0]]
        context["gunsar_probs"] = round(probs_formatted_gunsar[1] * 100, 0)

        if probs_formatted_gunsar[1] <= 0.2:
            context['gunsar_position'] = "highly unlikely"
        if probs_formatted_gunsar[1] > 0.2 and probs_formatted_gunsar[1] < 0.5:
            context['gunsar_position'] = "unlikely"
        if probs_formatted_gunsar[1] >= 0.5 and probs_formatted_gunsar[1] < 0.8:
            context['gunsar_position'] = "likely"
        if probs_formatted_gunsar[1] >= 0.8:
            context['gunsar_position'] = "highly likely"

        liberal_score = probs_formatted_imm[1] + probs_formatted_ill[0] + probs_formatted_imigcit[1] + probs_formatted_ice[0] + probs_formatted_aca[0] + probs_formatted_diversity[1] + probs_formatted_gunsar[1]

        if liberal_score < 2:
            context["liberal_position"] = "committed conservative"
        if liberal_score >= 2.5 and liberal_score <= 4:
            context["liberal_position"] = "moderate conservative"
        if liberal_score > 4 and liberal_score <= 5.5:
            context["liberal_position"] = "moderate progressive"
        if liberal_score >  5.5:
            context["liberal_position"] = "committed progressive"

        context["liberal_score"] = round(liberal_score,2)

        return render(request, 'results.html', context)
