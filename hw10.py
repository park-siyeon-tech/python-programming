import os
import pickle

FILE_NAME = "score.bin"

def input_scores():
    scores = []
    count = 1
    while True:
        score = int(input(f"#{count}? "))
        if score < 0:
            break
        scores.append({"student": count, "score": score})
        count += 1
    return scores

def get_average(score_list):
    if len(score_list) == 0:
        return 0
    total = sum(item["score"] for item in score_list)
    return total / len(score_list)

def show_scores(score_list):
    print("개인점수:", end=" ")
    for item in score_list:
        print(item["score"], end=" ")
    print()

def save_scores(score_list):
    with open(FILE_NAME, "wb") as f:
        pickle.dump(score_list, f)

def load_scores():
    with open(FILE_NAME, "rb") as f:
        return pickle.load(f)


if os.path.exists(FILE_NAME):
    print("[파일 읽기]")
    scores = load_scores()
else:
    print("[점수 입력]")
    scores = input_scores()
    save_scores(scores)

print("[점수 출력]")
show_scores(scores)
average = get_average(scores)
print(f"평균: {average:.1f}")
