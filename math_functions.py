#ספרייה של פונקציות אלגריתמיות
#נוצר על ידי תלמיד א' וב'


def wlcome():
    # ונקציה לברכה
    print("ברוכים הבאים לספרייה של פונקציות אלורתמיות")

def factorial(n):
    """מחזירה את הפקטוריאל של מספר שלם n"""
    if n < 0:
        raise ValueError("לא ניתן לחשב פקטוריאל למספר שלילי")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)    



if __name__=="__main__":
    wlcome()
    print(factorial(5))  # פלט צפוי: 120