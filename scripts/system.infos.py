import datetime
import subprocess
from subprocess import check_output


class LoggedUser:
	'''Logged User object class: manages the instance class user attributes'''
	def __init__(self, username, origin, login_at):
		self.username = username
		self.origin = origin
		self.login_at = login_at
class SystemInfo:
	'''System infos object class: manages the instance class system attributes'''
	def __init__(self, uptime_days, uptime_hours_minutes, logged_in_users, load_avg_1_min, load_avg_5_min, load_avg_15_min):
		self.uptime_days = uptime_days
		self.uptime_hours_minutes = uptime_hours_minutes
		self.logged_in_users = logged_in_users
		self.load_avg_1_min = load_avg_1_min
		self.load_avg_5_min = load_avg_5_min
		self.load_avg_15_min = load_avg_15_min

class RamInfo:
	'''Ram infos object class: manages the instance class ram attributes'''
	def __init__(self, total_ram, used_ram, free_ram):
		self.total_ram = total_ram
		self.used_ram = used_ram
		self.free_ram = free_ram

class DiskInfo:
	'''Disk infos object class: manages the instance class disk attributes'''
	def __init__(self, filesystem_disk, size_disk, used_disk, free_disk, percentage_disk_usage):
		self.filesystem_disk = filesystem_disk
		self.size_disk = size_disk
		self.used_disk = used_disk
		self.free_disk = free_disk
		self.percentage_disk_usage = percentage_disk_usage
		
def get_sys_uptime_infos():
	uptime_result = get_subprocess_data("uptime")
	sys_info = SystemInfo(uptime_result[2], uptime_result[4], uptime_result[5], uptime_result[9], uptime_result[10], uptime_result[11])

	return sys_info

def get_sys_logged_in_infos():
	users_result = get_subprocess_data("w | tail -n +3") 
	dict_users = []
	for users_row in range(int(len(users_result) / 8)):
		dict_users.append(LoggedUser(users_result[0], users_result[2], users_result[3]))
	
	return dict_users

def get_ram_infos():
	ram_result = get_subprocess_data("free -m | tail -n +2 | head -n +1")
	ram_info = RamInfo(ram_result[1], ram_result[2], ram_result[3])

	return ram_info

def get_disk_infos():
	disk_result = get_subprocess_data("df -h / | tail -n1")
	
	disk_info = DiskInfo(disk_result[0], disk_result[1], disk_result[2], disk_result[3], disk_result[4])
	
	return disk_info

def get_subprocess_data(command):
	command_result = check_output([(command)], stderr=subprocess.STDOUT, shell=True)
	command_result = command_result.decode('utf-8')
	command_result = command_result.split()
	
	return command_result



with open("/var/log/system_infos.log", "a+") as output:
	sys_infos = get_sys_uptime_infos()
	sys_users_infos = get_sys_logged_in_infos()
	sys_ram_infos = get_ram_infos()
	sys_disk_infos = get_disk_infos()
	
	output.write("*~*~*~*~* SYS INFOS *~*~*~*~*\n")
	output.write("*~*~*~*~* DATETIME: {0} *~*~*~*~*\n".format(datetime.datetime.now()))
	output.write("--------> SYSTEM <--------\n")
	output.write("---> Uptime: {0} Day(s)\n".format(sys_infos.uptime_days))
	output.write("---> Uptime HH:MM: {0}\n".format(sys_infos.uptime_hours_minutes))
	output.write("---> Users currently logged: {0}\n".format(sys_infos.logged_in_users))
	output.write("---> CPU usage (1 min): {0}\n".format(sys_infos.load_avg_1_min))
	output.write("---> CPU usage (5 min): {0}\n".format(sys_infos.load_avg_5_min))
	output.write("---> CPU usage (15 min): {0}\n".format(sys_infos.load_avg_5_min))

	output.write("--------> USERS <--------\n")
	for user in sys_users_infos:
		output.write("---> Username: {0}\n".format(user.username))
		output.write("---> IP Origin: {0}\n".format(user.origin))
		output.write("---> Login@: {0}\n".format(user.login_at))
		
	output.write("--------> MEMORY <--------\n")
	output.write("---> Total Ram: {0} MB\n".format(sys_ram_infos.total_ram))
	output.write("---> Used Ram: {0} MB\n".format(sys_ram_infos.used_ram))
	output.write("---> Free Ram: {0} MB\n".format(sys_ram_infos.free_ram))

	output.write("--------> DISK <--------\n")
	output.write("---> Filesystem: {0}\n".format(sys_disk_infos.filesystem_disk))
	output.write("---> Disk Size: {0} MB\n".format(sys_disk_infos.size_disk))
	output.write("---> Used Disk: {0} MB\n".format(sys_disk_infos.used_disk))
	output.write("---> Free Disk: {0} MB\n".format(sys_disk_infos.free_disk))
	output.write("---> Usage Percentage: {0}\n".format(sys_disk_infos.percentage_disk_usage))
	
	output.write("*~*~*~*~* END *~*~*~*~*\n")
