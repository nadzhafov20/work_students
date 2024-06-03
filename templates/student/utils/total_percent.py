

def calculate_total_percent(student):
    total_percent = 0
    total_percent += 20 if student.qualification else 0
    total_percent += 20 if student.price_hour else 0
    total_percent += 10 if student.image else 0
    total_percent += 20 if student.about else 0
    total_percent += 30 if student.address else 0
    return total_percent