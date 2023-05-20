import pygame
import random

pygame.init()
sc = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class gameobject(pygame.sprite.Sprite):
	def __init__(self, img, x,y,shir,vis,napr):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load(img), (shir, vis))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.napr = "right"
	def ris(self):
		if self.napr == "right":
			sc.blit(self.image, (self.rect.x, self.rect.y))
		elif self.napr == "left":
			self.leftimage = pygame.transform.flip(self.image, True, False)
			sc.blit(self.leftimage, (self.rect.x, self.rect.y))
	def collidepoint(self, x, y):
		return self.rect.collidepoint(x, y)
	

xmouse, ymouse = pygame.mouse.get_pos()
xbg = 0
game_bg = gameobject("gamebg.png", -500, -400, 2048, 1152, "right")
arm = gameobject("arm.png", 400, 350, 400, 250, "right")
arms = gameobject("arms.png", 400, 350, 400, 250, "right")
arm_gold = gameobject("armgold.png", 400, 350, 400, 250, "right")
arms_gold = gameobject("armsgold.png", 400, 350, 400, 250, "right")
arm_second = gameobject("armsecond.png", 400, 350, 400, 250, "right")
arms_second = gameobject("armssecond.png", 400, 350, 400, 250, "right")
arm_knife = gameobject("armknife.png", 0, 0, 800, 600, "right")
arms_knife =  gameobject("armsknife.png", 0, 0, 800, 600, "right")
scope = gameobject("scope.png", xmouse-20, ymouse-20, 20, 20, "right")
light = gameobject("light.png", 0, 0, 800, 600, "right")
bar = gameobject("bar.png", 0, 0, 800, 600, "right")
ti = gameobject("t.png", 200, 200, 100, 260, "right")
cti = gameobject("ct.png", 200, 200, 100, 260, "right")

font = pygame.font.SysFont('arial', 36)

reloadtext = font.render("перезарядка...", False, (255,255,255))

#ammo = 30
ammoa = 30

ammok = "Bayonet"


ammos = 7
health = 100
kills = 0
skol = 0
delay = 0
perehod = 0
perehodschet = 0

#2048, 1152
arm_sost = arm
pygame.mouse.set_visible(False)
run = True
clock.tick(120)

t = []
ct = []

import time as tt
timmed = 'first'

