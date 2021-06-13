#Round-Robin Algorithm
#coded with love

from time import sleep

class RoundRobin:
	def __init__(self):
		self.quantum = int(input('Type the Quantum> '))
		self.switch = int(input('\nType the switch time> '))
		self.n = int(input('\nType the quantity> '))
		self.queue = []
	
	def define_values(self):
		for _ in range(self.n):
			values = int(input('Type the values> '))
			self.queue.append(values)
			
	def do_turn_around(self):
		queue = self.queue
		quantum = self.quantum
		turn_around = [0] * len(queue)
		time = 0

		while (sum(queue) != 0):
			for i in range(len(queue)):
				if (queue[i] <= quantum): 
					if (queue[i] <= turn_around[i]):
						turn_around[i] = time

					time += queue[i]
					queue[i] = 0

					print(f"\nProcess {i + 1} is done!")
					print(f"Finished in {time} u.t")
				elif (queue[i] == 0):
					pass
				else:
					if (queue[i] <= turn_around[i]):
						turn_around[i] = time

					time += quantum
					queue[i] -= quantum

					print(f"\nProcess {i + 1} is done!")
					print(f"Finished in {time} u.t")
					
				turn_around[i] = time
				time += self.switch
			print('~ ' * 15)
		print('All processes done!')
		print(f"Turnaround Time => {(sum(turn_around) / self.n):.2f}")

	def do_wait(self):
		pass		
def main():
	try:
		object_created = RoundRobin()

		object_created.define_values()
		object_created.do_turn_around()
		
	except KeyboardInterrupt:
		print('\n\nSystem shutting down')
		
		sleep(3)

if __name__=='__main__':
	main()

