from django.shortcuts import render
from django.http import HttpResponse
from .utils import *
import requests
from sklearn.preprocessing import normalize
import numpy as np
import pandas as pd
from kiwipiepy import Kiwi
# Create your views here.


def summarize_view(request):
    if request.method == 'POST':
        user_text = request.POST.get('user_text', '요약문이 제대로 전달되지 않은것 같아요!!')  # 템플릿에서 사용자가 입력한 텍스트를 가져옵니다.
        number = int(request.POST.get('sentence_number', 5))  # 사용자가 선택한 숫자를 가져옵니다. 기본값은 3
        if not user_text:
            return render(request, 'mainPage/result.html', {'summarized_result': "요약문을 보시려면 문장을 추가해주세요"})
        summarized_result = summarizeText(user_text, number)  # 가져온 텍스트를 요약 함수에 전달하여 요약 결과를 얻습니다.
        return render(request, 'mainPage/result.html', {'summarized_result': summarized_result})
        # 결과를 result.html 템플릿에 전달하여 보여줍니다.
    return render(request, 'mainPage/index.html')  # GET 요청 시에는 입력 폼을 보여줍니다.