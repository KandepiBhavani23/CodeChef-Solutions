# https://www.codechef.com/problems/SONGS
for _ in range(int(input())):
    train_journey_time, song_duration = map(int, input().split())
    song_play_time = train_journey_time // (song_duration * 3 )
    print(song_play_time)