curt =tt.time()
while run:
	gameobject.ris(game_bg)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEMOTION:
			#xmouse, ymouse = event.pos
			#if xmouse >=500:
				#game_bg.rect.x -=+
			#if xmouse <=300:
				#game_bg.rect.x +=2
			pass
		if event.type == pygame.MOUSEBUTTONDOWN:
			if perehod == 0:
				if arm_sost == arm:
					if ammoa > 0:
						for zlo in t:
							if zlo.collidepoint(xmouse, ymouse):
								t.remove(zlo)
						gameobject.ris(light)
						arm_sost = arms

				if arm_sost == arm_second:
					if ammos > 0:
						for zlo in t:
							if zlo.collidepoint(xmouse, ymouse):
								t.remove(zlo)
						gameobject.ris(light)
						arm_sost = arms_second

				if arm_sost == arm_knife:
					arm_sost = arms_knife

		if event.type == pygame.MOUSEBUTTONUP:
			pass
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				if arm_sost == arm:
					ammoa = -1
				if arm_sost == arm_second:
					ammos = -1
			if event.key == pygame.K_1:
				if arm_sost != arm:
					perehod = 1

			if event.key == pygame.K_2:
				#arm_sost = arm_second
				if arm_sost != arm_second:
					perehod = 2

			if event.key == pygame.K_3:
				#arm_sost = arm_second
				if arm_sost != arm_knife:
					perehod = 3

	nextt=tt.time()
	if timmed == 'first':
		timer = random.randint(1,3)
	if (nextt-curt)>timer:	
		curt =tt.time()
		timer = random.randint(1,3)
		timmed = '0'
		xt = random.randint(game_bg.rect.x,game_bg.rect.x+1948)
		yt = random.randint(300,400)
		terr = gameobject("t.png", xt, yt, 70, 175, "right")
		t.append(terr)
	for zlo in t:
		zlo.ris()
		#zlo.rect.x = game_bg.rect.x
	if perehod == 1:
		if arm_sost == arm_knife:
			arm_sost.rect.y += 100
		if arm_sost != arm_knife:
			arm_sost.rect.y += 50
		if arm_sost.rect.y >= 500:
			perehod = -1
			arm_sost.rect.y = 350
			arm_sost = arm
			ammo = ammoa
	if perehod == 2:
		if arm_sost == arm_knife:
			arm_sost.rect.y += 100
		if arm_sost != arm_knife:
			arm_sost.rect.y += 50
		if arm_sost.rect.y >= 500:
			perehod = -1
			arm_sost.rect.y = 350
			arm_sost = arm_second
			ammo = ammos
	if perehod == 3:
		arm_sost.rect.y += 50
		if arm_sost.rect.y >= 500:
			perehod = -1
			arm_sost.rect.y = 350
			arm_sost = arm_knife
			ammo = ammok
		#if arm_sost == arm_second:
		#	arm_second.rect.y += 50
		#	if arm_second.rect.y >= 500:
		#		perehod = -1
		#		arm_second.rect.y = 350
		#		arm_sost = arm
		#		ammo = ammoa

	if perehod == -1:
		if arm_sost == arm_second:
			if perehodschet == 0:
				arm_second.rect.y = 500
				perehodschet = 1
			arm_second.rect.y -= 50
			if arm_second.rect.y <= 350:
				perehod = 0
				perehodschet = 0
				arm_second.rect.y = 350
		if arm_sost == arm:
			if perehodschet == 0:
				arm.rect.y = 500
				perehodschet = 1
			arm.rect.y -= 50
			if arm.rect.y <= 350:
				perehod = 0
				perehodschet = 0
				arm.rect.y = 350
		if arm_sost == arm_knife:
			if perehodschet == 0:
				arm_knife.rect.y = 150
				perehodschet = 1
			arm_knife.rect.y -= 100
			if arm_knife.rect.y <= 0:
				perehod = 0
				perehodschet = 0
				arm_knife.rect.y = 0
	xmouse, ymouse = pygame.mouse.get_pos()
	if xmouse >=525:
		if game_bg.rect.x > -1248:
			game_bg.rect.x -=10
			for zlo in t:
				zlo.rect.x -=10
	if xmouse <=275:
		if game_bg.rect.x < 0:
			game_bg.rect.x +=10
			for zlo in t:
				zlo.rect.x +=10
	if arm_sost == arm:
		ammot = str(ammoa)
		ammot2 = ammot +" / 30"
	if arm_sost == arm_second:
		ammot = str(ammos)
		ammot2 = ammot +" / 7"
	if arm_sost == arm_knife:
		ammot = str(ammok)
		ammot2 = ammot
	killst = str(kills)
	scope.rect.x = xmouse - 10
	scope.rect.y = ymouse - 10
	gameobject.ris(arm_sost)
	gameobject.ris(scope)
	gameobject.ris(bar)
	ammotext = font.render(ammot2, False, (255,255,255))
	killstext = font.render(killst, False, (255,255,255))
	if arm_sost == arms:
		sc.blit(ammotext, (5,554))
		delay += 1
		if delay >= 3:
			delay = 0
			arm_sost = arm
			ammoa -=1
	if arm_sost == arms_second:
		sc.blit(ammotext, (5,554))
		delay += 1
		if delay >= 3:
			ammos -=1
			delay = 0
			arm_sost = arm_second
	if arm_sost == arms_knife:
		delay += 1
		if delay >= 3:
			delay = 0
			arm_sost = arm_knife
	if arm_sost == arm:
		if ammoa > -1:
			sc.blit(ammotext, (5,554))
		if ammoa <= -1:
			sc.blit(reloadtext, (5,554))
			ammoa -=1
			if ammoa == -30:
				ammoa = 30

	if arm_sost == arm_second:
		if ammos > -1:
			sc.blit(ammotext, (5,554))
		if ammos <= -1:
			sc.blit(reloadtext, (5,554))
			ammos -=1
			if ammos == -30:
				ammos = 7

	if arm_sost == arm_knife or arm_sost == arms_knife:
		sc.blit(ammotext, (5,554))

	sc.blit(killstext, (5,500))
	if perehod == 0:
		arms.rect.y = 350
		arms.rect.x = 400
		arms_second.rect.y = 350
		arms_second.rect.x = 400
		arms_knife.rect.y = 0
		arms_knife.rect.x = 0

	pygame.display.flip()

pygame.quit()