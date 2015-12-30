Name:		rofi
Version:	0.15.12
Release:	1%{?dist}
Summary:	A window switcher, run dialog and dmenu replacement

#Group:		
License:	MIT/X11
URL:		https://davedavenport.github.io/%{name}/
Source0:	https://github.com/DaveDavenport/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: i3 >= 4.5
BuildRequires: pkgconfig(xft) >= 2.0
BuildRequires: pkgconfig(cairo-xlib)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xinerama)

%description
A popup window switcher roughly based on superswitcher, requiring only xlib and pango.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%check
make test

%files
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_mandir}/man1/rofi.1.*
%{_mandir}/man1/rofi-sensible-terminal.1.*
%doc AUTHORS Changelog README.md Examples 
%license COPYING

%changelog
* Wed Dec 30 2015 Yaroslav Sapozhnyk <yaroslav.sapozhnik@gmail.com> - 0.15.12-1
- Updating to 0.15.12

* Wed Dec 30 2015 Yaroslav Sapozhnyk <yaroslav.sapozhnik@gmail.com> - 0.15.11-2
- Spec file cleanup

* Wed Dec 30 2015 Yaroslav Sapozhnyk <yaroslav.sapozhnik@gmail.com> - 0.15.11-1
- Initial package


