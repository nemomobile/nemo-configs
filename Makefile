all:

install:
	install -D -m 644 connman/main.conf $(DESTDIR)/etc/connman/main.conf
	install -D -m 644 prjconf/nemo-prjconf.xml $(DESTDIR)/usr/share/prjconf/nemo-prjconf.xml

