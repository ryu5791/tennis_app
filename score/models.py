from django.db import models

# Create your models here.
class TblManage(models.Model):
	tblID			= models.IntegerField()
	thresholdPtn    = models.CharField(default="", blank=True, max_length=50)
	dispTblName     = models.CharField(default="", blank=True, max_length=50)
	startPeriod     = models.DateField(null=True)
	endPeriod       = models.DateField(null=True)
	hideLastMonth   = models.BooleanField(default=False)
	rvNum           = models.IntegerField()
	chNum           = models.IntegerField()
	event1name      = models.CharField(default="", blank=True, max_length=50)
	event2name      = models.CharField(default="", blank=True, max_length=50)
	event3name      = models.CharField(default="", blank=True, max_length=50)
	event4name      = models.CharField(default="", blank=True, max_length=50)
	event5name      = models.CharField(default="", blank=True, max_length=50)
	event6name      = models.CharField(default="", blank=True, max_length=50)
	event7name      = models.CharField(default="", blank=True, max_length=50)
	event8name      = models.CharField(default="", blank=True, max_length=50)
	comment         = models.CharField(default="", blank=True, max_length=50)

class TblDaily(models.Model):
	tblID		= models.PositiveIntegerField()
	date        = models.DateField(null=True)
	totalGame   = models.PositiveIntegerField()
	playerNum   = models.PositiveIntegerField()

class TblMember(models.Model):
	playerID	= models.PositiveIntegerField()
	name        = models.CharField(default="", blank=True, max_length=20)
	dispName    = models.CharField(default="", blank=True, max_length=20)
	inputName1  = models.CharField(default="", blank=True, max_length=20)
	inputName2  = models.CharField(default="", blank=True, max_length=20)

class TblScore(models.Model):
	date        = models.DateField(null=True)
	gameNo      = models.PositiveIntegerField(null=True)
	gamePt      = models.PositiveIntegerField(default=0, null=True, blank=True)
	playerID    = models.PositiveIntegerField(null=True)
	pairID      = models.PositiveIntegerField(null=True)
	row         = models.PositiveIntegerField(default=0, null=True)
#	serve1st    = models.BooleanField(default=False, null=True)
#	serve2nd    = models.NullBooleanField(null=True)
	serve1st    = models.PositiveIntegerField(null=True)
	serve2nd    = models.PositiveIntegerField(null=True)
	serveTurn   = models.PositiveIntegerField(default=0, null=True)
	temp        = models.BooleanField(default=False, null=True)

class TblRank(models.Model):
	gameNum		= models.PositiveIntegerField()
	gamePt      = models.FloatField()
	gross       = models.FloatField()
	HDCP        = models.FloatField()
	playerID    = models.PositiveIntegerField()
	net         = models.FloatField()
	winNum      = models.PositiveIntegerField()
	name        = models.CharField(default="", blank=True, max_length=20)

class TblPeriodData(models.Model):
	tblID		= models.ForeignKey(TblManage, on_delete=models.CASCADE)
	playerID    = models.ForeignKey(TblMember, on_delete=models.PROTECT)
	HDCP        = models.FloatField(null=True)
	event1      = models.IntegerField(null=True)
	event2      = models.IntegerField(null=True)
	event3      = models.IntegerField(null=True)
	event4      = models.IntegerField(null=True)
	event5      = models.IntegerField(null=True)
	event6      = models.IntegerField(null=True)
	event7      = models.IntegerField(null=True)
	event8      = models.IntegerField(null=True)
	adjustDate  = models.IntegerField(null=True)


