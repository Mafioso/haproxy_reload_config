#!/bin/bash
sudo cp /opt/haproxy_reload/haproxy_reload/proxy_list.cfg /etc/haproxy/
sudo haproxy -f /etc/haproxy/haproxy.cfg -f /etc/haproxy/proxy_list.cfg -p /var/run/haproxy.pid -sf $(cat /var/run/haproxy.pid)

