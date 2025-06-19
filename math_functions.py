#ספרייה של פונקציות אלגריתמיות
#נוצר על ידי תלמיד א' וב'


def wlcome():
     # ונקציה לברכה
    print("ברוכים הבאים לספרייה של פונקציות אלורתמיות")

def is_prime(target):
    if target<2:
        return False
    for i in range(2,int(target/2)+1):
        if (target%i)==0:
            return False
    return True


if __name__=="__main__":
    wlcome()
    print(is_prime((15)))
