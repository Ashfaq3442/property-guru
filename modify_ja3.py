from mitmproxy import tls

def tls_client_hello(data: tls.ClientHelloData):
    print(f"Original Ciphers: {data.client_hello.ciphers}")
    data.client_hello.ciphers = [0x1301, 0x1302, 0x1303]  # Modify ciphers
    print(f"Modified Ciphers: {data.client_hello.ciphers}")
