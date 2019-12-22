# Configuración Wifi

Los cambios que hagamos en la configuración del Wifi mediante el applet del escritorio se trasladan al fichero

```
/etc/wpa_supplicant/wpa_supplicant.conf
```

Si lo abrimos veremos que tenemos un definición por cada red

Para editarlo tenemos que usar sudo

```
sudo geany /etc/wpa_supplicant/wpa_supplicant.conf
```

Una entrada normal tiene el formato


```
network={
	ssid="SSID_RED"
	psk="PASSWORD"
	key_mgmt=WPA-PSK
}
```


Para eduroam sería

```
network={
	ssid="eduroam"
	proto=RSN
	key_mgmt=WPA-EAP
	pairwise=CCMP
	auth_alg=OPEN
	eap=PEAP
	identity="email@correo.ugr.es"
	password="PASSWORD"
	phase1="peaplabel=0"
	phase2="auth=MSCHAPV2"
	priority=999
	proactive_key_caching=1
	disabled=1
}

```

Para que los cambios se usen haremos

```
sudo service networking stop 
sudo wpa_supplicant -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf -B
```

[Tutorial sobre eduroam](https://autottblog.wordpress.com/raspberry-pi-arduino/connecting-raspberry-pi-to-eduroam/)

## Creando un hotspot

[Creando un Hotspot con Raspberry](https://descubrearduino.com/raspberry-pi-como-punto-de-acceso-inalambrico/)
