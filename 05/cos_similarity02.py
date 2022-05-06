import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("./movies_metadata.csv", low_memory=False)       # 데이터 파일 접근

pd.set_option("display.max_rows", None)                             # 판다스 출력 옵션 지정
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 10)

data = data.head(20000)                                             # 데이터 상위 20000개 추출
data["overview"] = data["overview"].fillna("")                      # NULL -> 빈값 대체

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(data["overview"])                # TF-IDF 행렬

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)          # 상호 간 코사인 유사도
print('코사인 유사도 연산 결과 :', cosine_sim.shape)

title_to_index = dict(zip(data["title"], data.index))               # {타이틀:인덱스} 딕셔너리 생성성

#영화 제목 Father of the Bride Part II의 인덱스를 리턴
#idx = title_to_index['Father of the Bride Part II']
#print(idx)


def get_recommendations(title, cosine_sim=cosine_sim):              # 영화제목 파라미터와 제일 유사한 10개의 영화 추출 함수
    # 선택한 영화의 타이틀로부터 해당 영화의 인덱스를 받아온다.
    idx = title_to_index[title]

    # 해당 영화와 모든 영화와의 유사도를 가져온다.
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 영화들을 정렬한다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 10개의 영화를 받아온다.
    sim_scores = sim_scores[1:11]

    # 가장 유사한 10개의 영화의 인덱스를 얻는다.
    movie_indices = [idx[0] for idx in sim_scores]

    # 가장 유사한 10개의 영화의 제목을 리턴한다.
    return data["title"].iloc[movie_indices]


print(get_recommendations("The Dark Knight Rises"))
