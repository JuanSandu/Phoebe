import tcp
import pwm

try:
	server=tcp.mysocket()
	server.server("192.168.1.192",4200)		#RPI IP
	server.accept()

	exit = False

	while not exit:
		tcp_input = server.receive()
		#print tcp_input
		if tcp_input == "RIGHT":
			right_motor = int(server.receive())
			#right_motor = server.receive()
			print "RIGHT: ", right_motor
		elif tcp_input == "LEFT":
			left_motor = int(server.receive())
			print "LEFT: ", left_motor
		elif tcp_input == "EXIT":
			exit = True
			print "EXIT: ", exit
finally:
	print "Closing"
	server.closesocket()
