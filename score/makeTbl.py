from .models import TblScore, TblMember, TblRank, TblDaily
import logging
import time

"""
2019-04-25 08:14:04,143 DEBUG <QuerySet [{'playerID': 6}, {'playerID': 10}, {'playerID': 13}, {'playerID': 17}, {'playerID': 18}, {'playerID': 22}, {'playerID': 29}, {'playerID': 32}, {'playerID': 34}, {'playerID': 39}, {'playerID': 40}, {'playerID': 49}, {'playerID': 50}, {'playerID': 53}, {'playerID': 55}, {'playerID': 66}, {'playerID': 72}, {'playerID': 73}, {'playerID': 76}, {'playerID': 77}, '...(remaining elements truncated)...']>
2
"""
class ManageRank():
	def getTbl(start_date, end_date):

		tScore = TblScore.objects.filter(date__range=(start_date, end_date))
		tScore = tScore.order_by("playerID")

		tMember = TblMember.objects.filter()

		unq_playerId = tScore.values("playerID").order_by("playerID").distinct()
	#	logging.debug(unq_playerId[0]["playerID"])

		TblRank.objects.all().delete()

		for player in unq_playerId:
			tRank = TblRank()
			# データ初期化
			gameNum = 0
			gamePt = 0
			winNum = 0
			for scr in tScore:
				if player["playerID"] == scr.playerID:
					gameNum += 1
					gamePt += scr.gamePt
					if scr.gamePt == 5:
						winNum += 1
			# 結果を格納
			tRank.gameNum	 = gameNum
			tRank.gamePt      = gamePt
			tRank.gross       = gamePt/gameNum
			tRank.HDCP        = 0
			tRank.playerID    = player['playerID']
			tRank.name        = get_nameFromId(tRank.playerID, tMember)
			tRank.net         = tRank.gross + tRank.HDCP
			tRank.winNum      = winNum
			tRank.save()

			logging.debug("tRank.name:" + str(tRank.name))
			
		return TblRank.objects.all()


def get_nameFromId(playerID, tMember):
	for mem in tMember:
		if playerID == mem.playerID:
			ret = mem.name
	if ret == None:
		logging.debug("◆◆get_nameFromId()  NG")

	return ret




