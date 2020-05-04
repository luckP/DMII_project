import pandas as pd
import numpy as np
import pathlib, html


def str_to_int(x):
    try:
        return int(x)
    except:
        return np.NaN


def main():
    
    dest_dir = pathlib.Path(__file__).resolve().parent.parent / 'data'
    print('Outputting files to', dest_dir)
    
    # the movies file
    df = pd.read_csv('movie-names.txt', sep='\t', encoding='latin1')

    # transform html characters into normal ones
    df['moviename'] = df['moviename'].apply(lambda x : html.unescape(x)) 
    
    df.to_csv(dest_dir / 'movie.csv', index=False)
    print(dest_dir / 'movie.csv')

    
    # the ratings file, turn to UTF-8
    df = pd.read_csv('Ratings.timed.txt', sep='\t',  encoding = 'UTF-16')
    df.to_csv(dest_dir / 'ratings.csv', index=False)
    print(dest_dir / 'ratings.csv')

    # the profiles file
    df = pd.read_csv('profile.txt')

    # some rows have text instead of numbers
    df['age'] = df['age'].apply(lambda x : str_to_int(x))
    df['profileview'] = df['profileview'].apply(lambda x : str_to_int(x))
    
    df.to_csv(dest_dir / 'profile.csv', index=False)
    print(dest_dir / 'profile.csv')

    print('Done')

    
if __name__ == '__main__':
    main()
