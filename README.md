# rpmspecs
RPM spec files

## Packaging info
### Compton    
Download source 
```
#wget -O chjj-compton-%{commit}.tar.gz --no-check-certificate --content-disposition http://github.com/chjj/compton/tarball/%{commit}
```
[Old RPM Package](http://pkgs.fedoraproject.org/cgit/?q=compton)  
[Direct Link](https://admin.fedoraproject.org/pkgdb/package/rpms/compton/)
[openSuSE Link](https://build.opensuse.org/package/binaries/X11:QtDesktop/compton?repository=Fedora_21)
### i3-gaps
i3-gaps package doesn't have configure script, hence need to

1. Untar i3-gaps.tar.gz package
2. Run autoreconf -fi (this is not recommended to be run from RPM build)
3. Package the i3-gaps back

[Fedora i3 spec](http://pkgs.fedoraproject.org/cgit/rpms/i3.git/tree/i3.spec)  
[Arch i3-gaps pkgbuild](https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=i3-gaps)  

## Useful links
[How to create RPM package](https://fedoraproject.org/wiki/How_to_create_an_RPM_package)  
[How to create GNU Hello World package](https://fedoraproject.org/wiki/How_to_create_a_GNU_Hello_RPM_package)  
[Max RPM](http://rpm.org/max-rpm-snapshot/index.html)

### Fedora Packaging
[Fedora Packagers Guilde](https://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/Packagers_Guide/)  
[Fedora RPM Guide](https://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/)  
[Joining Packagers](https://fedoraproject.org/wiki/Join_the_package_collection_maintainers)  

### Packaging Links
[pkg-config](http://www.freedesktop.org/wiki/Software/pkg-config/)   
[How To Find Libs](https://cmake.org/Wiki/CMake:How_To_Find_Libraries)   
[pkg-config Guide](http://people.freedesktop.org/~dbn/pkg-config-guide.html)   
[BuildRequires](https://fedoraproject.org/wiki/Packaging:Guidelines#BuildRequires_based_on_pkg-config)   
[Howto Use BuildRequires](https://fedoraproject.org/wiki/HOWTOUseRequires)

### Github
[Tarball Docs](https://developer.github.com/v3/repos/contents/)

##Commands
```
rpmdev-bumpspec -n 0.15.12 -r rofi.spec --comment="Updating..." -u "User Name <user.name@host.com>"
pkg-config --list-all | grep xft2
pkg-config --print-requires cairo-xlib
pkg-config --list-all | grep startup-notification-1.0
/usr/lib/rpm/macros #has info on rpm build macroses
```

## CMatrix
Patch0:
```
--- Makefile.am
+++ Makefile.am
@@ -8,32 +8,27 @@
                matrix.psf.gz mtx.pcf cmatrix.1 cmatrix.spec

 install-data-local:
-       @if test -d /usr/share/consolefonts; then \
-           echo " Installing matrix fonts in /usr/share/consolefonts..."; \
-           $(INSTALL_DATA) $(srcdir)/matrix.fnt /usr/share/consolefonts; \
-           $(INSTALL_DATA) $(srcdir)/matrix.psf.gz /usr/share/consolefonts; \
+       @if test -d /usr/share/kbd/consolefonts; then \
+           echo " Installing matrix fonts in $(DESTDIR)/usr/share/kbd/consolefonts..."; \
+           $(INSTALL_DATA) $(srcdir)/matrix.fnt $(DESTDIR)/usr/share/kbd/consolefonts; \
+           $(INSTALL_DATA) $(srcdir)/matrix.psf.gz $(DESTDIR)/usr/share/kbd/consolefonts; \
+       elif test -d /usr/share/consolefonts; then \
+           echo " Installing matrix fonts in $(DESTDIR)/usr/share/consolefonts..."; \
+           $(INSTALL_DATA) $(srcdir)/matrix.fnt $(DESTDIR)/usr/share/consolefonts; \
+           $(INSTALL_DATA) $(srcdir)/matrix.psf.gz $(DESTDIR)/usr/share/consolefonts; \
+       elif test -d /lib/kbd/consolefonts; then \
+           echo " Installing matrix fonts in $(DESTDIR)/lib/kbd/consolefonts..."; \
+           $(INSTALL_DATA) $(srcdir)/matrix.fnt $(DESTDIR)/lib/kbd/consolefonts; \
+           $(INSTALL_DATA) $(srcdir)/matrix.psf.gz $(DESTDIR)/lib/kbd/consolefonts; \
        fi
-       @if test -d /usr/lib/kbd/consolefonts; then \
-           echo " Installing matrix fonts in /usr/lib/kbd/consolefonts..."; \
-           $(INSTALL_DATA) $(srcdir)/matrix.fnt /usr/lib/kbd/consolefonts; \
-           $(INSTALL_DATA) $(srcdir)/matrix.psf.gz /usr/lib/kbd/consolefonts; \
-       fi
-       @if test -d /usr/lib/X11/fonts/misc; then \
-           echo " Installing X window matrix fonts in /usr/lib/X11/fonts/misc..."; \
-           $(INSTALL_DATA) $(srcdir)/mtx.pcf /usr/lib/X11/fonts/misc; \
-           $(INSTALL_DATA) $(srcdir)/mtx.pcf /usr/lib/X11/fonts/misc; \
-           echo " Running mkfontdir /usr/lib/X11/fonts/misc..."; \
-           $(MKFONTDIR) /usr/lib/X11/fonts/misc; \
-           echo " Done.  If this is the first time you have installed CMatrix you will"; \
-           echo " probably have to restart X window in order to use the mtx.pcf font."; \
+       @if test -d /usr/X11R6/lib/X11/fonts/misc; then \
+           echo " Installing X window matrix fonts in $(DESTDIR)/usr/X11R6/lib/X11/fonts/misc..."; \
+           $(INSTALL_DATA) $(srcdir)/mtx.pcf $(DESTDIR)/usr/X11R6/lib/X11/fonts/misc; \
+           $(INSTALL_DATA) $(srcdir)/mtx.pcf $(DESTDIR)/usr/X11R6/lib/X11/fonts/misc; \
        else \
-       if test -d /usr/X11R6/lib/X11/fonts/misc; then \
-           echo " Installing X window matrix fonts in /usr/X11R6/lib/X11/fonts/misc..."; \
-           $(INSTALL_DATA) $(srcdir)/mtx.pcf /usr/X11R6/lib/X11/fonts/misc; \
-           $(INSTALL_DATA) $(srcdir)/mtx.pcf /usr/X11R6/lib/X11/fonts/misc; \
-           echo " Running mkfontdir /usr/X11R6/lib/X11/fonts/misc..."; \
-           $(MKFONTDIR) /usr/X11R6/lib/X11/fonts/misc; \
-           echo " Done.  If this is the first time you have installed CMatrix you will"; \
-           echo " probably have to restart X window in order to use the mtx.pcf font."; \
+       if test -d /usr/lib/X11/fonts/misc; then \
+           echo " Installing X window matrix fonts in $(DESTDIR)/usr/lib/X11/fonts/misc..."; \
+           $(INSTALL_DATA) $(srcdir)/mtx.pcf $(DESTDIR)/usr/lib/X11/fonts/misc; \
+           $(INSTALL_DATA) $(srcdir)/mtx.pcf $(DESTDIR)/usr/lib/X11/fonts/misc; \
        fi \
        fi
```
