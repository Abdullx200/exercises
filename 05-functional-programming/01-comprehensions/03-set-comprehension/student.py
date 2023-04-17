def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs, ys):
    return {sim 
                for sim in xs 
                    if sim in ys
            }