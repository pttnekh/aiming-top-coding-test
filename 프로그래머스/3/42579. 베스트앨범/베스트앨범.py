def solution(genres, plays):
    
    # 장르별 딕셔너리 만들어서 내부에 튜플(재생수, 인덱스) 넣기
    dict_by_genre = {}
    for index, play in enumerate(plays):
        g = genres[index]
        if g not in dict_by_genre:
            dict_by_genre[g] = []
        dict_by_genre[g].append((play, index))

    # 재생수 합계 구하기
    genre_total = {}
    for genre, songs in dict_by_genre.items(): # songs는 [(500, 0), (150, 2), (800, 4)] 같은 리스트
        genre_total[genre] = sum(play for play, index in songs)
        songs.sort(key=lambda x: (-x[0], x[1])) # 재생 수 내림차순, 인덱스 오름차순
    
    sorted_genres = sorted(genre_total.keys(), key=lambda g: -genre_total[g])


    answer = []
    
    for g in sorted_genres:
        for play, index in dict_by_genre[g][:2]:
            answer.append(index)

    return answer