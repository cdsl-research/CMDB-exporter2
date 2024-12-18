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

以下のように表示されて入ればOKです．




<img width="483" alt="スクリーンショット 2024-12-18 11 44 02" src="https://github.com/user-attachments/assets/a6ee041c-ea1f-46fa-80bf-4f71cc25646a" />



