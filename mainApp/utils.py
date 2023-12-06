from sklearn.preprocessing import normalize
import numpy as np
import pandas as pd
from kiwipiepy import Kiwi
import math
import re

def get_nouns(text, kiwi = Kiwi()):
    results = []
    result = kiwi.analyze(text)
    for token, pos, _, _ in result[0][0]:
        if len(token) != 1 and pos.startswith('NN'):
            results.append(token)
    return results

def textrank(x, df=0.85, max_iter=50): # df = Dumping Factor : 0.85라고 가정, max_iter = 최대 반복횟수, 제한 조건을 두고 적절한 값에 수렴할떄까지 반복해야 하나 임의적으로 50회라고 지정
    assert 0 < df < 1

    # initialize
    A = normalize(x, axis=0, norm='l1')
    R = np.ones(A.shape[0]).reshape(-1, 1)
    bias = (1 - df) * np.ones(A.shape[0]).reshape(-1, 1)
    # iteration
    for _ in range(max_iter):
        R = df * (A * R) + bias

    return R


def summarizeText(content, number):
    content = content.replace('\r', '')
    content = re.split(r'[\n]+', content)
    # content = [item for item in content if item != '']
    data = []
    for text in content:
        if (text == " " or len(text) == 0):
            continue
        temp_dict = dict()
        temp_dict['sentence'] = text
        temp_dict['token_list'] = get_nouns(text)  # kiwi 형태소 분석으로 구분
        data.append(temp_dict)

    data_frame = pd.DataFrame(data)  # DataFrame에 넣어 깔끔하게 보기
    similarity_matrix = []
    for i, row_i in data_frame.iterrows():
        i_row_vec = []
        for j, row_j in data_frame.iterrows():
            if i == j:
                i_row_vec.append(0.0)
            else:
                intersection = len(set(row_i['token_list']) & set(row_j['token_list'])) # 유사도 계산의 분자 부분
                if len(set(row_i['token_list'])) > 0:
                    log_i = math.log(len(set(row_i['token_list']))) if len(set(row_i['token_list'])) > 0 else 1
                    log_j = math.log(len(set(row_j['token_list']))) if len(set(row_j['token_list'])) > 0 else 1
                    similarity = intersection / (1 + log_i + log_j)
                    i_row_vec.append(similarity)

        similarity_matrix.append(i_row_vec)

        weightedGraph = np.array(similarity_matrix)

    R = textrank(weightedGraph)

    R = R.sum(axis=1)
    indexs = R.argsort()[-number:] # 랭크값 상위 n 문장의 인덱스를 가져옴

    summarized_sentences = """ """
    for index in sorted(indexs): # 출력 구조의 순서를 유지하기 위해 정렬함
        summarized_sentences += data_frame['sentence'][index] + "\n"

    return summarized_sentences
