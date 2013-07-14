all:

install:
	install -D -m 644 connman/main.conf $(DESTDIR)/etc/connman/main.conf

