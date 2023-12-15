import pandas as pd

data = {'Title': ['Marybeth', 'Matrix', 'Star Wars', 'Inception', 'Jurassic Park'],
        'Year': [1978, 1999, 1977, 2010, 1993]}
df = pd.DataFrame(data)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


df['Vowels'] = df['Title'].apply(count_vowels)

print(df)
