"""
代理配置模块 - 统一处理本地服务的代理设置
"""
import os


def configure_proxy():
    """
    配置代理设置，确保本地服务（localhost/127.0.0.1）直连，不经过代理
    从环境变量读取代理配置，允许自定义
    """
    # 设置 NO_PROXY 确保本地服务直连
    no_proxy = os.getenv('NO_PROXY', 'localhost,127.0.0.1')
    os.environ['NO_PROXY'] = no_proxy

    # 如果环境变量中明确设置了代理为空，则删除代理变量
    # 这允许用户在 .env 中通过设置 HTTP_PROXY= 来禁用代理
    proxy_vars = ['HTTP_PROXY', 'http_proxy', 'HTTPS_PROXY', 'https_proxy']

    for proxy_var in proxy_vars:
        # 如果环境变量存在但值为空，删除它
        if proxy_var in os.environ and not os.environ[proxy_var]:
            del os.environ[proxy_var]

    # 打印当前代理配置（调试用）
    if os.getenv('DEBUG'):
        print("🔧 Proxy Configuration:")
        print(f"   NO_PROXY: {os.environ.get('NO_PROXY', 'Not set')}")
        for proxy_var in proxy_vars:
            value = os.environ.get(proxy_var, 'Not set')
            print(f"   {proxy_var}: {value}")


# 模块导入时自动执行配置
configure_proxy()
