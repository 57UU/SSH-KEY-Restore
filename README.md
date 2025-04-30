# SSH-KEY-Restore

windows重装系统后，恢复原先的免密登录

文件目录如下

分别对应私钥与公钥
```
-keys
  -key
  -key.pub
```
其中，公钥被更新（当前用户名与计算机名），私钥复制到原位置(重命名为id_rsa)