Collecting uvicorn>=0.12.0 (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached uvicorn-0.37.0-py3-none-any.whl.metadata (6.6 kB)
Collecting httpcore==1.* (from httpx>=0.25.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting h11>=0.16 (from httpcore==1.*->httpx>=0.25.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting dnspython>=2.0.0 (from email-validator>=2.0.0->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached dnspython-2.8.0-py3-none-any.whl.metadata (5.7 kB)
Collecting typer>=0.15.1 (from fastapi-cli>=0.0.8->fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached typer-0.19.2-py3-none-any.whl.metadata (16 kB)
Collecting rich-toolkit>=0.14.8 (from fastapi-cli>=0.0.8->fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached rich_toolkit-0.15.1-py3-none-any.whl.metadata (1.0 kB)
Collecting greenlet!=0.4.17 (from greenback>=1.2.1->apache-airflow-task-sdk==1.1.0->apache-airflow)
  Downloading greenlet-3.2.4-cp312-cp312-win_amd64.whl.metadata (4.2 kB)
Collecting outcome (from greenback>=1.2.1->apache-airflow-task-sdk==1.1.0->apache-airflow)
  Downloading outcome-1.3.0.post0-py2.py3-none-any.whl.metadata (2.6 kB)
Collecting zipp>=3.20 (from importlib-metadata>=7.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached zipp-3.23.0-py3-none-any.whl.metadata (3.6 kB)
Collecting MarkupSafe>=2.0 (from jinja2>=3.1.5->apache-airflow-core==3.1.0->apache-airflow)
  Downloading markupsafe-3.0.3-cp312-cp312-win_amd64.whl.metadata (2.8 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=4.19.1->apache-airflow-core==3.1.0->apache-airflow)
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=4.19.1->apache-airflow-core==3.1.0->apache-airflow)
  Downloading referencing-0.36.2-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.7.1 (from jsonschema>=4.19.1->apache-airflow-core==3.1.0->apache-airflow)
  Downloading rpds_py-0.27.1-cp312-cp312-win_amd64.whl.metadata (4.3 kB)
Collecting pyyaml>=5.2 (from libcst>=1.8.2->apache-airflow-core==3.1.0->apache-airflow)
  Downloading pyyaml-6.0.3-cp312-cp312-win_amd64.whl.metadata (2.4 kB)
Collecting uc-micro-py (from linkify-it-py>=2.0.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached uc_micro_py-1.0.3-py3-none-any.whl.metadata (2.0 kB)
Collecting wirerope>=0.4.7 (from methodtools>=0.4.7->apache-airflow-core==3.1.0->apache-airflow)
  Using cached wirerope-1.0.0-py2.py3-none-any.whl.metadata (3.3 kB)
Collecting opentelemetry-exporter-otlp-proto-grpc==1.37.0 (from opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached opentelemetry_exporter_otlp_proto_grpc-1.37.0-py3-none-any.whl.metadata (2.4 kB)
Collecting opentelemetry-exporter-otlp-proto-http==1.37.0 (from opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached opentelemetry_exporter_otlp_proto_http-1.37.0-py3-none-any.whl.metadata (2.3 kB)
Collecting googleapis-common-protos~=1.57 (from opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached googleapis_common_protos-1.70.0-py3-none-any.whl.metadata (9.3 kB)
Collecting grpcio<2.0.0,>=1.63.2 (from opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow)
  Downloading grpcio-1.75.1-cp312-cp312-win_amd64.whl.metadata (3.8 kB)
Collecting opentelemetry-exporter-otlp-proto-common==1.37.0 (from opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached opentelemetry_exporter_otlp_proto_common-1.37.0-py3-none-any.whl.metadata (1.8 kB)
Collecting opentelemetry-sdk~=1.37.0 (from opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached opentelemetry_sdk-1.37.0-py3-none-any.whl.metadata (1.5 kB)
Collecting opentelemetry-semantic-conventions==0.58b0 (from opentelemetry-sdk~=1.37.0->opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached opentelemetry_semantic_conventions-0.58b0-py3-none-any.whl.metadata (2.4 kB)
Collecting six>=1.5 (from python-dateutil>=2.7.0->apache-airflow-core==3.1.0->apache-airflow)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting text-unidecode>=1.3 (from python-slugify>=5.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached text_unidecode-1.3-py2.py3-none-any.whl.metadata (2.4 kB)
Collecting markdown-it-py>=2.2.0 (from rich>=13.6.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached markdown_it_py-4.0.0-py3-none-any.whl.metadata (7.3 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=13.6.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting click>=8.1.7 (from rich-toolkit>=0.14.8->fastapi-cli>=0.0.8->fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow)
  Downloading click-8.3.0-py3-none-any.whl.metadata (2.6 kB)
Collecting shellingham>=1.3.0 (from typer>=0.15.1->fastapi-cli>=0.0.8->fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting pathlib-abc==0.5.1 (from universal-pathlib!=0.2.4,>=0.2.2->apache-airflow-core==3.1.0->apache-airflow)
  Using cached pathlib_abc-0.5.1-py3-none-any.whl.metadata (4.6 kB)
Collecting httptools>=0.6.3 (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow)
  Downloading httptools-0.6.4-cp312-cp312-win_amd64.whl.metadata (3.7 kB)
Collecting python-dotenv>=0.13 (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow)
  Using cached python_dotenv-1.1.1-py3-none-any.whl.metadata (24 kB)
Collecting watchfiles>=0.13 (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow)
  Downloading watchfiles-1.1.0-cp312-cp312-win_amd64.whl.metadata (5.0 kB)
Collecting websockets>=10.4 (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow)
  Downloading websockets-15.0.1-cp312-cp312-win_amd64.whl.metadata (7.0 kB)
Using cached apache_airflow-3.1.0-py3-none-any.whl (12 kB)
Using cached apache_airflow_core-3.1.0-py3-none-any.whl (5.3 MB)
Using cached apache_airflow_task_sdk-1.1.0-py3-none-any.whl (297 kB)
Using cached alembic-1.16.5-py3-none-any.whl (247 kB)
Using cached opentelemetry_proto-1.37.0-py3-none-any.whl (72 kB)
Using cached protobuf-6.32.1-cp310-abi3-win_amd64.whl (435 kB)
Downloading requests-2.32.5-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.3-cp312-cp312-win_amd64.whl (107 kB)
Downloading idna-3.10-py3-none-any.whl (70 kB)
Downloading urllib3-2.5.0-py3-none-any.whl (129 kB)
Downloading apache_airflow_providers_postgres-6.3.0-py3-none-any.whl (22 kB)
Downloading pandas-2.3.3-cp312-cp312-win_amd64.whl (11.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.0/11.0 MB 2.1 MB/s  0:00:05
Using cached a2wsgi-1.10.10-py3-none-any.whl (17 kB)
Using cached aiosqlite-0.21.0-py3-none-any.whl (15 kB)
Using cached apache_airflow_providers_common_compat-1.7.4-py3-none-any.whl (30 kB)
Using cached apache_airflow_providers_common_io-1.6.3-py3-none-any.whl (19 kB)
Using cached apache_airflow_providers_common_sql-1.28.1-py3-none-any.whl (66 kB)
Using cached apache_airflow_providers_smtp-2.3.1-py3-none-any.whl (24 kB)
Using cached aiosmtplib-4.0.2-py3-none-any.whl (27 kB)
Using cached apache_airflow_providers_standard-1.9.0-py3-none-any.whl (144 kB)
Using cached argcomplete-3.6.2-py3-none-any.whl (43 kB)
Downloading asgiref-3.10.0-py3-none-any.whl (24 kB)
Downloading asyncpg-0.30.0-cp312-cp312-win_amd64.whl (621 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 621.1/621.1 kB 2.1 MB/s  0:00:00
Downloading attrs-25.4.0-py3-none-any.whl (67 kB)
Using cached cadwyn-5.4.4-py3-none-any.whl (60 kB)
Downloading certifi-2025.10.5-py3-none-any.whl (163 kB)
Using cached colorlog-6.9.0-py3-none-any.whl (11 kB)
Using cached cron_descriptor-2.0.6-py3-none-any.whl (74 kB)
Using cached croniter-6.0.0-py2.py3-none-any.whl (25 kB)
Downloading cryptography-46.0.2-cp311-abi3-win_amd64.whl (3.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.5/3.5 MB 2.0 MB/s  0:00:01
Downloading cffi-2.0.0-cp312-cp312-win_amd64.whl (183 kB)
Downloading Deprecated-1.2.18-py2.py3-none-any.whl (10.0 kB)
Downloading wrapt-1.17.3-cp312-cp312-win_amd64.whl (38 kB)
Using cached dill-0.4.0-py3-none-any.whl (119 kB)
Using cached fastapi-0.118.0-py3-none-any.whl (97 kB)
Using cached pydantic-2.11.10-py3-none-any.whl (444 kB)
Downloading pydantic_core-2.33.2-cp312-cp312-win_amd64.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 1.8 MB/s  0:00:01
Using cached starlette-0.48.0-py3-none-any.whl (73 kB)
Using cached anyio-4.11.0-py3-none-any.whl (109 kB)
Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Using cached email_validator-2.3.0-py3-none-any.whl (35 kB)
Using cached dnspython-2.8.0-py3-none-any.whl (331 kB)
Using cached fastapi_cli-0.0.13-py3-none-any.whl (11 kB)
Using cached fsspec-2025.9.0-py3-none-any.whl (199 kB)
Using cached greenback-1.2.1-py3-none-any.whl (28 kB)
Downloading greenlet-3.2.4-cp312-cp312-win_amd64.whl (299 kB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Using cached importlib_metadata-8.7.0-py3-none-any.whl (27 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading jsonschema-4.25.1-py3-none-any.whl (90 kB)
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading lazy_object_proxy-1.12.0-cp312-cp312-win_amd64.whl (26 kB)
Downloading libcst-1.8.5-cp312-cp312-win_amd64.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 3.1 MB/s  0:00:00
Using cached linkify_it_py-2.0.3-py3-none-any.whl (19 kB)
Using cached lockfile-0.12.2-py2.py3-none-any.whl (13 kB)
Downloading markupsafe-3.0.3-cp312-cp312-win_amd64.whl (15 kB)
Using cached methodtools-0.4.7-py2.py3-none-any.whl (4.0 kB)
Using cached more_itertools-10.8.0-py3-none-any.whl (69 kB)
Downloading msgspec-0.19.0-cp312-cp312-win_amd64.whl (187 kB)
Using cached natsort-8.4.0-py3-none-any.whl (38 kB)
Downloading numpy-2.3.3-cp312-cp312-win_amd64.whl (12.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.8/12.8 MB 2.0 MB/s  0:00:06
Using cached opentelemetry_api-1.37.0-py3-none-any.whl (65 kB)
Using cached opentelemetry_exporter_otlp-1.37.0-py3-none-any.whl (7.0 kB)
Using cached opentelemetry_exporter_otlp_proto_grpc-1.37.0-py3-none-any.whl (19 kB)
Using cached opentelemetry_exporter_otlp_proto_common-1.37.0-py3-none-any.whl (18 kB)
Using cached opentelemetry_exporter_otlp_proto_http-1.37.0-py3-none-any.whl (19 kB)
Using cached googleapis_common_protos-1.70.0-py3-none-any.whl (294 kB)
Downloading grpcio-1.75.1-cp312-cp312-win_amd64.whl (4.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.6/4.6 MB 1.9 MB/s  0:00:02
Using cached opentelemetry_sdk-1.37.0-py3-none-any.whl (131 kB)
Using cached opentelemetry_semantic_conventions-0.58b0-py3-none-any.whl (207 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Using cached pathspec-0.12.1-py3-none-any.whl (31 kB)
Downloading pendulum-3.1.0-cp312-cp312-win_amd64.whl (260 kB)
Using cached pluggy-1.6.0-py3-none-any.whl (20 kB)
Downloading psutil-7.1.0-cp37-abi3-win_amd64.whl (247 kB)
Downloading psycopg2_binary-2.9.10-cp312-cp312-win_amd64.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 3.2 MB/s  0:00:00
Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 2.8 MB/s  0:00:00
Using cached pygtrie-2.5.0-py3-none-any.whl (25 kB)
Using cached PyJWT-2.10.1-py3-none-any.whl (22 kB)
Using cached python_daemon-3.1.2-py3-none-any.whl (30 kB)
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached python_multipart-0.0.20-py3-none-any.whl (24 kB)
Using cached python_slugify-8.0.4-py2.py3-none-any.whl (10 kB)
Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
Downloading pyyaml-6.0.3-cp312-cp312-win_amd64.whl (154 kB)
Downloading referencing-0.36.2-py3-none-any.whl (26 kB)
Using cached retryhttp-1.3.3-py3-none-any.whl (17 kB)
Using cached rich-14.1.0-py3-none-any.whl (243 kB)
Using cached markdown_it_py-4.0.0-py3-none-any.whl (87 kB)
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Using cached rich_argparse-1.7.1-py3-none-any.whl (25 kB)
Using cached rich_toolkit-0.15.1-py3-none-any.whl (29 kB)
Downloading click-8.3.0-py3-none-any.whl (107 kB)
Downloading rpds_py-0.27.1-cp312-cp312-win_amd64.whl (232 kB)
Downloading setproctitle-1.3.7-cp312-cp312-win_amd64.whl (13 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
Downloading sqlalchemy-2.0.43-cp312-cp312-win_amd64.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 3.5 MB/s  0:00:00
Using cached SQLAlchemy_JSONField-1.0.2-py3-none-any.whl (10 kB)
Using cached sqlalchemy_utils-0.42.0-py3-none-any.whl (91 kB)
Downloading sqlparse-0.5.3-py3-none-any.whl (44 kB)
Using cached structlog-25.4.0-py3-none-any.whl (68 kB)
Using cached svcs-25.1.0-py3-none-any.whl (19 kB)
Using cached tabulate-0.9.0-py3-none-any.whl (35 kB)
Using cached tenacity-9.1.2-py3-none-any.whl (28 kB)
Using cached termcolor-3.1.0-py3-none-any.whl (7.7 kB)
Using cached text_unidecode-1.3-py2.py3-none-any.whl (78 kB)
Using cached typer-0.19.2-py3-none-any.whl (46 kB)
Using cached shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
Using cached types_requests-2.32.4.20250913-py3-none-any.whl (20 kB)
Using cached typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Using cached universal_pathlib-0.3.2-py3-none-any.whl (67 kB)
Using cached pathlib_abc-0.5.1-py3-none-any.whl (20 kB)
Using cached uuid6-2025.0.1-py3-none-any.whl (7.0 kB)
Using cached uvicorn-0.37.0-py3-none-any.whl (67 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading httptools-0.6.4-cp312-cp312-win_amd64.whl (88 kB)
Using cached python_dotenv-1.1.1-py3-none-any.whl (20 kB)
Downloading watchfiles-1.1.0-cp312-cp312-win_amd64.whl (292 kB)
Downloading websockets-15.0.1-cp312-cp312-win_amd64.whl (176 kB)
Using cached wirerope-1.0.0-py2.py3-none-any.whl (9.2 kB)
Using cached zipp-3.23.0-py3-none-any.whl (10 kB)
Using cached mako-1.3.10-py3-none-any.whl (78 kB)
Downloading outcome-1.3.0.post0-py2.py3-none-any.whl (10 kB)
Downloading pycparser-2.23-py3-none-any.whl (118 kB)
Using cached uc_micro_py-1.0.3-py3-none-any.whl (6.2 kB)
Installing collected packages: text-unidecode, pytz, pygtrie, lockfile, zipp, wrapt, websockets, uuid6, urllib3, uc-micro-py, tzdata, typing-extensions, termcolor, tenacity, tabulate, structlog, sqlparse, sniffio, six, shellingham, setproctitle, rpds-py, pyyaml, python-slugify, python-multipart, python-dotenv, python-daemon, pyjwt, pygments, pycparser, psycopg2-binary, psutil, protobuf, pluggy, pathspec, pathlib-abc, packaging, numpy, natsort, msgspec, more-itertools, mdurl, MarkupSafe, lazy-object-proxy, itsdangerous, idna, httptools, h11, greenlet, fsspec, dnspython, dill, colorama, charset_normalizer, certifi, attrs, asyncpg, asgiref, argcomplete, annotated-types, aiosmtplib, a2wsgi, wirerope, universal-pathlib, typing-inspection, types-requests, svcs, sqlalchemy, requests, referencing, python-dateutil, pydantic-core, outcome, opentelemetry-proto, markdown-it-py, Mako, linkify-it-py, libcst, jinja2, importlib-metadata, httpcore, grpcio, googleapis-common-protos, email-validator, deprecated, cron-descriptor, colorlog, click, cffi, anyio, aiosqlite, watchfiles, uvicorn, starlette, sqlalchemy-utils, sqlalchemy-jsonfield, rich, pydantic, pendulum, pandas, opentelemetry-exporter-otlp-proto-common, opentelemetry-api, methodtools, jsonschema-specifications, httpx, greenback, cryptography, croniter, alembic, typer, rich-toolkit, rich-argparse, retryhttp, opentelemetry-semantic-conventions, jsonschema, fastapi, opentelemetry-sdk, fastapi-cli, cadwyn, opentelemetry-exporter-otlp-proto-http, opentelemetry-exporter-otlp-proto-grpc, opentelemetry-exporter-otlp, apache-airflow-providers-standard, apache-airflow-providers-smtp, apache-airflow-providers-common-io, apache-airflow-providers-common-compat, apache-airflow-task-sdk, apache-airflow-providers-common-sql, apache-airflow-core, apache-airflow, apache-airflow-providers-postgres
Successfully installed Mako-1.3.10 MarkupSafe-3.0.3 a2wsgi-1.10.10 aiosmtplib-4.0.2 aiosqlite-0.21.0 alembic-1.16.5 annotated-types-0.7.0 anyio-4.11.0 apache-airflow-3.1.0 apache-airflow-core-3.1.0 apache-airflow-providers-common-compat-1.7.4 apache-airflow-providers-common-io-1.6.3 apache-airflow-providers-common-sql-1.28.1 apache-airflow-providers-postgres-6.3.0 apache-airflow-providers-smtp-2.3.1 apache-airflow-providers-standard-1.9.0 apache-airflow-task-sdk-1.1.0 argcomplete-3.6.2 asgiref-3.10.0 asyncpg-0.30.0 attrs-25.4.0 cadwyn-5.4.4 certifi-2025.10.5 cffi-2.0.0 charset_normalizer-3.4.3 click-8.3.0 colorama-0.4.6 colorlog-6.9.0 cron-descriptor-2.0.6 croniter-6.0.0 cryptography-46.0.2 deprecated-1.2.18 dill-0.4.0 dnspython-2.8.0 email-validator-2.3.0 fastapi-0.118.0 fastapi-cli-0.0.13 fsspec-2025.9.0 googleapis-common-protos-1.70.0 greenback-1.2.1 greenlet-3.2.4 grpcio-1.75.1 
h11-0.16.0 httpcore-1.0.9 httptools-0.6.4 httpx-0.28.1 idna-3.10 importlib-metadata-8.7.0 itsdangerous-2.2.0 jinja2-3.1.6 jsonschema-4.25.1 jsonschema-specifications-2025.9.1 lazy-object-proxy-1.12.0 libcst-1.8.5 linkify-it-py-2.0.3 lockfile-0.12.2 markdown-it-py-4.0.0 mdurl-0.1.2 methodtools-0.4.7 more-itertools-10.8.0 msgspec-0.19.0 natsort-8.4.0 numpy-2.3.3 opentelemetry-api-1.37.0 opentelemetry-exporter-otlp-1.37.0 opentelemetry-exporter-otlp-proto-common-1.37.0 opentelemetry-exporter-otlp-proto-grpc-1.37.0 opentelemetry-exporter-otlp-proto-http-1.37.0 opentelemetry-proto-1.37.0 opentelemetry-sdk-1.37.0 opentelemetry-semantic-conventions-0.58b0 outcome-1.3.0.post0 packaging-25.0 pandas-2.3.3 pathlib-abc-0.5.1 pathspec-0.12.1 pendulum-3.1.0 pluggy-1.6.0 protobuf-6.32.1 psutil-7.1.0 psycopg2-binary-2.9.10 pycparser-2.23 pydantic-2.11.10 pydantic-core-2.33.2 pygments-2.19.2 pygtrie-2.5.0 pyjwt-2.10.1 python-daemon-3.1.2 python-dateutil-2.9.0.post0 python-dotenv-1.1.1 python-multipart-0.0.20 python-slugify-8.0.4 pytz-2025.2 pyyaml-6.0.3 referencing-0.36.2 requests-2.32.5 retryhttp-1.3.3 rich-14.1.0 rich-argparse-1.7.1 rich-toolkit-0.15.1 rpds-py-0.27.1 setproctitle-1.3.7 shellingham-1.5.4 six-1.17.0 sniffio-1.3.1 sqlalchemy-2.0.43 sqlalchemy-jsonfield-1.0.2 sqlalchemy-utils-0.42.0 sqlparse-0.5.3 starlette-0.48.0 structlog-25.4.0 svcs-25.1.0 tabulate-0.9.0 tenacity-9.1.2 termcolor-3.1.0 text-unidecode-1.3 typer-0.19.2 types-requests-2.32.4.20250913 typing-extensions-4.15.0 typing-inspection-0.4.2 tzdata-2025.2 uc-micro-py-1.0.3 universal-pathlib-0.3.2 urllib3-2.5.0 uuid6-2025.0.1 uvicorn-0.37.0 watchfiles-1.1.0 websockets-15.0.1 wirerope-1.0.0 wrapt-1.17.3 zipp-3.23.0
(.venv) PS D:\Python\complementos\faculdade> python "Criando DAGs.py"
D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__init__.py:45: RuntimeWarning: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly tested on fairly modern Linux Distros and recent versions of macOS. On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers. The work to add Windows support is tracked via https://github.com/apache/airflow/issues/10388, but it is not a high priority.
  warnings.warn(
D:\Python\complementos\faculdade\Criando DAGs.py:3 DeprecatedImportWarning: The `airflow.operators.bash.BashOperator` attribute is deprecated. Please use `'airflow.providers.standard.operators.bash.BashOperator'`.
D:\Python\complementos\faculdade\Criando DAGs.py:4 DeprecatedImportWarning: The `airflow.operators.python.PythonOperator` attribute is deprecated. Please use `'airflow.providers.standard.operators.python.PythonOperator'`.
Traceback (most recent call last):
  File "D:\Python\complementos\faculdade\Criando DAGs.py", line 5, in <module>
    from airflow.providers.postgres.operators.postgres import PostgresOperator
ModuleNotFoundError: No module named 'airflow.providers.postgres.operators'
(.venv) PS D:\Python\complementos\faculdade> python -c "from airflow.providers.postgres.operators.postgres import PostgresOperator; print('Postgres OK')"
D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__init__.py:45: RuntimeWarning: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly tested on fairly modern Linux Distros and recent versions of macOS. On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers. The work to add Windows support is tracked via https://github.com/apache/airflow/issues/10388, but it is not a high priority.
  warnings.warn(
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'airflow.providers.postgres.operators'
(.venv) PS D:\Python\complementos\faculdade> python -c "import airflow.providers.postgres; import os; print(os.listdir(os.path.dirname(airflow.providers.postgres.__file__)))"     
D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__init__.py:45: RuntimeWarning: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly tested on fairly modern Linux Distros and recent versions of macOS. On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers. The work to add Windows support is tracked via https://github.com/apache/airflow/issues/10388, but it is not a high priority.
  warnings.warn(
['assets', 'dialects', 'get_provider_info.py', 'hooks', 'LICENSE', '__init__.py', '__pycache__']
(.venv) PS D:\Python\complementos\faculdade> python -c "from airflow.providers.postgres.hooks.postgres import PostgresHook; print('PostgresHook OK')"
D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__init__.py:45: RuntimeWarning: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly tested on fairly modern Linux Distros and recent versions of macOS. On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers. The work to add Windows support is tracked via https://github.com/apache/airflow/issues/10388, but it is not a high priority.
  warnings.warn(
PostgresHook OK
(.venv) PS D:\Python\complementos\faculdade> python -c "from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator; print('SQL Operator OK')"
D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__init__.py:45: RuntimeWarning: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly tested on fairly modern Linux Distros and recent versions of macOS. On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers. The work to add Windows support is tracked via https://github.com/apache/airflow/issues/10388, but it is not a high priority.
  warnings.warn(
SQL Operator OK
(.venv) PS D:\Python\complementos\faculdade> python "Criando DAGs.py"
D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__init__.py:45: RuntimeWarning: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly tested on fairly modern Linux Distros and recent versions of macOS. On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers. The work to add Windows support is tracked via https://github.com/apache/airflow/issues/10388, but it is not a high priority.
  warnings.warn(
D:\Python\complementos\faculdade\Criando DAGs.py:3 DeprecatedImportWarning: The `airflow.operators.bash.BashOperator` attribute is deprecated. Please use `'airflow.providers.standard.operators.bash.BashOperator'`.
D:\Python\complementos\faculdade\Criando DAGs.py:4 DeprecatedImportWarning: The `airflow.operators.python.PythonOperator` attribute is deprecated. Please use `'airflow.providers.standard.operators.python.PythonOperator'`.
Traceback (most recent call last):
  File "D:\Python\complementos\faculdade\Criando DAGs.py", line 16, in <module>
    with DAG(
         ^^^^
TypeError: DAG.__init__() got an unexpected keyword argument 'schedule_interval'
(.venv) PS D:\Python\complementos\faculdade> (Get-Content "Criando DAGs.py") -replace 'schedule_interval', 'schedule' | Set-Content "Criando DAGs.py"
(.venv) PS D:\Python\complementos\faculdade> 
(.venv) PS D:\Python\complementos\faculdade> pip install apache-airflow
Requirement already satisfied: apache-airflow in d:\python\complementos\faculdade\.venv\lib\site-packages (3.1.0)
Requirement already satisfied: apache-airflow-core==3.1.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow) (3.1.0)
Requirement already satisfied: apache-airflow-task-sdk==1.1.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow) (1.1.0)
Requirement already satisfied: natsort>=8.4.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow) (8.4.0)
Requirement already satisfied: a2wsgi>=1.10.8 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.10.10)
Requirement already satisfied: aiosqlite>=0.20.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.21.0)
Requirement already satisfied: alembic<2.0,>=1.13.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.16.5)
Requirement already satisfied: apache-airflow-providers-common-compat>=1.6.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.7.4)
Requirement already satisfied: apache-airflow-providers-common-io>=1.5.3 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.6.3)
Requirement already satisfied: apache-airflow-providers-common-sql>=1.26.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.28.1)
Requirement already satisfied: apache-airflow-providers-smtp>=2.0.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.3.1)
Requirement already satisfied: apache-airflow-providers-standard>=0.4.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.9.0)
Requirement already satisfied: argcomplete>=1.10 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (3.6.2)
Requirement already satisfied: asgiref>=2.3.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (3.10.0)
Requirement already satisfied: attrs!=25.2.0,>=22.1.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (25.4.0)       
Requirement already satisfied: cadwyn>=5.2.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (5.4.4)
Requirement already satisfied: colorlog>=6.8.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (6.9.0)
Requirement already satisfied: cron-descriptor>=1.2.24 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.0.6)       
Requirement already satisfied: croniter>=2.0.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (6.0.0)
Requirement already satisfied: cryptography>=41.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (46.0.2)
Requirement already satisfied: deprecated>=1.2.13 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.2.18)
Requirement already satisfied: dill>=0.2.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.4.0)
Requirement already satisfied: fastapi>=0.116.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.118.0)
Requirement already satisfied: httpx>=0.25.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.28.1)
Requirement already satisfied: importlib-metadata>=7.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (8.7.0)
Requirement already satisfied: itsdangerous>=2.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.2.0)
Requirement already satisfied: jinja2>=3.1.5 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (3.1.6)
Requirement already satisfied: jsonschema>=4.19.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (4.25.1)
Requirement already satisfied: lazy-object-proxy>=1.2.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.12.0)     
Requirement already satisfied: libcst>=1.8.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.8.5)
Requirement already satisfied: linkify-it-py>=2.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.0.3)
Requirement already satisfied: lockfile>=0.12.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.12.2)
Requirement already satisfied: methodtools>=0.4.7 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.4.7)
Requirement already satisfied: msgspec>=0.19.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.19.0)
Requirement already satisfied: opentelemetry-api>=1.27.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.37.0)    
Requirement already satisfied: opentelemetry-exporter-otlp>=1.27.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.37.0)
Requirement already satisfied: opentelemetry-proto<9999,>=1.27.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.37.0)
Requirement already satisfied: packaging>=25.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (25.0)
Requirement already satisfied: pathspec>=0.9.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.12.1)
Requirement already satisfied: pendulum>=3.1.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (3.1.0)
Requirement already satisfied: pluggy>=1.5.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.6.0)
Requirement already satisfied: psutil>=5.8.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (7.1.0)
Requirement already satisfied: pydantic>=2.11.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.11.10)
Requirement already satisfied: pygments!=2.19.0,>=2.0.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.19.2)
Requirement already satisfied: pygtrie>=2.5.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.5.0)
Requirement already satisfied: pyjwt>=2.10.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.10.1)
Requirement already satisfied: python-daemon>=3.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (3.1.2)
Requirement already satisfied: python-dateutil>=2.7.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.9.0.post0)  
Requirement already satisfied: python-slugify>=5.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (8.0.4)
Requirement already satisfied: requests<3,>=2.32.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.32.5)
Requirement already satisfied: rich-argparse>=1.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.7.1)
Requirement already satisfied: rich>=13.6.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (14.1.0)
Requirement already satisfied: setproctitle>=1.3.3 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.3.7)
Requirement already satisfied: sqlalchemy-jsonfield>=1.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.0.2)     
Requirement already satisfied: sqlalchemy-utils>=0.41.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.42.0)     
Requirement already satisfied: sqlalchemy>=1.4.49 in d:\python\complementos\faculdade\.venv\lib\site-packages (from sqlalchemy[asyncio]>=1.4.49->apache-airflow-core==3.1.0->apache-airflow) (2.0.43)
Requirement already satisfied: starlette>=0.45.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.48.0)
Requirement already satisfied: structlog>=25.4.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (25.4.0)
Requirement already satisfied: svcs>=25.1.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (25.1.0)
Requirement already satisfied: tabulate>=0.9.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.9.0)
Requirement already satisfied: tenacity>=8.3.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (9.1.2)
Requirement already satisfied: termcolor>=3.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (3.1.0)
Requirement already satisfied: typing-extensions>=4.14.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (4.15.0)    
Requirement already satisfied: universal-pathlib!=0.2.4,>=0.2.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.3.2)
Requirement already satisfied: uuid6>=2024.7.10 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2025.0.1)
Requirement already satisfied: fsspec>=2023.10.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-task-sdk==1.1.0->apache-airflow) (2025.9.0)      
Requirement already satisfied: greenback>=1.2.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-task-sdk==1.1.0->apache-airflow) (1.2.1)
Requirement already satisfied: retryhttp!=1.3.0,>=1.2.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-task-sdk==1.1.0->apache-airflow) (1.3.3)
Requirement already satisfied: types-requests>=2.31.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-task-sdk==1.1.0->apache-airflow) (2.32.4.20250913)
Requirement already satisfied: Mako in d:\python\complementos\faculdade\.venv\lib\site-packages (from alembic<2.0,>=1.13.1->apache-airflow-core==3.1.0->apache-airflow) (1.3.10)   
Requirement already satisfied: protobuf<7.0,>=5.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-proto<9999,>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (6.32.1)
Requirement already satisfied: charset_normalizer<4,>=2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from requests<3,>=2.32.0->apache-airflow-core==3.1.0->apache-airflow) (3.4.3)
Requirement already satisfied: idna<4,>=2.5 in d:\python\complementos\faculdade\.venv\lib\site-packages (from requests<3,>=2.32.0->apache-airflow-core==3.1.0->apache-airflow) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from requests<3,>=2.32.0->apache-airflow-core==3.1.0->apache-airflow) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in d:\python\complementos\faculdade\.venv\lib\site-packages (from requests<3,>=2.32.0->apache-airflow-core==3.1.0->apache-airflow) (2025.10.5)
Requirement already satisfied: sqlparse>=0.5.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-providers-common-sql>=1.26.0->apache-airflow-core==3.1.0->apache-airflow) (0.5.3)
Requirement already satisfied: more-itertools>=9.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-providers-common-sql>=1.26.0->apache-airflow-core==3.1.0->apache-airflow) (10.8.0)
Requirement already satisfied: aiosmtplib>=0.1.6 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-providers-smtp>=2.0.2->apache-airflow-core==3.1.0->apache-airflow) (4.0.2)
Requirement already satisfied: typing-inspection>=0.4.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from cadwyn>=5.2.1->apache-airflow-core==3.1.0->apache-airflow) (0.4.2)
Requirement already satisfied: colorama in d:\python\complementos\faculdade\.venv\lib\site-packages (from colorlog>=6.8.2->apache-airflow-core==3.1.0->apache-airflow) (0.4.6)     
Requirement already satisfied: pytz>2021.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from croniter>=2.0.2->apache-airflow-core==3.1.0->apache-airflow) (2025.2)
Requirement already satisfied: cffi>=2.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from cryptography>=41.0.0->apache-airflow-core==3.1.0->apache-airflow) (2.0.0)
Requirement already satisfied: pycparser in d:\python\complementos\faculdade\.venv\lib\site-packages (from cffi>=2.0.0->cryptography>=41.0.0->apache-airflow-core==3.1.0->apache-airflow) (2.23)
Requirement already satisfied: wrapt<2,>=1.10 in d:\python\complementos\faculdade\.venv\lib\site-packages (from deprecated>=1.2.13->apache-airflow-core==3.1.0->apache-airflow) (1.17.3)
Requirement already satisfied: annotated-types>=0.6.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from pydantic>=2.11.0->apache-airflow-core==3.1.0->apache-airflow) (0.7.0)
Requirement already satisfied: pydantic-core==2.33.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from pydantic>=2.11.0->apache-airflow-core==3.1.0->apache-airflow) (2.33.2)
Requirement already satisfied: anyio<5,>=3.6.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from starlette>=0.45.0->apache-airflow-core==3.1.0->apache-airflow) (4.11.0)
Requirement already satisfied: sniffio>=1.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from anyio<5,>=3.6.2->starlette>=0.45.0->apache-airflow-core==3.1.0->apache-airflow) (1.3.1)
Requirement already satisfied: fastapi-cli>=0.0.8 in d:\python\complementos\faculdade\.venv\lib\site-packages (from fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.0.13)
Requirement already satisfied: python-multipart>=0.0.18 in d:\python\complementos\faculdade\.venv\lib\site-packages (from fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.0.20)
Requirement already satisfied: email-validator>=2.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (2.3.0)
Requirement already satisfied: uvicorn>=0.12.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.37.0)
Requirement already satisfied: httpcore==1.* in d:\python\complementos\faculdade\.venv\lib\site-packages (from httpx>=0.25.0->apache-airflow-core==3.1.0->apache-airflow) (1.0.9)  
Requirement already satisfied: h11>=0.16 in d:\python\complementos\faculdade\.venv\lib\site-packages (from httpcore==1.*->httpx>=0.25.0->apache-airflow-core==3.1.0->apache-airflow) (0.16.0)
Requirement already satisfied: dnspython>=2.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from email-validator>=2.0.0->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (2.8.0)
Requirement already satisfied: typer>=0.15.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from fastapi-cli>=0.0.8->fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.19.2)
Requirement already satisfied: rich-toolkit>=0.14.8 in d:\python\complementos\faculdade\.venv\lib\site-packages (from fastapi-cli>=0.0.8->fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.15.1)
Requirement already satisfied: greenlet!=0.4.17 in d:\python\complementos\faculdade\.venv\lib\site-packages (from greenback>=1.2.1->apache-airflow-task-sdk==1.1.0->apache-airflow) (3.2.4)
Requirement already satisfied: outcome in d:\python\complementos\faculdade\.venv\lib\site-packages (from greenback>=1.2.1->apache-airflow-task-sdk==1.1.0->apache-airflow) (1.3.0.post0)
Requirement already satisfied: zipp>=3.20 in d:\python\complementos\faculdade\.venv\lib\site-packages (from importlib-metadata>=7.0->apache-airflow-core==3.1.0->apache-airflow) (3.23.0)
Requirement already satisfied: MarkupSafe>=2.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from jinja2>=3.1.5->apache-airflow-core==3.1.0->apache-airflow) (3.0.3)Requirement already satisfied: jsonschema-specifications>=2023.03.6 in d:\python\complementos\faculdade\.venv\lib\site-packages (from jsonschema>=4.19.1->apache-airflow-core==3.1.0->apache-airflow) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in d:\python\complementos\faculdade\.venv\lib\site-packages (from jsonschema>=4.19.1->apache-airflow-core==3.1.0->apache-airflow) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from jsonschema>=4.19.1->apache-airflow-core==3.1.0->apache-airflow) (0.27.1)
Requirement already satisfied: pyyaml>=5.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from libcst>=1.8.2->apache-airflow-core==3.1.0->apache-airflow) (6.0.3)    
Requirement already satisfied: uc-micro-py in d:\python\complementos\faculdade\.venv\lib\site-packages (from linkify-it-py>=2.0.0->apache-airflow-core==3.1.0->apache-airflow) (1.0.3)
Requirement already satisfied: wirerope>=0.4.7 in d:\python\complementos\faculdade\.venv\lib\site-packages (from methodtools>=0.4.7->apache-airflow-core==3.1.0->apache-airflow) (1.0.0)
Requirement already satisfied: opentelemetry-exporter-otlp-proto-grpc==1.37.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (1.37.0)
Requirement already satisfied: opentelemetry-exporter-otlp-proto-http==1.37.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (1.37.0)
Requirement already satisfied: googleapis-common-protos~=1.57 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (1.70.0)
Requirement already satisfied: grpcio<2.0.0,>=1.63.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (1.75.1)
Requirement already satisfied: opentelemetry-exporter-otlp-proto-common==1.37.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (1.37.0)
Requirement already satisfied: opentelemetry-sdk~=1.37.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (1.37.0)
Requirement already satisfied: opentelemetry-semantic-conventions==0.58b0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-sdk~=1.37.0->opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (0.58b0)
Requirement already satisfied: tzdata>=2020.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from pendulum>=3.1.0->apache-airflow-core==3.1.0->apache-airflow) (2025.2)
Requirement already satisfied: six>=1.5 in d:\python\complementos\faculdade\.venv\lib\site-packages (from python-dateutil>=2.7.0->apache-airflow-core==3.1.0->apache-airflow) (1.17.0)
Requirement already satisfied: text-unidecode>=1.3 in d:\python\complementos\faculdade\.venv\lib\site-packages (from python-slugify>=5.0->apache-airflow-core==3.1.0->apache-airflow) (1.3)
Requirement already satisfied: markdown-it-py>=2.2.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from rich>=13.6.0->apache-airflow-core==3.1.0->apache-airflow) (4.0.0)
Requirement already satisfied: mdurl~=0.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from markdown-it-py>=2.2.0->rich>=13.6.0->apache-airflow-core==3.1.0->apache-airflow) (0.1.2)
Requirement already satisfied: click>=8.1.7 in d:\python\complementos\faculdade\.venv\lib\site-packages (from rich-toolkit>=0.14.8->fastapi-cli>=0.0.8->fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (8.3.0)
Requirement already satisfied: shellingham>=1.3.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from typer>=0.15.1->fastapi-cli>=0.0.8->fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (1.5.4)
Requirement already satisfied: pathlib-abc==0.5.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from universal-pathlib!=0.2.4,>=0.2.2->apache-airflow-core==3.1.0->apache-airflow) (0.5.1)
Requirement already satisfied: httptools>=0.6.3 in d:\python\complementos\faculdade\.venv\lib\site-packages (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.6.4)
Requirement already satisfied: python-dotenv>=0.13 in d:\python\complementos\faculdade\.venv\lib\site-packages (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (1.1.1)
Requirement already satisfied: watchfiles>=0.13 in d:\python\complementos\faculdade\.venv\lib\site-packages (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (1.1.0)
Requirement already satisfied: websockets>=10.4 in d:\python\complementos\faculdade\.venv\lib\site-packages (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (15.0.1)
(.venv) PS D:\Python\complementos\faculdade> 
(.venv) PS D:\Python\complementos\faculdade> pip install apache-airflow
Requirement already satisfied: apache-airflow in d:\python\complementos\faculdade\.venv\lib\site-packages (3.1.0)
Requirement already satisfied: apache-airflow-core==3.1.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow) (3.1.0)
Requirement already satisfied: apache-airflow-task-sdk==1.1.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow) (1.1.0)
Requirement already satisfied: natsort>=8.4.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow) (8.4.0)
Requirement already satisfied: a2wsgi>=1.10.8 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.10.10)
Requirement already satisfied: aiosqlite>=0.20.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.21.0)
Requirement already satisfied: alembic<2.0,>=1.13.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.16.5)
Requirement already satisfied: apache-airflow-providers-common-compat>=1.6.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.7.4)
Requirement already satisfied: apache-airflow-providers-common-io>=1.5.3 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.6.3)
Requirement already satisfied: apache-airflow-providers-common-sql>=1.26.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.28.1)
Requirement already satisfied: apache-airflow-providers-smtp>=2.0.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.3.1)
Requirement already satisfied: apache-airflow-providers-standard>=0.4.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.9.0)
Requirement already satisfied: argcomplete>=1.10 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (3.6.2)
Requirement already satisfied: asgiref>=2.3.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (3.10.0)
Requirement already satisfied: attrs!=25.2.0,>=22.1.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (25.4.0)       
Requirement already satisfied: cadwyn>=5.2.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (5.4.4)
Requirement already satisfied: colorlog>=6.8.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (6.9.0)
Requirement already satisfied: cron-descriptor>=1.2.24 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.0.6)       
Requirement already satisfied: croniter>=2.0.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (6.0.0)
Requirement already satisfied: cryptography>=41.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (46.0.2)
Requirement already satisfied: deprecated>=1.2.13 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.2.18)
Requirement already satisfied: dill>=0.2.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.4.0)
Requirement already satisfied: fastapi>=0.116.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.118.0)
Requirement already satisfied: httpx>=0.25.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.28.1)
Requirement already satisfied: importlib-metadata>=7.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (8.7.0)       
Requirement already satisfied: itsdangerous>=2.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.2.0)
Requirement already satisfied: jinja2>=3.1.5 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (3.1.6)
Requirement already satisfied: jsonschema>=4.19.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (4.25.1)
Requirement already satisfied: lazy-object-proxy>=1.2.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.12.0)     
Requirement already satisfied: libcst>=1.8.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.8.5)
Requirement already satisfied: linkify-it-py>=2.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.0.3)
Requirement already satisfied: lockfile>=0.12.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.12.2)
Requirement already satisfied: methodtools>=0.4.7 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.4.7)
Requirement already satisfied: msgspec>=0.19.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.19.0)
Requirement already satisfied: opentelemetry-api>=1.27.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.37.0)    
Requirement already satisfied: opentelemetry-exporter-otlp>=1.27.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.37.0)
Requirement already satisfied: opentelemetry-proto<9999,>=1.27.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.37.0)
Requirement already satisfied: packaging>=25.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (25.0)
Requirement already satisfied: pathspec>=0.9.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.12.1)
Requirement already satisfied: pendulum>=3.1.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (3.1.0)
Requirement already satisfied: pluggy>=1.5.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.6.0)
Requirement already satisfied: psutil>=5.8.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (7.1.0)
Requirement already satisfied: pydantic>=2.11.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.11.10)
Requirement already satisfied: pygments!=2.19.0,>=2.0.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.19.2)     
Requirement already satisfied: pygtrie>=2.5.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.5.0)
Requirement already satisfied: pyjwt>=2.10.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.10.1)
Requirement already satisfied: python-daemon>=3.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (3.1.2)
Requirement already satisfied: python-dateutil>=2.7.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.9.0.post0)  
Requirement already satisfied: python-slugify>=5.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (8.0.4)
Requirement already satisfied: requests<3,>=2.32.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2.32.5)
Requirement already satisfied: rich-argparse>=1.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.7.1)
Requirement already satisfied: rich>=13.6.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (14.1.0)
Requirement already satisfied: setproctitle>=1.3.3 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.3.7)
Requirement already satisfied: sqlalchemy-jsonfield>=1.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (1.0.2)     
Requirement already satisfied: sqlalchemy-utils>=0.41.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.42.0)     
Requirement already satisfied: sqlalchemy>=1.4.49 in d:\python\complementos\faculdade\.venv\lib\site-packages (from sqlalchemy[asyncio]>=1.4.49->apache-airflow-core==3.1.0->apache-airflow) (2.0.43)
Requirement already satisfied: starlette>=0.45.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.48.0)
Requirement already satisfied: structlog>=25.4.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (25.4.0)
Requirement already satisfied: svcs>=25.1.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (25.1.0)
Requirement already satisfied: tabulate>=0.9.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.9.0)
Requirement already satisfied: tenacity>=8.3.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (9.1.2)
Requirement already satisfied: termcolor>=3.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (3.1.0)
Requirement already satisfied: typing-extensions>=4.14.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (4.15.0)    
Requirement already satisfied: universal-pathlib!=0.2.4,>=0.2.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (0.3.2)
Requirement already satisfied: uuid6>=2024.7.10 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-core==3.1.0->apache-airflow) (2025.0.1)
Requirement already satisfied: fsspec>=2023.10.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-task-sdk==1.1.0->apache-airflow) (2025.9.0)
Requirement already satisfied: greenback>=1.2.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-task-sdk==1.1.0->apache-airflow) (1.2.1)
Requirement already satisfied: retryhttp!=1.3.0,>=1.2.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-task-sdk==1.1.0->apache-airflow) (1.3.3)  
Requirement already satisfied: types-requests>=2.31.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-task-sdk==1.1.0->apache-airflow) (2.32.4.20250913)
Requirement already satisfied: Mako in d:\python\complementos\faculdade\.venv\lib\site-packages (from alembic<2.0,>=1.13.1->apache-airflow-core==3.1.0->apache-airflow) (1.3.10)
Requirement already satisfied: protobuf<7.0,>=5.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-proto<9999,>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (6.32.1)
Requirement already satisfied: charset_normalizer<4,>=2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from requests<3,>=2.32.0->apache-airflow-core==3.1.0->apache-airflow) (3.4.3)
Requirement already satisfied: idna<4,>=2.5 in d:\python\complementos\faculdade\.venv\lib\site-packages (from requests<3,>=2.32.0->apache-airflow-core==3.1.0->apache-airflow) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from requests<3,>=2.32.0->apache-airflow-core==3.1.0->apache-airflow) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in d:\python\complementos\faculdade\.venv\lib\site-packages (from requests<3,>=2.32.0->apache-airflow-core==3.1.0->apache-airflow) (2025.10.5)
Requirement already satisfied: sqlparse>=0.5.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-providers-common-sql>=1.26.0->apache-airflow-core==3.1.0->apache-airflow) (0.5.3)
Requirement already satisfied: more-itertools>=9.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-providers-common-sql>=1.26.0->apache-airflow-core==3.1.0->apache-airflow) (10.8.0)
Requirement already satisfied: aiosmtplib>=0.1.6 in d:\python\complementos\faculdade\.venv\lib\site-packages (from apache-airflow-providers-smtp>=2.0.2->apache-airflow-core==3.1.0->apache-airflow) (4.0.2)
Requirement already satisfied: typing-inspection>=0.4.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from cadwyn>=5.2.1->apache-airflow-core==3.1.0->apache-airflow) (0.4.2)
Requirement already satisfied: colorama in d:\python\complementos\faculdade\.venv\lib\site-packages (from colorlog>=6.8.2->apache-airflow-core==3.1.0->apache-airflow) (0.4.6)
Requirement already satisfied: pytz>2021.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from croniter>=2.0.2->apache-airflow-core==3.1.0->apache-airflow) (2025.2) 
Requirement already satisfied: cffi>=2.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from cryptography>=41.0.0->apache-airflow-core==3.1.0->apache-airflow) (2.0.0)
Requirement already satisfied: pycparser in d:\python\complementos\faculdade\.venv\lib\site-packages (from cffi>=2.0.0->cryptography>=41.0.0->apache-airflow-core==3.1.0->apache-airflow) (2.23)
Requirement already satisfied: wrapt<2,>=1.10 in d:\python\complementos\faculdade\.venv\lib\site-packages (from deprecated>=1.2.13->apache-airflow-core==3.1.0->apache-airflow) (1.17.3)
Requirement already satisfied: annotated-types>=0.6.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from pydantic>=2.11.0->apache-airflow-core==3.1.0->apache-airflow) (0.7.0)
Requirement already satisfied: pydantic-core==2.33.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from pydantic>=2.11.0->apache-airflow-core==3.1.0->apache-airflow) (2.33.2)
Requirement already satisfied: anyio<5,>=3.6.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from starlette>=0.45.0->apache-airflow-core==3.1.0->apache-airflow) (4.11.0)
Requirement already satisfied: sniffio>=1.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from anyio<5,>=3.6.2->starlette>=0.45.0->apache-airflow-core==3.1.0->apache-airflow) (1.3.1)
Requirement already satisfied: fastapi-cli>=0.0.8 in d:\python\complementos\faculdade\.venv\lib\site-packages (from fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.0.13)
Requirement already satisfied: python-multipart>=0.0.18 in d:\python\complementos\faculdade\.venv\lib\site-packages (from fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.0.20)
Requirement already satisfied: email-validator>=2.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (2.3.0)
Requirement already satisfied: uvicorn>=0.12.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.37.0)
Requirement already satisfied: httpcore==1.* in d:\python\complementos\faculdade\.venv\lib\site-packages (from httpx>=0.25.0->apache-airflow-core==3.1.0->apache-airflow) (1.0.9)  
Requirement already satisfied: h11>=0.16 in d:\python\complementos\faculdade\.venv\lib\site-packages (from httpcore==1.*->httpx>=0.25.0->apache-airflow-core==3.1.0->apache-airflow) (0.16.0)
Requirement already satisfied: dnspython>=2.0.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from email-validator>=2.0.0->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (2.8.0)
Requirement already satisfied: typer>=0.15.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from fastapi-cli>=0.0.8->fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.19.2)
Requirement already satisfied: rich-toolkit>=0.14.8 in d:\python\complementos\faculdade\.venv\lib\site-packages (from fastapi-cli>=0.0.8->fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.15.1)
Requirement already satisfied: greenlet!=0.4.17 in d:\python\complementos\faculdade\.venv\lib\site-packages (from greenback>=1.2.1->apache-airflow-task-sdk==1.1.0->apache-airflow) (3.2.4)
Requirement already satisfied: outcome in d:\python\complementos\faculdade\.venv\lib\site-packages (from greenback>=1.2.1->apache-airflow-task-sdk==1.1.0->apache-airflow) (1.3.0.post0)
Requirement already satisfied: zipp>=3.20 in d:\python\complementos\faculdade\.venv\lib\site-packages (from importlib-metadata>=7.0->apache-airflow-core==3.1.0->apache-airflow) (3.23.0)
Requirement already satisfied: MarkupSafe>=2.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from jinja2>=3.1.5->apache-airflow-core==3.1.0->apache-airflow) (3.0.3)Requirement already satisfied: jsonschema-specifications>=2023.03.6 in d:\python\complementos\faculdade\.venv\lib\site-packages (from jsonschema>=4.19.1->apache-airflow-core==3.1.0->apache-airflow) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in d:\python\complementos\faculdade\.venv\lib\site-packages (from jsonschema>=4.19.1->apache-airflow-core==3.1.0->apache-airflow) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from jsonschema>=4.19.1->apache-airflow-core==3.1.0->apache-airflow) (0.27.1)
Requirement already satisfied: pyyaml>=5.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from libcst>=1.8.2->apache-airflow-core==3.1.0->apache-airflow) (6.0.3)    
Requirement already satisfied: uc-micro-py in d:\python\complementos\faculdade\.venv\lib\site-packages (from linkify-it-py>=2.0.0->apache-airflow-core==3.1.0->apache-airflow) (1.0.3)
Requirement already satisfied: wirerope>=0.4.7 in d:\python\complementos\faculdade\.venv\lib\site-packages (from methodtools>=0.4.7->apache-airflow-core==3.1.0->apache-airflow) (1.0.0)
Requirement already satisfied: opentelemetry-exporter-otlp-proto-grpc==1.37.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (1.37.0)
Requirement already satisfied: opentelemetry-exporter-otlp-proto-http==1.37.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (1.37.0)
Requirement already satisfied: googleapis-common-protos~=1.57 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (1.70.0)
Requirement already satisfied: grpcio<2.0.0,>=1.63.2 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (1.75.1)
Requirement already satisfied: opentelemetry-exporter-otlp-proto-common==1.37.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (1.37.0)
Requirement already satisfied: opentelemetry-sdk~=1.37.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (1.37.0)
Requirement already satisfied: opentelemetry-semantic-conventions==0.58b0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from opentelemetry-sdk~=1.37.0->opentelemetry-exporter-otlp-proto-grpc==1.37.0->opentelemetry-exporter-otlp>=1.27.0->apache-airflow-core==3.1.0->apache-airflow) (0.58b0)
Requirement already satisfied: tzdata>=2020.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from pendulum>=3.1.0->apache-airflow-core==3.1.0->apache-airflow) (2025.2)
Requirement already satisfied: six>=1.5 in d:\python\complementos\faculdade\.venv\lib\site-packages (from python-dateutil>=2.7.0->apache-airflow-core==3.1.0->apache-airflow) (1.17.0)
Requirement already satisfied: text-unidecode>=1.3 in d:\python\complementos\faculdade\.venv\lib\site-packages (from python-slugify>=5.0->apache-airflow-core==3.1.0->apache-airflow) (1.3)
Requirement already satisfied: markdown-it-py>=2.2.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from rich>=13.6.0->apache-airflow-core==3.1.0->apache-airflow) (4.0.0)
Requirement already satisfied: mdurl~=0.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from markdown-it-py>=2.2.0->rich>=13.6.0->apache-airflow-core==3.1.0->apache-airflow) (0.1.2)
Requirement already satisfied: click>=8.1.7 in d:\python\complementos\faculdade\.venv\lib\site-packages (from rich-toolkit>=0.14.8->fastapi-cli>=0.0.8->fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (8.3.0)
Requirement already satisfied: shellingham>=1.3.0 in d:\python\complementos\faculdade\.venv\lib\site-packages (from typer>=0.15.1->fastapi-cli>=0.0.8->fastapi-cli[standard-no-fastapi-cloud-cli]>=0.0.8; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (1.5.4)
Requirement already satisfied: pathlib-abc==0.5.1 in d:\python\complementos\faculdade\.venv\lib\site-packages (from universal-pathlib!=0.2.4,>=0.2.2->apache-airflow-core==3.1.0->apache-airflow) (0.5.1)
Requirement already satisfied: httptools>=0.6.3 in d:\python\complementos\faculdade\.venv\lib\site-packages (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (0.6.4)
Requirement already satisfied: python-dotenv>=0.13 in d:\python\complementos\faculdade\.venv\lib\site-packages (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (1.1.1)
Requirement already satisfied: watchfiles>=0.13 in d:\python\complementos\faculdade\.venv\lib\site-packages (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (1.1.0)
Requirement already satisfied: websockets>=10.4 in d:\python\complementos\faculdade\.venv\lib\site-packages (from uvicorn[standard]>=0.12.0; extra == "standard-no-fastapi-cloud-cli"->fastapi[standard-no-fastapi-cloud-cli]>=0.116.0->apache-airflow-core==3.1.0->apache-airflow) (15.0.1)
(.venv) PS D:\Python\complementos\faculdade> python "Criando DAGs.py"  
D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__init__.py:45: RuntimeWarning: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly tested on fairly modern Linux Distros and recent versions of macOS. On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers. The work to add Windows support is tracked via https://github.com/apache/airflow/issues/10388, but it is not a high priority.
  warnings.warn(
(.venv) PS D:\Python\complementos\faculdade> export AIFLOW_HOME=D:/Python/complementos/faculdade
export : O termo 'export' não é reconhecido como nome de cmdlet, função, arquivo de script ou programa operável. Verifique a grafia do nome ou, se um caminho tiver sido 
incluído, veja se o caminho está correto e tente novamente.
No linha:1 caractere:1
+ export AIFLOW_HOME=D:/Python/complementos/faculdade
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (export:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
(.venv) PS D:\Python\complementos\faculdade> $env:AIRFLOW_HOME = "D:/Python/complementos/faculdade"
(.venv) PS D:\Python\complementos\faculdade> echo $env:AIRFLOW_HOME
D:/Python/complementos/faculdade
(.venv) PS D:\Python\complementos\faculdade> airflow standalone
D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__init__.py:45: RuntimeWarning: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly tested on fairly modern Linux Distros and recent versions of macOS. On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers. The work to add Windows support is tracked via https://github.com/apache/airflow/issues/10388, but it is not a high priority.
  warnings.warn(
2025-10-07T02:19:33.239739Z [warning  ] No module named 'fcntl'        [airflow.configuration] loc=configuration.py:1266
2025-10-07T02:19:33.240698Z [warning  ] cannot load CLI commands from auth manager: The object could not be loaded. Please check "auth_manager" key in "core" section. Current value: "airflow.api_fastapi.auth.managers.simple.simple_auth_manager.SimpleAuthManager". [airflow.cli.cli_parser] loc=cli_parser.py:81
2025-10-07T02:19:33.241695Z [warning  ] Auth manager is not configured and api-server will not be able to start. [airflow.cli.cli_parser] loc=cli_parser.py:82
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "D:\Python\complementos\faculdade\.venv\Scripts\airflow.exe\__main__.py", line 6, in <module>
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__main__.py", line 55, in main
    args.func(args)
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\cli\cli_config.py", line 48, in command
    func = import_string(import_path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\module_loading.py", line 41, in import_string
    module = import_module(module_path)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Acer\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\cli\commands\standalone_command.py", line 36, in <module>
    from airflow.jobs.scheduler_job_runner import SchedulerJobRunner
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\jobs\scheduler_job_runner.py", line 50, in <module>
    from airflow.dag_processing.bundles.base import BundleUsageTrackingManager
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\dag_processing\bundles\base.py", line 20, in <module>
    import fcntl
ModuleNotFoundError: No module named 'fcntl'
(.venv) PS D:\Python\complementos\faculdade> Get-ChildItem Env:AIRFLOW_HOME

Name                           Value
----                           -----
AIRFLOW_HOME                   D:/Python/complementos/faculdade


(.venv) PS D:\Python\complementos\faculdade> airflow db init   
D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__init__.py:45: RuntimeWarning: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly tested on fairly modern Linux Distros and recent versions of macOS. On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers. The work to add Windows support is tracked via https://github.com/apache/airflow/issues/10388, but it is not a high priority.
  warnings.warn(
2025-10-07T02:20:15.030221Z [warning  ] No module named 'fcntl'        [airflow.configuration] loc=configuration.py:1266
2025-10-07T02:20:15.031218Z [warning  ] cannot load CLI commands from auth manager: The object could not be loaded. Please check "auth_manager" key in "core" section. Current value: "airflow.api_fastapi.auth.managers.simple.simple_auth_manager.SimpleAuthManager". [airflow.cli.cli_parser] loc=cli_parser.py:81
2025-10-07T02:20:15.032218Z [warning  ] Auth manager is not configured and api-server will not be able to start. [airflow.cli.cli_parser] loc=cli_parser.py:82
Usage: airflow db [-h] COMMAND ...

Database operations

Positional Arguments:
  COMMAND
    check           Check if the database can be reached
    check-migrations
                    Check if migration have finished
    clean           Purge old records in metastore tables
    downgrade       Downgrade the schema of the metadata database.
    drop-archived   Drop archived tables created through the db clean command
    export-archived
                    Export archived data from the archive tables
    migrate         Migrates the metadata database to the latest version
    reset           Burn down and rebuild the metadata database
    shell           Runs a shell to access the database

Options:
  -h, --help        show this help message and exit

airflow db command error: argument COMMAND: invalid choice: 'init' (choose from 'check', 'check-migrations', 'clean', 'downgrade', 'drop-archived', 'export-archived', 'migrate', 'reset', 'shell'), see help above.
(.venv) PS D:\Python\complementos\faculdade> airflow db migrate
D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__init__.py:45: RuntimeWarning: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly tested on fairly modern Linux Distros and recent versions of macOS. On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers. The work to add Windows support is tracked via https://github.com/apache/airflow/issues/10388, but it is not a high priority.
  warnings.warn(
2025-10-07T02:20:36.186150Z [warning  ] No module named 'fcntl'        [airflow.configuration] loc=configuration.py:1266
2025-10-07T02:20:36.187158Z [warning  ] cannot load CLI commands from auth manager: The object could not be loaded. Please check "auth_manager" key in "core" section. Current value: "airflow.api_fastapi.auth.managers.simple.simple_auth_manager.SimpleAuthManager". [airflow.cli.cli_parser] loc=cli_parser.py:81
2025-10-07T02:20:36.188144Z [warning  ] Auth manager is not configured and api-server will not be able to start. [airflow.cli.cli_parser] loc=cli_parser.py:82
DB: sqlite:///D:/Python/complementos/faculdade/airflow.db
Performing upgrade to the metadata database sqlite:///D:/Python/complementos/faculdade/airflow.db
2025-10-07T02:20:37.517144Z [info     ] Context impl SQLiteImpl.       [alembic.runtime.migration] loc=migration.py:211
2025-10-07T02:20:37.518107Z [info     ] Will assume non-transactional DDL. [alembic.runtime.migration] loc=migration.py:214
2025-10-07T02:20:37.521103Z [warning  ] No module named 'fcntl'        [airflow.configuration] loc=configuration.py:1266
Traceback (most recent call last):
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\configuration.py", line 1264, in getimport
    return import_string(full_qualified_path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\module_loading.py", line 41, in import_string
    module = import_module(module_path)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Acer\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\api_fastapi\auth\managers\simple\simple_auth_manager.py", line 20, in <module>
    import fcntl
ModuleNotFoundError: No module named 'fcntl'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "D:\Python\complementos\faculdade\.venv\Scripts\airflow.exe\__main__.py", line 6, in <module>
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__main__.py", line 55, in main
    args.func(args)
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\cli\cli_config.py", line 49, in command
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\cli.py", line 114, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\providers_configuration_loader.py", line 54, in wrapped_function
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\cli\commands\db_command.py", line 207, in migratedb
    run_db_migrate_command(args, db.upgradedb, _REVISION_HEADS_MAP)
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\cli\commands\db_command.py", line 135, in run_db_migrate_command
    command(
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\session.py", line 100, in wrapper
    return func(*args, session=session, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\db.py", line 1124, in upgradedb
    initdb(session=session)
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\session.py", line 98, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\db.py", line 740, in initdb
    external_db_manager = RunDBManager()
                          ^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\db_manager.py", line 157, in __init__
    auth_manager_db_manager = create_auth_manager().get_db_manager()
                              ^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\api_fastapi\app.py", line 141, in create_auth_manager
    auth_manager_cls = get_auth_manager_cls()
                       ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\api_fastapi\app.py", line 128, in get_auth_manager_cls
    auth_manager_cls = conf.getimport(section="core", key="auth_manager")
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\configuration.py", line 1267, in getimport
    raise AirflowConfigException(
airflow.exceptions.AirflowConfigException: The object could not be loaded. Please check "auth_manager" key in "core" section. Current value: "airflow.api_fastapi.auth.managers.simple.simple_auth_manager.SimpleAuthManager".
(.venv) PS D:\Python\complementos\faculdade> airflow db migrate
D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__init__.py:45: RuntimeWarning: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly tested on fairly modern Linux Distros and recent versions of macOS. On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers. The work to add Windows support is tracked via https://github.com/apache/airflow/issues/10388, but it is not a high priority.
  warnings.warn(
2025-10-07T02:21:56.460260Z [warning  ] No module named 'fcntl'        [airflow.configuration] loc=configuration.py:1266
2025-10-07T02:21:56.461259Z [warning  ] cannot load CLI commands from auth manager: The object could not be loaded. Please check "auth_manager" key in "core" section. Current value: "airflow.api_fastapi.auth.managers.simple.simple_auth_manager.SimpleAuthManager". [airflow.cli.cli_parser] loc=cli_parser.py:81
2025-10-07T02:21:56.462221Z [warning  ] Auth manager is not configured and api-server will not be able to start. [airflow.cli.cli_parser] loc=cli_parser.py:82
DB: sqlite:///D:/Python/complementos/faculdade/airflow.db
Performing upgrade to the metadata database sqlite:///D:/Python/complementos/faculdade/airflow.db
2025-10-07T02:21:56.956064Z [info     ] Context impl SQLiteImpl.       [alembic.runtime.migration] loc=migration.py:211
2025-10-07T02:21:56.956799Z [info     ] Will assume non-transactional DDL. [alembic.runtime.migration] loc=migration.py:214
2025-10-07T02:21:56.959798Z [warning  ] No module named 'fcntl'        [airflow.configuration] loc=configuration.py:1266
Traceback (most recent call last):
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\configuration.py", line 1264, in getimport
    return import_string(full_qualified_path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\module_loading.py", line 41, in import_string
    module = import_module(module_path)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Acer\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\api_fastapi\auth\managers\simple\simple_auth_manager.py", line 20, in <module>
    import fcntl
ModuleNotFoundError: No module named 'fcntl'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "D:\Python\complementos\faculdade\.venv\Scripts\airflow.exe\__main__.py", line 6, in <module>
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__main__.py", line 55, in main
    args.func(args)
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\cli\cli_config.py", line 49, in command
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\cli.py", line 114, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\providers_configuration_loader.py", line 54, in wrapped_function
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\cli\commands\db_command.py", line 207, in migratedb
    run_db_migrate_command(args, db.upgradedb, _REVISION_HEADS_MAP)
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\cli\commands\db_command.py", line 135, in run_db_migrate_command
    command(
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\session.py", line 100, in wrapper
    return func(*args, session=session, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\db.py", line 1124, in upgradedb
    initdb(session=session)
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\session.py", line 98, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\db.py", line 740, in initdb
    external_db_manager = RunDBManager()
                          ^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\db_manager.py", line 157, in __init__
    auth_manager_db_manager = create_auth_manager().get_db_manager()
                              ^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\api_fastapi\app.py", line 141, in create_auth_manager
    auth_manager_cls = get_auth_manager_cls()
                       ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\api_fastapi\app.py", line 128, in get_auth_manager_cls
    auth_manager_cls = conf.getimport(section="core", key="auth_manager")
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\configuration.py", line 1267, in getimport
    raise AirflowConfigException(
airflow.exceptions.AirflowConfigException: The object could not be loaded. Please check "auth_manager" key in "core" section. Current value: "airflow.api_fastapi.auth.managers.simple.simple_auth_manager.SimpleAuthManager".
(.venv) PS D:\Python\complementos\faculdade> $env:AIRFLOW__CORE__AUTH_MANAGER = ""; airflow db migrate
D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__init__.py:45: RuntimeWarning: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly tested on fairly modern Linux Distros and recent versions of macOS. On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers. The work to add Windows support is tracked via https://github.com/apache/airflow/issues/10388, but it is not a high priority.
  warnings.warn(
2025-10-07T02:22:53.919659Z [warning  ] No module named 'fcntl'        [airflow.configuration] loc=configuration.py:1266
2025-10-07T02:22:53.920825Z [warning  ] cannot load CLI commands from auth manager: The object could not be loaded. Please check "auth_manager" key in "core" section. Current value: "airflow.api_fastapi.auth.managers.simple.simple_auth_manager.SimpleAuthManager". [airflow.cli.cli_parser] loc=cli_parser.py:81
2025-10-07T02:22:53.921826Z [warning  ] Auth manager is not configured and api-server will not be able to start. [airflow.cli.cli_parser] loc=cli_parser.py:82
DB: sqlite:///D:/Python/complementos/faculdade/airflow.db
Performing upgrade to the metadata database sqlite:///D:/Python/complementos/faculdade/airflow.db
2025-10-07T02:22:54.414594Z [info     ] Context impl SQLiteImpl.       [alembic.runtime.migration] loc=migration.py:211
2025-10-07T02:22:54.414594Z [info     ] Will assume non-transactional DDL. [alembic.runtime.migration] loc=migration.py:214
2025-10-07T02:22:54.417588Z [warning  ] No module named 'fcntl'        [airflow.configuration] loc=configuration.py:1266
Traceback (most recent call last):
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\configuration.py", line 1264, in getimport
    return import_string(full_qualified_path)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\module_loading.py", line 41, in import_string
    module = import_module(module_path)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Acer\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\api_fastapi\auth\managers\simple\simple_auth_manager.py", line 20, in <module>
    import fcntl
ModuleNotFoundError: No module named 'fcntl'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "D:\Python\complementos\faculdade\.venv\Scripts\airflow.exe\__main__.py", line 6, in <module>
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\__main__.py", line 55, in main
    args.func(args)
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\cli\cli_config.py", line 49, in command
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\cli.py", line 114, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\providers_configuration_loader.py", line 54, in wrapped_function
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\cli\commands\db_command.py", line 207, in migratedb
    run_db_migrate_command(args, db.upgradedb, _REVISION_HEADS_MAP)
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\cli\commands\db_command.py", line 135, in run_db_migrate_command
    command(
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\session.py", line 100, in wrapper
    return func(*args, session=session, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\db.py", line 1124, in upgradedb
    initdb(session=session)
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\session.py", line 98, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\db.py", line 740, in initdb
    external_db_manager = RunDBManager()
                          ^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\utils\db_manager.py", line 157, in __init__
    auth_manager_db_manager = create_auth_manager().get_db_manager()
                              ^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\api_fastapi\app.py", line 141, in create_auth_manager
    auth_manager_cls = get_auth_manager_cls()
                       ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\api_fastapi\app.py", line 128, in get_auth_manager_cls
    auth_manager_cls = conf.getimport(section="core", key="auth_manager")
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python\complementos\faculdade\.venv\Lib\site-packages\airflow\configuration.py", line 1267, in getimport
    raise AirflowConfigException(
airflow.exceptions.AirflowConfigException: The object could not be loaded. Please check "auth_manager" key in "core" section. Current value: "airflow.api_fastapi.auth.managers.simple.simple_auth_manager.SimpleAuthManager".
(.venv) PS D:\Python\complementos\faculdade> 
