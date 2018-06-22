def letter_grade(score):
    if score >= 90:
        print "A"
    else:
        if score >= 80:
            print "B"
        else:
            if score >= 70:
                print "C"
            else:
                if score <= 60:
                    print "F"
letter_grade(74)