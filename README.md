Website to host/manage photo's

Build docker image:  
```docker build --no-cache .```

Push docker image:  
```docker push mahulst/buurman```

Run:
```docker run -v /data/buurman:/data/buurman -p 8000:8000 mahulst/buurman:latest```