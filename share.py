from pyngrok import ngrok

public_url = ngrok.connect(8000)

print("Public URL:")
print(public_url)