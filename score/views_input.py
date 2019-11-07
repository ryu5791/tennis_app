from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import TblScore, TblMember

from logging import getLogger		#getLogger("" + str())

import logging
import json
import io
import csv

@login_required(login_url='/admin/login/')
def inputScr(request):
	logging.basicConfig(level=logging.DEBUG)
	test = User.objects.filter(username=request.user)
	logging.debug("index user:" + str(request.user))
	getLogger("index user:" + str(request.user))
	getLogger("index is_super:" + str(request.user.is_superuser))
	getLogger("index test:" + str(test))
	getLogger("index has_perm:" + str(request.user.has_perm("score.add_tblscore") ))
#	getLogger("index has_perm:" + str(request.user.has_perm("auth.add_user") ))
	params = {'authInput': request.user.has_perm("score.add_tblscore"),}
	return render(request, "score/input_input.html", params)

"""------------------------------------------------------
ファイル変更
	csvファイルを出力

Args:
	request

Returns:
	render
------------------------------------------------------"""
@login_required(login_url='/admin/login/')
def changeScr(request):
	params ={	'authInput': request.user.has_perm("score.add_tblscore"),}
	return render(request, "score/input_change.html", params)


"""------------------------------------------------------
ファイルインポート
	とりあえずjsonのみ対応。（いずれはcsvも）

Args:
	request

Returns:
	render
------------------------------------------------------"""
@login_required(login_url='/admin/login/')
def importScr(request):

	getLogger("importScr request.method:" + str(request.method))
	
	msg_result = "test"

	try:

		#ファイル読み込み
		if request.method == "POST":
			# json
			if "json" in request.FILES["json"].name:
				if "Score"	in request.FILES["json"].name:
					getLogger("importScr Score TRUE")

					# スコア → データベース
					temp = io.TextIOWrapper(request.FILES["json"].file ,encoding="utf-8_sig")
					json_score = json.load(temp)

					roopCount=0					#デバッグ用

					for scr in json_score["results"]:
						tblScore, created = TblScore.objects.get_or_create(date=str(scr["date"].replace('/', '-')) \
															,  gameNo=str(scr["gameNo"]) \
															,  playerID=int(scr["ID"]))
						tblScore.date = scr["date"].replace('/', '-')
						tblScore.gameNo		= int(scr["gameNo"])
						tblScore.gamePt		= int(scr["gamePt"])
						tblScore.playerID	= int(scr["ID"])
						tblScore.pairID		= int(scr["pairID"])
						tblScore.row		= int(scr["row"])
						tblScore.serve1st	= int(scr["serve1st"])
						if scr["serve2nd"] is not None:
							tblScore.serve2nd	= int(scr["serve2nd"])
						tblScore.serveTurn	= int(scr["serveTurn"]-1)
						# 保存！
						tblScore.save()

						roopCount = roopCount + 1												#デバッグ用
						getLogger("importScr roopCount:" + str(roopCount) + str(created))	#デバッグ用

					msg_result = "score読み込み完了"
					
				elif "member"  in request.FILES["json"].name:
					temp = io.TextIOWrapper(request.FILES["json"].file ,encoding="utf-8_sig")
					json_member = json.load(temp)

					roopCount=0					#デバッグ用

					# メンバー → データベース登録
					for mem in json_member["results"]:
						tblMember, created = TblMember.objects.get_or_create(playerID=int(mem["ID"]))
						tblMember.playerID		= int(mem["ID"])
						tblMember.name			= mem["name"]
						tblMember.dispName		= mem["dispName"]
						tblMember.inputName1	= mem["nickname1"]
						tblMember.inputName2	= mem["dispName"]
						# 保存！
						tblMember.save()

						roopCount = roopCount + 1									#デバッグ用
						getLogger("importScr roopCount:" + str(roopCount) )		#デバッグ用

					msg_result = "member読み込み完了"
	except:
		msg_result = "読み込み失敗"

	
	params ={	'authInput': request.user.has_perm("score.add_tblscore"),
				'throw_result' : msg_result}
	return render(request, "score/input_import.html", params)

"""------------------------------------------------------
ファイルエクスポート
	csvファイルを出力

Args:
	request

Returns:
	render
------------------------------------------------------"""
@login_required(login_url='/admin/login/')
def exportScr(request):

	if request.method == "POST":
		if "button_export" in request.POST:
			# CSVファイル出力
			with open('score.csv',mode='a',encoding='utf-8', newline='') as f:
				writer = csv.writer(f)
				for dt in TblScore.objects.all():
					writer.writerow(	[ \
										str(dt.date).replace('-','/')	,\
										dt.gameNo						,\
										dt.playerID						,\
										dt.pairID						,\
										dt.serve1st						,\
										dt.serve2nd						,\
										dt.gamePt						,\
										])

	params ={	'authInput': request.user.has_perm("score.add_tblscore"),}
	return render(request, "score/input_export.html", params)




