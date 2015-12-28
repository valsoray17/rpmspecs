Name:		rofi
Version:	0.15.11
Release:	1%{?dist}
Summary:	A window switcher, run dialog and dmenu replacement

#Group:		
License:	MIT/X11
URL:		https://davedavenport.github.io/%{name}/
Source0:	https://github.com/DaveDavenport/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

#BuildRequires:	
#Requires:	

%description
A popup window switcher roughly based on superswitcher, requiring only xlib and pango.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}


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

