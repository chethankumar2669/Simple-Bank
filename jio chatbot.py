import wikipedia as wiki
def ai(quirey):
	x=wiki.summary(quirey,sentences=1)
	return(x)
while True:
	data=input("Ask jio for anything:-")
	printf(ai(data))	