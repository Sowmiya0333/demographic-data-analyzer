import pandas as pd

def demographic_data_analyzer():
    # Load dataset
    df = pd.read_csv("data.csv")

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Percentage with advanced education (>50K earnings)
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[advanced_education & (df['salary'] == '>50K')].shape[0] / df[advanced_education].shape[0]) * 100, 1)
    
    # 5. Percentage without advanced education (>50K earnings)
    lower_education_rich = round((df[~advanced_education & (df['salary'] == '>50K')].shape[0] / df[~advanced_education].shape[0]) * 100, 1)

    # 6. Minimum hours per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of min hour workers earning >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # 8. Country with highest percentage of >50K earners
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    highest_earning_country = (country_earnings / country_counts * 100).idxmax()
    highest_earning_country_percentage = round((country_earnings / country_counts * 100).max(), 1)

    # 9. Most popular occupation for >50K earners in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
