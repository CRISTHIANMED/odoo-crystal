server {
    listen 443 ssl;
    server_name www.crystalitservice.com;

    proxy_read_timeout 720s;
    proxy_connect_timeout 720s;
    proxy_send_timeout 720s;

    location / {
        proxy_pass http://localhost:8069;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}

server {
    listen 443 ssl;
    server_name crystalitservice.com;

    return 301 https://www.crystalitservice.com$request_uri;
}

server {
    listen 80;
    server_name crystalitservice.com www.crystalitservice.com;

    return 301 https://www.crystalitservice.com$request_uri;
}
