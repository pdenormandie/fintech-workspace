student_loan_information_aj = {
    "student_name": "Amy Johnson",
    "university": "Yale",
    "academic_year": "2015_2016",
    "loan_amount": 45000,
    "duration_years": 10,
    "payments_started": False,
}

print("The original student loan profile", student_loan_information_aj)


student_loan_information_aj["student_name"] = "Amy Johnston"
print("The amended student loan profile:", student_loan_information_aj)
