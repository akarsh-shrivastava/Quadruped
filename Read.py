from time import sleep


def read_from_file(filename,th_list=[],off_list=[]):
	motion_set=[]
	try:
		file=open(filename,'r')
		angles=file.read()

		i=0
		for th in th_list:
			i+=1
			angles=angles.replace('m'+str(i),str(th))

		i=0
		for off in off_list:
			i+=1
			angles=angles.replace('o'+str(i),str(off))

		motions=angles.split('\n')
		motions=filter(None,motions)

		for motion in motions:
			motion_split=motion.split('|')
			ang_str,wait_time_str = motion_split[0],motion_split[1]

			wait_time_float=float(filter(None,str(wait_time_str).split())[0])

			ang_list_str=filter( None, ang_str.split() )
			ang_list_float=[float(x) for x in ang_list_str]

			motion_set.append([ang_list_float,wait_time_float])



	except IOError:
		raise 'File not found\n'

	return filter(None,motion_set)



def do_motion(dxl, filename, times='infinite', th_list=[], off_list=[]):
	motion_set=read_from_file(filename,th_list=[], off_list=[])

	if times=='infinite':
		while True:
			try:
				for motion in motion_set:
					dxl.set_position(motion[0])
					sleep(motion[1])
			except KeyboardInterrupt:
				break

	else:
		try:
			for i in range(int(times)):
				for motion in motion_set:
					dxl.set_position(motion[0])
					sleep(motion[1])
		except ValueError:
			raise("invalid number of times")
		except KeyboardInterrupt:
			pass
