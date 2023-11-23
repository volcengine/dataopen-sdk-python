# openapi 使用说明

## Client 参数说明

| 字段       | 类型            | 默认值                                | 含义                                                |
| ---------- | --------------- | ------------------------------------- | --------------------------------------------------- |
| app_id     | str             | 无                                    | 应用的唯一标识符                                    |
| app_secret | str             | 无                                    | 用于应用的安全认证的密钥                            |
| url        | str or NoneType | "https://analytics.volcengineapi.com" | 服务器的 URL 地址                                   |
| env        | str or NoneType | "dataopen"                            | 环境设置，可选值为 "dataopen" 或 "dataopen_staging" |
| expiration | str or NoneType | "1800"                                | 过期时间，单位是秒                                  |

## client.request 参数说明

| 字段        | 类型           | 默认值 | 含义                                            |
| ----------- | -------------- | ------ | ----------------------------------------------- |
| service_url | str            | 无     | 请求的服务 URL 地址                             |
| method      | str            | 无     | 请求的 HTTP 方法，例如 "GET", "POST" 等         |
| headers     | Dict[str, str] | {}     | 请求头，包含的信息如认证凭据，内容类型等        |
| params      | Dict[str, any] | {}     | URL 参数，用于 GET 请求                         |
| body        | Dict[str, any] | {}     | 请求体，通常在 POST 或 PUT 请求中包含发送的数据 |

## 样例

### 1、Get 方法

```python
from dataopen import Client, ParamsValueType

app_id = ""
app_secret = ""

dataopen_client = Client(app_id, app_secret)

headers = {}

params: dict[str, ParamsValueType] = {
    "app": 46,
    "page_size": 1,
    "page": 1,
}

body = {}

res = dataopen_client.request("/xxx/openapi/v1/open/flight-list", "GET", headers, params, body)
print("\n\nOutput: ", res)
```

### 2、Post 方法

```python
from dataopen import Client, ParamsValueType

app_id = ""
app_secret = ""

dataopen_client = Client(app_id, app_secret)

headers = {}

params = {}

body: dict[str, any] = {
    "uid_list": ["1111111110000"],
}

res = dataopen_client.request(
    "/xxx/openapi/v1/open/flight/version/6290880/add-test-user",
    "POST",
    headers,
    params,
    body,
)

# Output results
print("\n\nOutput: ", res)
```
