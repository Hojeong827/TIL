# Section 14 마크다운 정리

## Exercise 1-76: Sorting
* [exercise1-76](https://github.com/Hojeong827/TIL/blob/main/Python/basic/code/exercise1-76.py)  
    지금까지 배운 반복문과 조건문을 이용하여서 Sorting(정렬) 을 하는 코드 구현
    <pre><code>
    scores = [40, 20, 30, 10, 50]
    sorted_scores = list()
    for _ in range(len(scores)):                # 궁금했던 점이 scores가 temp_scores로 복사되면서 원소의 갯수가
                                                  점점 내려가기 때문에 range안의 값이 바뀔 가능성이 있었는데 
                                                  따로 값을 출력해본 결과 영향을 받지 않는다는 것을 발견
                                                  (=> _ 대신 i 로 설정하고 출력한 결과 0~4까지 출력됨)
                                                  즉 for 문의 조건문에서는 영향을 받지 않지만 반복문 안에서의 
                                                  변수는 영향을 받는다가 결론
        M, M_idx = scores[0], 0
        for score_idx in range(len(scores)):    # scores 안에서 최댓값과 최댓값의 index값 구하기
            if scores[score_idx]>M:
                M=scores[score_idx]
                M_idx=score_idx
    
        temp_scores=list()
        for score_idx in range(len(scores)):
            if score_idx == M_idx:              # 최대값은 sorted에 저장
                sorted_scores.append(scores[score_idx])
            else:                               # 나머지는 임시 공간에 저장
                temp_scores.append(scores[score_idx])
        scores=temp_scores                      # 원래의 socres배열을 임시 공간에 저장된 값으로 복사
        print("reamining scores: ", scores)
        print("sorted scores: ", sorted_scores, '\n')
    </code></pre>