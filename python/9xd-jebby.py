import random
9xd_members = [
"	강길전	",
"	강석진	",
"	강은주	",
"	고상우	",
"	고효준	",
"	고희원	",
"	국윤수	",
"	김관호	",
"	김남호	",
"	김도훈	",
"	김영경	",
"	김우현	",
"	김은지	",
"	김택근	",
"	라태웅	",
"	박명호	",
"	박성훈	",
"	박세현	",
"	박수영	",
"	박영석	",
"	박유진	",
"	박지은	",
"	박찬민	",
"	박총명	",
"	박현식	",
"	박혜정	",
"	박희정	",
"	배상현	",
"	변동삼	",
"	서동현	",
"	양현찬	",
"	양홍일	",
"	오상택	",
"	오승현	",
"	유형주	",
"	윤건영	",
"	이강산	",
"	이건희	",
"	이규진	",
"	이동건	",
"	이병주	",
"	이성우	",
"	이원준	",
"	이주원	",
"	이혜정	",
"	이혜정	",
"	이희진	",
"	임규산	",
"	임원균	",
"	임준혁	",
"	장기효	",
"	장호동	",
"	장효원	",
"	정동아	",
"	정소희	",
"	정재훈	",
"	정지윤	",
"	정현지	",
"	정희영	",
"	조대연	",
"	조승완	",
"	진유림	",
"	차강혁	",
"	천상원	",
"	최가람	",
"	최병훈	",
"	최봉재	",
"	최정연	",
"	최현묵	",
"	추은선	",
"	하동현	",
"	하조은	",
"	하태지	",
"	한웅제	",
"	홍은진	",
"	Hanur Lee	",
"	Hyesu Bae	",
"	Jinho Jung	",
"	xodla	"
]

for i in range(0, 20):
	member_count = len(9xd_members)
	idx = random.randInt(member_count)
	print(9xd_members.pop(idx))