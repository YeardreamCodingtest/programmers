from operator import itemgetter
def solution(genres, plays):
    n = len(genres)
    song_dir = {}
    play_dir = {}

    for i in range(n):
        if genres[i] not in song_dir:
            play_dir[genres[i]] = plays[i]
            song_dir[genres[i]] = [(plays[i], i)]

        else:
            play_dir[genres[i]] += plays[i]
            song_dir[genres[i]].append((plays[i], i))
            song_dir[genres[i]].sort

    answer = []
    play_dir = sorted(play_dir.items(), key = lambda item: item[1], reverse = True)


    for play in play_dir:
        gen = play[0]
        song = sorted(song_dir[gen], key = itemgetter(0), reverse = True)
        count = 0
        for s in song:
            answer.append(s[1])
            if count == 1:
                break
            count += 1
    return answer