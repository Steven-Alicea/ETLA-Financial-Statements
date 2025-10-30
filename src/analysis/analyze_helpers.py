def print_analysis(df, title):
    print(title)
    print(df)

# create function to check the input format for dates 
#(yyyy-mm-dd | mm/dd/yyyy | jan dd, yyyy | jan d, yyyy | january dd, yyyy | january d, yyyy)
def rename_title_for_dates(title, start_date, end_date):
    if start_date and end_date:
        title = title + f" Between {start_date} and {end_date}"
    elif start_date and not end_date:
        title = title +  f" After {start_date}"
    elif not start_date and end_date:
        title = title + f" Before {end_date}"
    return title
