# CMDB-exporter2


### 用途

CMDB-Masterに対してデータを送るためのexporterです．

### 環境
- Ubuntu 22.04.4 LTS
- Python 3.10.12
  - ライブラリ
    - re
    - subprocess
    - xmlrpc.server
   
### 使いかた

cdコマンドでCMDB-exporter2/collecter/に移動
```
$ cd CMDB-exporter2/collecter/
```

実行
```
$ python3 cmdb-exporter.py 
Listening on 0.0.0.0:8000...
```

以下のように表示されていればOKです．


<img width="633" alt="スクリーンショット 2024-12-19 14 31 43" src="https://github.com/user-attachments/assets/fe99624e-3e89-4a43-baba-6edabded925c" />







