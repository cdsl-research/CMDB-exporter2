from xmlrpc.server import SimpleXMLRPCServer
import subprocess
import re

# サーバーの設定
HOST = "0.0.0.0"
PORT = 8000

def get_network_status():
    """
    ss -tunap の出力を取得し、Peer Address:Port だけを抽出し、IPv6アドレスを除外し、
    192.168.100.24 と (hostname -I の IP) と (PeerAddress:Port) を結合して返す
    """
    try:
        # ssコマンドを実行
        result = subprocess.run(["ss", "-tunap"], capture_output=True, text=True, check=True)
        output = result.stdout

        # Peer Address:Port を抽出する正規表現
        peer_address_pattern = re.compile(r'\s+(\S+:\d+)\s*$')

        # Peer Address:Port のリストを作成
        peer_addresses = []
        for line in output.splitlines():
            match = peer_address_pattern.search(line)
            if match:
                peer = match.group(1)
                # IPv6アドレス（[::ffff:...]）を除外する
                if not peer.startswith("[::ffff:"):
                    peer_addresses.append(peer)

        # ホストのIPアドレスを取得 (hostname -I コマンド)
        hostname_result = subprocess.run(["hostname", "-I"], capture_output=True, text=True, check=True)
        hostname_ip = hostname_result.stdout.strip()

        # 結果を (192.168.100.24, IP, PeerAddress:Port) 形式で返す
        result_string = ""
        for peer in peer_addresses:
            result_string += f"(192.168.100.24,{hostname_ip},{peer})\n"

        return result_string.strip()  # 最後に改行がないようにする

    except subprocess.CalledProcessError as e:
        return f"Command error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

# サーバーの起動
server = SimpleXMLRPCServer((HOST, PORT), allow_none=True)
print(f"Listening on {HOST}:{PORT}...")

# 関数を登録
server.register_function(get_network_status, "get_network_status")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Server stopped.")

