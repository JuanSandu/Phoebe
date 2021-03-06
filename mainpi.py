import tcp
import pwm

def map(bar, from_min,  from_max,  to_min,  to_max):
  return (bar - from_min) * (to_max - to_min) / (from_max - from_min) + to_min;

try:
	right_pin = pwm.__init__(24,1000)
	left_pin = pwm.__init__(5,1000)
	pwm.start(right_pin,0)
	pwm.start(left_pin,0)

	server=tcp.mysocket()
	server.server("192.168.1.192",4200)		#RPI IP
	server.accept()

	exit = False

	while not exit:
		tcp_input = server.receive()
		if tcp_input == "RIGHT":
			right_motor = map(int(server.receive()),0,255,5,10)
			pwm.changedc(right_pin,right_motor)
		elif tcp_input == "LEFT":
			left_motor = map(int(server.receive()),0,255,5,10)
			pwm.changedc(left_pin,left_motor)
		elif tcp_input == "EXIT":
			exit = True
finally:
	pwm.end(left_pin)
	pwm.end(right_pin)
	pwm.clean()

	server.closesocket()
