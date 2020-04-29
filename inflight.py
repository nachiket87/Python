flight_lengths = 120
movie_lengths = [20, 20, 70, 12, 100, 90, 40, 81, 39]


def fl(flight_lengths, movie_lengths):
    for i in range(0, len(movie_lengths)-1):
        for j in (i+1, len(movie_lengths)-1):
            if movie_lengths[i] + movie_lengths[j] == flight_lengths:
                return "movie: " + str(i+1) + ' ' + "movie: " + str(j+1)
    else:
        return "Can't watch two movies"

print(fl(flight_lengths, movie_lengths))