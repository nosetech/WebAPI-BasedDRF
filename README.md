# WebAPI-BasedDRF

Django REST framework を使用した API 開発を行うベースとなるコードセットです。

# Usage

## プロジェクト初期化

init_project.sh を使用して、新たに開発を行なっていくプロジェクトを作成します。  
以下のようにスクリプトを実行してください。

```
init_project.sh プロジェクト名
```

## ローカル環境の構築

### .env の作成

src/.env を作成してください。

.env 例

```
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
SECRET_KEY=[SECRET KEY]
DATABASE_URL=mysql://admin:admin@db:3306/webapi_db
JWT_EXPIRATION_SECONDS=3600
JWT_REFRESH_EXPIRATION_DAYS=1
CORS_ORIGIN=http://localhost:3000
DJANGO_LOG_LEVEL='INFO'
APP_LOG_LEVEL='DEBUG'
```

| 環境変数                    | 説明                                                     | 設定値                                                                 |
| --------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------- |
| DEBUG                       | デバッグモードの ON/OFF                                  | True or False                                                          |
| ALLOWED_HOSTS               | アクセスを許可する接続元アドレス                         | ex) localhost                                                          |
| SECRET_KEY                  | django シークレットキー                                  | ex) django プロジェクト作成時に settigs.py に記載されている SECRET_KEY |
| DATABASE_URL                | データベースの接続先 URL                                 | ex) mysql:admin:admin@db:3306/webapi_db                                |
| JWT_EXPIRATION_SECONDS      | JWT アクセストークンの有効期限(秒)                       | ex) 3600                                                               |
| JWT_REFRESH_EXPIRATION_DAYS | JWT リフレッシュトークンの有効期限(日数)                 | ex) 1                                                                  |
| CORS_ORIGIN                 | アクセスを許可するオリジン                               | ex) http://localhost:3000                                              |
| DJANGO_LOG_LEVEL            | django フレームワークが出力するログのログレベル          | DEBUG, INFO, WARNING, ERROR, CRITICAL                                  |
| APP_LOG_LEVEL               | 自分で追加したアプリケーションが出力するログのログレベル | DEBUG, INFO, WARNING, ERROR, CRITICAL                                  |

### docker 環境のビルド・実行

```
docker compose build
```

```
docker compose up -d
```

### DB マイグレーション、スーパーユーザー作成

```
docker exec -it webapi_app python manage.py migrate
```

```
docker exec -it webapi_app python manage.py createsuperuser
```

### その他

- tox の実行

```
docker exec -it webapi_app tox
```
