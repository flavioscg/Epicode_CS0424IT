# Consegna S1/L2

Richiesta:

*Scrivere per i seguenti IP: IP Network, IP Gateway ‘convenzionale’, IP Broadcast, quali e quanti ottetti per gli host, quanti e quali per la network.*


	  1.1.1.1/8
      128.1.6.5/12 
      200.1.2.3/24.
      192.192.1.1/22
      126.5.4.3/9
  	  200.1.9.8/24
      172.16.0.4/16


## 1.1.1.1/8

|          | Decimale | Binario            |
|----------|----------|--------------------|
| **IP**   | 1.1.1.1 | 00000001.00000001.00000001.00000001 |
| **Subnet mask** | 255.0.0.0 | 11111111.00000000.00000000.00000000 |

Applicando ad esempio il metodo dell'operatore logico AND, otteniamo come risultato:

00000001.00000000.00000000.00000000

ovvero: 1.0.0.0 in decimale.

Oppure settare tutti i bit a 0 dopo i primi 8bit (in questo caso).

Quindi:

    Network ip: 1.0.0.0/8
    
    Gateway ip: 1.0.0.1
   
    Considerando ancora il binario dell'indirizzo di rete: 
    00000001.00000000.00000000.00000000
    e settando tutti i numeri binari a 1 dopo gli 8 bit della subnet, otteniamo il broadcast
    00000001.11111111.11111111.11111111
  
  	Quindi:
    Broadcast ip: 1.255.255.255
    
    Ottetti host: 3: Secondo, terzo e quarto. (24 bit)
    Ottetti network: 1: il primo. (8 bit)
    Host massimi: 2^24 (ottetti disponibili per gli host in questo caso) − 2 = 16777214.
    
    
    
    
   ## 128.1.6.5/12

|          | Decimale | Binario            |
|----------|----------|--------------------|
| **IP**   | 128.1.6.5 | 10000000.00000001.00000110.00000101|
| **Subnet mask** | 255.240.0.0 | 11111111.11110000.00000000.00000000 |

Applico gli stessi procedimenti di cui sopra e ottengo:

10000000.00000000.00000000.00000000

ovvero: 128.0.0.0 in decimale.

Quindi:

    Network ip: 128.0.0.0/8
    Gateway ip: 1.0.0.1
    Broadcast ip: 128.15.255.255 (stesso metodo di settare i binari a 1 dopo i 12bit in questo caso)
    Ottetti host: 2 (20 bit) restanti
    Ottetti network: 2(12bit)
    Host massimi: 2^20(ottetti disponibili per gli host in questo caso) − 2 = 1048574.
    
    
    
   ## 200.1.2.3/24
       
       Network ip: 200.1.2.0
       Gateway ip: 200.1.2.1
       Broadcast ip: 200.1.2.255
       Ottetti host: 1
       Ottetti rete: 3
       Host massimi: 254
       
       
       
   ## 192.192.1.1/22
       
       Network ip: 192.192.0.0
       Gateway ip: 192.192.0.1
       Broadcast ip: 192.192.3.255
       Ottetti host: 2
       Ottetti rete: 2
       Host massimi: 1022
       
       
   ## 126.5.4.3/9
       
       Network ip: 126.0.0.0
       Gateway ip: 126.0.0.1
       Broadcast ip: 126.127.255.255
       Ottetti host: 3
       Ottetti rete: 1
       Host massimi: 8388696
       
       
       
   ## 200.1.9.8/24
       
       Network ip: 200.1.9.0
       Gateway ip: 200.1.9.1
       Broadcast ip: 200.1.9.255
       Ottetti host: 1
       Ottetti rete: 3
       Host massimi: 254
       
           
   ## 172.16.0.4/16
       
       Network ip: 172.16.0.0
       Gateway ip: 172.16.0.1
       Broadcast ip: 172.16.255.255
       Ottetti host: 2
       Ottetti rete: 2
       Host massimi: 65534
       
       