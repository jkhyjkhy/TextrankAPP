from django.test import TestCase
import re
# Create your tests here.

text = """맨체스터 시티와 경기에서 가장 부진한 두 선수가 서로 칭찬을 주고받았다.
토트넘 홋스퍼는 4일 오전 1시 30분(한국시간) 영국 맨체스터의 에티하드 스타디움에서 열린 2023-2024시즌 프리미어리그 14라운드 경기에서 맨체스터 시티와 3-3으로 비겼다.
토트넘은 2004년 이후 처음으로 리그 4연패에 빠질 뻔했던 위기를 벗어났다. 
토트넘은 지난 2004년 11월 데이비드 플리트 감독 시절 이후 단 한 번도 리그 4연패를 기록한 적 없다. 
이번엔 첼시와 울버햄튼, 아스톤 빌라에 차례로 패한 뒤 맨시티한테도 무릎 꿇을 위기였지만, 데얀 쿨루셉스키의 극적인 동점골로 기사회생했다.
치열하고 팽팽했던 난타전이었다. 양 팀은 모두 합해 슈팅 26개, 총 6골이 터진 정신 없는 경기를 치렀다.
토트넘은 전반 내내 맨시티의 강력한 전방 압박에 고전했지만, 후반 들어 기세를 올리며 승점 1점을 따냈다.
 맨시티의 슈팅이 두 차례나 골대를 때리는 행운도 따랐다.
경기의 주인공은 손흥민이었다. 전반 6분 손흥민은 선제골을 터뜨렸다. 코너킥 수비 이후 쿨루셉스키가 전방으로 길게 패스했다. 
빈 공간으로 쇄도하던 손흥민은 제레미 도쿠와 몸싸움을 이겨냈고 질주를 이어갔다. 
박스 오른쪽으로 파고든 그는 날카로운 슈팅으로 에데르송 골키퍼를 뚫어냈다.
'맨시티 킬러'다운 활약이다. 손흥민은 이날 전까지 맨시티를 상대로 만난 17경기에서 7골 3도움을 터트렸다. 그는 여기에 한 골을 더 추가하며 맨시티 상대 8골을 기록하게 됐다.
손흥민의 리그 9호 골이자 지난 10월 말 크리스탈 팰리스전 결승골 이후 4경기 만의 득점포다. 
그는 이번 득점으로 득점 2위 모하메드 살라(10골)를 바짝 추격했다. 동시에 PL 통산 112골을 만들며 사디오 마네, 디온 더블린을 제치고 프리미어리그 역사상 최다 득점 단독 24위에 이름을 올렸다.
경기 종료 후 이 경기에서 중앙 수비수로 선발 출전, 풀타임을 소화한 에메르송 로얄은 자신의 개인 소셜 미디어에 "좋은 경기였어 친구들.. 계속 가보자고"라는 글을 남겼다.
그러자 측면 미드필더로 출전해 전반전만 소화한 브리안 힐이 댓글을 달았다. 그는 "최고야"라는 댓글을 남겼다. 이에 에메르송은 다시 "역시 크랙"이라며 힐을 칭찬했다.
좋은 팀 분위기를 알리는 소셜 미디어 게시물이었지만, 두 선수는 맨시티전 딱히 좋은 활약을 펼치지 못했기에 '웃긴 상황'이라는 반응이 주를 이룬다.
실제로 영국 '풋볼 런던'이 경기 종료 후 매긴 토트넘 선수들의 평점에서 에메르송은 4점을, 힐은 5점을 부여받았다. 
매체는 "에메르송은 경기 시작 12분 만에 엉망이 됐다. 공을 잃은 뒤 엘링 홀란에게 기회를 헌납했다.
다행히 홀란은 득점 상황에서 실수했다. 전반전에만해도 엉성한 모습이 몇 번은 더 나왔다"라며 혹평했다.
또한 힐은 이례적으로 주장 손흥민의 분노를 끌어내기도 했다.
 양 팀이 1-1로 팽팽히 맞서던 전반 27분 문제의 장면이 나왔다. 측면 공격수로 선발 출전한 힐이 맨시티 진영에서 로드리의 패스 실수를 끊어냈다. 
중앙으로 뛰어드는 손흥민에게 패스했다면 바로 골키퍼와 맞닥뜨리는 결정적 기회가 될 수 있는 상황.
힐도 손흥민 쪽을 힐끔 봤지만, 곧바로 패스하지 않고 직접 공을 몰고 올라갔다. 
그리고 뒤늦게 손흥민에게 패스했다. 공은 당연히 커버를 들어온 맨시티 수비진에 차단당했다. 그렇게 절호의 기회가 달아났다.
그러자 손흥민은 힐을 바라보고, 오른팔을 크게 휘두르며 이례적으로 화를 냈다.
왜 자신에게 일찍 패스하지 않았냐며 답답함을 감추지 못하는 모습이었다. 머리를 감싸 쥐었던 힐은 양팔을 들어 올리며 항변했다.
한편 토트넘은 일단 3연패 수렁에서 벗어났다. 
이 경기 승점 1점을 챙긴 토트넘은 승점 27점(8승 3무 3패)을 만들며 5위에 자리했다. 
3경기 연속 무승부를 거둔 맨시티는 30점(9승 3무 2패)으로 3위로 내려앉았다. 선두 아스날(승점 33)과 격차는 3점으로 벌어졌다."""

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


def summarizeText(content):
    content = content.replace('\r', '')
    # content = re.split(r'[\n]+', content)
    content = re.split(r'\.\s*', content)
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
    print(R.shape)
    indexs = R.argsort()[-8:] # 랭크값 상위 여덟 문장의 인덱스를 가져옴

    summarized_sentences = """ """
    for index in sorted(indexs): # 출력 구조의 순서를 유지하기 위해 정렬함
        summarized_sentences += data_frame['sentence'][index] + "\n"

    return summarized_sentences

print(summarizeText(text))