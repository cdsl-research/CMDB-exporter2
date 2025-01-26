import subprocess
from xmlrpc.server import SimpleXMLRPCServer

command = "ss -tunap | grep 'ESTAB'"
HOST = "0.0.0.0"
PORT = 8000

def get_connnection():
    command_print = subprocess.run(command,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    command_data = command_print.stdout
    print(command_data) #stdoutの情報を取得
    command_lines = command_data.splitlines() #リスト型に変換
    command_list = [item.split() for item in command_lines]

    return command_list


server = SimpleXMLRPCServer((HOST, PORT), allow_none=True)
server.register_function(get_connnection, "get_connnection")  # 関数を登録
print(f"Listening on {HOST}:{PORT}...")
server.serve_forever()

