def calculate_total_avg(eng, c_lang, py):
    total = eng + c_lang + py
    average = round(total / 3, 2)
    return total, average

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"