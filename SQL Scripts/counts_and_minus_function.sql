# Total Count for each provider
Select Count(*) As netflix_count # 8785
From netflix;

Select Count(*) As disney_count	# 1448
From disney;

Select Count(*) As hulu_count	# 2594
From hulu;

Select Count(*) As prime_count	# 9615
From prime;

Select Count(*) As total	# 22,442
From streaming;

# Total Rows = 21,791

# Finding the movies that match
Select Count(d.title) as Same	# 45
From disney d
Join streaming s ON d.title = s.title;

Select Count(d.title) as different	# 1403
From disney d
LEFT JOIN streaming s ON d.title = s.title
Where s.title IS NULL;