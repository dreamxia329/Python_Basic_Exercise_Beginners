from Students import Students, ForeignStudent

s3 = ForeignStudent('Tommy', 'Chinese', 88)
print(s3.fetch_students_info())
s3.NationalDetails.describe_national_details()
s3.NationalDetails.get_scholarship()
