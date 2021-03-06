import math

DEFAULT_TIME_INCREMENT = 0.1

class SimpleStrategy():
	""" moves fired missile without taking gravity into account """

	def move(self, missile):
		missile.time += DEFAULT_TIME_INCREMENT

		missile.x += (missile.fire_power) * math.cos(missile.angle)
		missile.y -= (missile.fire_power) * math.sin(missile.angle)

		#missile.x =  missile.fired_pos.x + 20*missile.fire_power * missile.time * math.cos(missile.angle)
		#missile.y =	 missile.fired_pos.y - 20*missile.fire_power * missile.time * math.sin(missile.angle)

class SmartStrategy():
	""" moves fired missile with taking gravity into account """

	def move(self, missile):
		missile.time += DEFAULT_TIME_INCREMENT
		gra = -missile.gravity

		missile.x += (missile.fire_power) * math.cos(missile.angle)
		missile.y -= (missile.fire_power) * math.sin(missile.angle) - 1/2*gra*missile.time*missile.time 

		#missile.x =  missile.fired_pos.x + 20*missile.fire_power * missile.time * math.cos(missile.angle)
		#missile.y =	 missile.fired_pos.y - 20*missile.fire_power * missile.time * math.sin(missile.angle) + 1/2*gra*missile.time*missile.time

		x = missile.x - missile.lastx
		y =  missile.lasty - missile.y

		missile.rotation = math.degrees(math.atan2(y,x))
