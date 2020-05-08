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
	template_name = 'questions.html' # changed from home

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
			'1',
			request.POST['gender'],
            request.POST['age'],
            request.POST['education'],
            request.POST['marital_status'],
            request.POST['ethnicity'],
            request.POST['income'],
            request.POST['religion'],
        ]

        user_input = [float(x) for item in user_input_raw for x in item.split(',')]

        user_series = pd.Series(user_input,index=['ability_binary',
                                                'gender',
                                                'age_30to40',
                                                'age_40to50',
                                                'age_50to60',
                                                'age_60to70',
                                                'age_over70',
                                                'age_under30',
                                                'four_yr_college',
                                                'high_school',
                                                'no_hs',
                                                'post_grad',
                                                'some_college',
                                                'two_yr_college',
                                                'civil',
                                                'divorced',
                                                'married',
                                                'never_married',
                                                'separated',
                                                'widowed',
                                                'asian',
                                                'black',
                                                'hispanic',
                                                'mixed',
                                                'native_american',
                                                'other_race',
                                                'white',
                                                'inc_120-200k',
                                                'inc_20-30k',
                                                'inc_30-60k',
                                                'inc_60-120k',
                                                'inc_less20k',
                                                'inc_over200k',
                                                'buddhist',
                                                'christian',
                                                'jewish',
                                                'mormon',
                                                'muslim',
                                                'no_rel',
                                                'other_rel'])

        file1 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_gw1.joblib'),'rb')
        log_reg_gw1 = load(file1)
        probs_gw1 = log_reg_gw1.predict_proba([user_series])
        probs_formatted_gw1 = [round(elem, 2) for elem in probs_gw1.tolist()[0]]
        context["gw1_probs"] = round(probs_formatted_gw1[1] * 100, 0)

        if probs_formatted_gw1[1] <= 0.2:
            context['gw1_position'] = "highly unlikely"
        if probs_formatted_gw1[1] > 0.2 and probs_formatted_gw1[1] < 0.5:
            context['gw1_position'] = "unlikely"
        if probs_formatted_gw1[1] >= 0.5 and probs_formatted_gw1[1] < 0.8:
            context['gw1_position'] = "likely"
        if probs_formatted_gw1[1] >= 0.8:
            context['gw1_position'] = "highly likely"

        file2 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_refugees.joblib'),'rb')
        log_reg_refugees = load(file2)
        probs_refugees = log_reg_refugees.predict_proba([user_series])
        probs_formatted_refugees = [round(elem, 2) for elem in probs_refugees.tolist()[0]]
        context["refugees_probs"] = round(probs_formatted_refugees[1] * 100, 0)

        if probs_formatted_refugees[1] <= 0.2:
            context['refugees_position'] = "highly unlikely"
        if probs_formatted_refugees[1] > 0.2 and probs_formatted_refugees[1] < 0.5:
            context['refugees_position'] = "unlikely"
        if probs_formatted_refugees[1] >= 0.5 and probs_formatted_refugees[1] < 0.8:
            context['refugees_position'] = "likely"
        if probs_formatted_refugees[1] >= 0.8:
            context['refugees_position'] = "highly likely"

        file3 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_trade4.joblib'),'rb')
        log_reg_trade4 = load(file3)
        probs_trade4 = log_reg_trade4.predict_proba([user_series])
        probs_formatted_trade4 = [round(elem, 2) for elem in probs_trade4.tolist()[0]]
        context["trade4_probs"] = round(probs_formatted_trade4[1] * 100, 0)

        if probs_formatted_trade4[1] <= 0.2:
            context['trade4_position'] = "highly unlikely"
        if probs_formatted_trade4[1] > 0.2 and probs_formatted_trade4[1] < 0.5:
            context['trade4_position'] = "unlikely"
        if probs_formatted_trade4[1] >= 0.5 and probs_formatted_trade4[1] < 0.8:
            context['trade4_position'] = "likely"
        if probs_formatted_trade4[1] >= 0.8:
            context['trade4_position'] = "highly likely"

        file4 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_richpoor2.joblib'),'rb')
        log_reg_richpoor2 = load(file4)
        probs_richpoor2 = log_reg_richpoor2.predict_proba([user_series])
        probs_formatted_richpoor2 = [round(elem, 2) for elem in probs_richpoor2.tolist()[0]]
        context["richpoor2_probs"] = round(probs_formatted_richpoor2[1] * 100, 0)

        if probs_formatted_richpoor2[1] <= 0.2:
            context['richpoor2_position'] = "highly unlikely"
        if probs_formatted_richpoor2[1] > 0.2 and probs_formatted_richpoor2[1] < 0.5:
            context['richpoor2_position'] = "unlikely"
        if probs_formatted_richpoor2[1] >= 0.5 and probs_formatted_richpoor2[1] < 0.8:
            context['richpoor2_position'] = "likely"
        if probs_formatted_richpoor2[1] >= 0.8:
            context['richpoor2_position'] = "highly likely"

        file5 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_immignum.joblib'),'rb')
        log_reg_immignum = load(file5)
        probs_immignum = log_reg_immignum.predict_proba([user_series])
        probs_formatted_immignum = [round(elem, 2) for elem in probs_immignum.tolist()[0]]
        context["immignum_probs"] = round(probs_formatted_immignum[1] * 100, 0)

        if probs_formatted_immignum[1] <= 0.2:
            context['immignum_position'] = "highly unlikely"
        if probs_formatted_immignum[1] > 0.2 and probs_formatted_immignum[1] < 0.5:
            context['immignum_position'] = "unlikely"
        if probs_formatted_immignum[1] >= 0.5 and probs_formatted_immignum[1] < 0.8:
            context['immignum_position'] = "likely"
        if probs_formatted_immignum[1] >= 0.8:
            context['immignum_position'] = "highly likely"

        file6 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_dreamer.joblib'),'rb')
        log_reg_dreamer = load(file6)
        probs_dreamer = log_reg_dreamer.predict_proba([user_series])
        probs_formatted_dreamer = [round(elem, 2) for elem in probs_dreamer.tolist()[0]]
        context["dreamer_probs"] = round(probs_formatted_dreamer[1] * 100, 0)

        if probs_formatted_dreamer[1] <= 0.2:
            context['dreamer_position'] = "highly unlikely"
        if probs_formatted_dreamer[1] > 0.2 and probs_formatted_dreamer[1] < 0.5:
            context['dreamer_position'] = "unlikely"
        if probs_formatted_dreamer[1] >= 0.5 and probs_formatted_dreamer[1] < 0.8:
            context['dreamer_position'] = "likely"
        if probs_formatted_dreamer[1] >= 0.8:
            context['dreamer_position'] = "highly likely"

        file7 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_freecol.joblib'),'rb')
        log_reg_freecol = load(file7)
        probs_freecol = log_reg_freecol.predict_proba([user_series])
        probs_formatted_freecol = [round(elem, 2) for elem in probs_freecol.tolist()[0]]
        context["freecol_probs"] = round(probs_formatted_freecol[1] * 100, 0)

        if probs_formatted_freecol[1] <= 0.2:
            context['freecol_position'] = "highly unlikely"
        if probs_formatted_freecol[1] > 0.2 and probs_formatted_freecol[1] < 0.5:
            context['freecol_position'] = "unlikely"
        if probs_formatted_freecol[1] >= 0.5 and probs_formatted_freecol[1] < 0.8:
            context['freecol_position'] = "likely"
        if probs_formatted_freecol[1] >= 0.8:
            context['freecol_position'] = "highly likely"

        file8 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_diversity5.joblib'),'rb')
        log_reg_diversity5 = load(file8)
        probs_diversity5 = log_reg_diversity5.predict_proba([user_series])
        probs_formatted_diversity5 = [round(elem, 2) for elem in probs_diversity5.tolist()[0]]
        context["diversity5_probs"] = round(probs_formatted_diversity5[1] * 100, 0)

        if probs_formatted_diversity5[1] <= 0.2:
            context['diversity5_position'] = "highly unlikely"
        if probs_formatted_diversity5[1] > 0.2 and probs_formatted_diversity5[1] < 0.5:
            context['diversity5_position'] = "unlikely"
        if probs_formatted_diversity5[1] >= 0.5 and probs_formatted_diversity5[1] < 0.8:
            context['diversity5_position'] = "likely"
        if probs_formatted_diversity5[1] >= 0.8:
            context['diversity5_position'] = "highly likely"

        file9 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_prek.joblib'),'rb')
        log_reg_prek = load(file9)
        probs_prek = log_reg_prek.predict_proba([user_series])
        probs_formatted_prek = [round(elem, 2) for elem in probs_prek.tolist()[0]]
        context["prek_probs"] = round(probs_formatted_prek[1] * 100, 0)

        if probs_formatted_prek[1] <= 0.2:
            context['prek_position'] = "highly unlikely"
        if probs_formatted_prek[1] > 0.2 and probs_formatted_prek[1] < 0.5:
            context['prek_position'] = "unlikely"
        if probs_formatted_prek[1] >= 0.5 and probs_formatted_prek[1] < 0.8:
            context['prek_position'] = "likely"
        if probs_formatted_prek[1] >= 0.8:
            context['prek_position'] = "highly likely"

        file10 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_rr2.joblib'),'rb')
        log_reg_rr2 = load(file10)
        probs_rr2 = log_reg_rr2.predict_proba([user_series])
        probs_formatted_rr2 = [round(elem, 2) for elem in probs_rr2.tolist()[0]]
        context["rr2_probs"] = round(probs_formatted_rr2[1] * 100, 0)

        if probs_formatted_rr2[1] <= 0.2:
            context['rr2_position'] = "highly unlikely"
        if probs_formatted_rr2[1] > 0.2 and probs_formatted_rr2[1] < 0.5:
            context['rr2_position'] = "unlikely"
        if probs_formatted_rr2[1] >= 0.5 and probs_formatted_rr2[1] < 0.8:
            context['rr2_position'] = "likely"
        if probs_formatted_rr2[1] >= 0.8:
            context['rr2_position'] = "highly likely"

        file11 = open(os.path.join(settings.STATIC_ROOT, 'scikit/log_reg_taxecon.joblib'),'rb')
        log_reg_taxecon = load(file11)
        probs_taxecon = log_reg_taxecon.predict_proba([user_series])
        probs_formatted_taxecon = [round(elem, 2) for elem in probs_taxecon.tolist()[0]]
        context["taxecon_probs"] = round(probs_formatted_taxecon[1] * 100, 0)

        if probs_formatted_taxecon[1] <= 0.2:
            context['taxecon_position'] = "highly unlikely"
        if probs_formatted_taxecon[1] > 0.2 and probs_formatted_taxecon[1] < 0.5:
            context['taxecon_position'] = "unlikely"
        if probs_formatted_taxecon[1] >= 0.5 and probs_formatted_taxecon[1] < 0.8:
            context['taxecon_position'] = "likely"
        if probs_formatted_taxecon[1] >= 0.8:
            context['taxecon_position'] = "highly likely"

        econ_liberal_score = probs_formatted_taxecon[1] + probs_formatted_freecol[0] + probs_formatted_richpoor2[0] + probs_formatted_prek[0] + probs_formatted_gw1[0]
        social_liberal_score = probs_formatted_diversity5[1] + probs_formatted_rr2[1] + probs_formatted_immignum[1] + probs_formatted_dreamer[1] + probs_formatted_refugees[1]

        context["econ_liberal_score"] = round(econ_liberal_score,2)
        context["social_liberal_score"] = round(social_liberal_score,2)

        if econ_liberal_score < 2:
            context["econ_liberal_position"] = "fiscally progressive"
        if econ_liberal_score >= 2 and econ_liberal_score <= 3:
            context["econ_liberal_position"] = "fiscally moderate"
        if econ_liberal_score > 3:
            context["econ_liberal_position"] = "fiscally conservative"

        if social_liberal_score < 2:
            context["social_liberal_position"] = "socially conservative"
        if social_liberal_score >= 2 and social_liberal_score <= 3:
            context["social_liberal_position"] = "socially moderate"
        if social_liberal_score > 3:
            context["social_liberal_position"] = "socially progressive"

        return render(request, 'results.html', context)
