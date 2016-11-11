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
