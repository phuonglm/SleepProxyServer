import logging
from scapy.all import sendp,  Ether, IP, UDP, Raw, conf

def wake(mac):
    if logging.getLogger().getEffectiveLevel() > logging.DEBUG:
        conf.verb = 0

    logging.info("Sending WOL packet to %s" % (mac, ))
    mac = mac.decode("hex")
    sendp(Ether(dst='ff:ff:ff:ff:ff:ff') / IP(dst='255.255.255.255', flags="DF") / UDP(dport=9, sport=39227) / Raw('\xff' * 6 + mac * 16))

if __name__ == '__main__':
    import sys
    wake(sys.argv[1])
