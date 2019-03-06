def attackDamage(defender, damage):
	defender.Hp -= damage

def checkWeakness(attacker, defender, damage):
	if (attacker.Pokemon_Type == defender.Weakness):
		damage *= 2
	return damage

def basicAttack(attacker, defender, damage):
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def whimsyTackle(attacker, defender, damage):
	x = randint(0,1) #coin flip
	damage = checkWeakness(attacker, defender, damage)
	if x == 1:
		attackDamage(defender, damage)
	else:
		print("tails, attack does no damage")

def amnesia(attacker, defender, damage, player, choice):
	damage = checkWeakness(attacker, defender, damage)
	if player == 'p':
		oppAttackNotAvail = choice
	else:
		playerAttackNotAvail = choice
	attackDamage(defender, damage)

def facade(attacker, defender, damage, player):
	if player == 'p':
		if playerBurned == True or playerPoisoned == True:
			damage += 80
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(attacker, defender, damage)

def recklessCharge(attacker, defender, damage):
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)
	attackDamage(attacker, 10)

def agility(attacker, defender, damage, player):
	if player == 'p':
		playerAgility = True
	else:
		oppAgility = True
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(attacker, damage)

def swallowDive(attacker, defender, damage, player):
	if player == 'p':
		if playerAgility == True:
			damage += 80
		playerAgility = False
	else:
		if oppAgility == True:
			damage += 80
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def coreBeam(attacker, defender, damage, player):
	damage = checkWeakness(attacker, defender, damage)
	for i in attacker.Energies:
		if i.Name == "Metal Energy":
			x = i
	if player == 'p':
		playerDiscard.append(attacker.Energies.pop(x))
	else:
		oppDiscard.append(attacker.Energies.pop(x))
	attackDamage(defender, damage)

def dustGathering(player):
	if player == 'p':
		playerDrawCard()
	else:
		oppDrawCard()

def teleport(pokemonIndex, player):
	switch(pokemonIndex, player)

def shiningArrow(attacker, defender, location):
	if location == 'active':
		damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def fangsOfTheSunne(attacker, defender, damage, player):
	if player == 'p':
		playerAttackNotAvail = 2
	else:
		oppAttackNotAvail = 2
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def dangerousBlow(attacker, defender, damage):
	if defender.Stage == 0:
		damage += 60
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def anchorShot(attacker, defender, damage, player):
	if player == 'p':
		oppCantRetreat = True
	else:
		playerCantRetreat = True
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def weatherTeller(attacker, player):
	if player == 'p':
		for i, e in reversed(list(enumerate(playerDeck))):
			if e.Card_Type == "Stadium":
				playerHand.append(playerDeck.pop(i))
	else:
		for i, e in reversed(list(enumerate(oppDeck))):
			if e.Card_Type == "Stadium":
				oppHand.append(oppDeck.pop(i))

def waterPulse(attacker, defender, damage, player):
	if player == 'p':
		oppAsleep = True
	else:
		playerAsleep = True
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def blownKiss(attacker, defender, damage):
	attackDamage(defender, damage)

def psybeam(attacker, defender, damage, player):
	if player == 'p':
		oppConfused = True
	else:
		playerConfused = True
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def flickeringFlames(attacker, defender, damage, player):
	if player == 'p':
		oppAsleep = True
	else:
		playerAsleep = True
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def shatterShot(attacker, defender, damage):
	energyCount = 0
	for i in attacker.Energies:
		if i.Name == 'Psychic Energy':
			energyCount += 1
	damage = damage * energyCount
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def wingsOfTheMoon(attacker, defender, damage, player):
	#####NEED TO MOVE ENERGIES#####
	if player == 'p':
		if len(playerBench) > 0:
			for i in reversed(list(enumerate(attacker.Energies))):
				playerBench[0].Energies.append(attacker.Energies.pop(i))
	else:
		if len(oppBench) > 0:
			for i in reversed(list(enumerate(attacker.Energies))):
				oppBench[0].Energies.append(attacker.Energies.pop(i))
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def supernaturalDance(attacker, defender, player):
	damageCounter = 0
	if player == 'p':
		for i in oppDiscard:
			if i.Card_Type == 'Pokemon':
				damageCounter += 1
	else:
		for i in playerDiscard:
			if i.Card_Type == 'Pokemon':
				damageCounter += 1
	damage = damageCounter * 10
	attackDamage(defender, damage)

def revelationDance(attacker, defender, damage):
	if len(stadium) > 0:
		damage = checkWeakness(attacker, defender, damage)
		attackDamage(defender, damage)

def venoshock(attacker, defender, damage, player):
	if player == 'p':
		if oppPoisoned == True:
			damage += 40
	else:
		if playerPoisoned == True:
			damage += 40
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def flamethrower(attacker, defender, damage, player):
	if player == 'p':
		playerDiscard.append(attacker.Energies.pop(0))
	damage = checkWeakness(attacker, defender, damage)
	attackDamage(defender, damage)

def filch(player):
	if player == 'p':
		playerDrawCard()
		playerDrawCard()
	else:
		oppDrawCard()
		oppDrawCard()

def copycat(attack, attacker, defender, damage, player, choice, pokemonIndex, location):
	if attack == whimseyTackle:
		whimsyTackle(attacker, defender, damage)
	if attack == amnesia:
		amnesia(attacker, defender, damage, player, choice)
	if attack == facade:
		facade(attacker, defender, damage, player)
	if attack == recklessCharge:
		recklessCharge(attacker, defender, damage)
	if attack == agility:
		agility(attacker, defender, damage, player)
	if attack == swallowDive:
		swallowDive(attacker, defender, damage, player)
	if attack == coreBeam:
		coreBeam(attacker, defender, damage, player)
	if attack == dustGathering:
		dustGathering(player)
	if attack == teleport:
		teleport(pokemonIndex, player)
	if attack == shiningArrow:
		shiningArrow(attacker, defender, location)
	if attack == fangsOfTheSunne:
		fangsOfTheSunne(attacker, defender, damage, player)
	if attack == dangerousBlow:
		dangerousBlow(attacker, defender, damage)
	if attack == anchorShot:
		anchorShot(attacker, defender, damage, player)
	if attack == weatherTeller:
		weatherTeller(attacker, player)
	if attack == waterPulse:
		waterPulse(attacker, defender, damage, player)
	if attack == blownKiss:
		blownKiss(attacker, defender, damage)
	if attack == psybeam:
		psybeam(attacker, defender, damage, player)
	if attack == flickeringFlames:
		flickeringFlames(attacker, defender, damage, player)
	if attack == shatterShot:
		shatterShot(attacker, defender, damage)
	if attack == wingsOfTheMoon:
		wingsOfTheMoon(attacker, defender, damage, player)
	if attack == supernaturalDance:
		supernaturalDance(attacker, defender, player)
	if attack == revelationDance:
		revelationDance(attacker, defender, damage)
	if attack == venoshock:
		venoshock(attacker, defender, damage, player)
	if attack == flamethrower:
		flamethrower(attacker, defender, damage, player)
	if attack == filch:
		filch(player)
	if attack == copycat:
		pass
	else:
		basicAttack(defender, damage)
