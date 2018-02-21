%global pkgname xprofile

Name:		xorg-x11-%{pkgname}	
Version:	1.0.0
Release:	1%{?dist}
Summary:	X.Org X11 X Window System scripts to source .xprofile

License:	GPLv3+
URL:		https://github.com/valsoray17/rpmspecs
Source0:	xprofile-%{version}.tar.gz

#BuildRequires:	
#Requires:	

%description


%prep
%setup -c

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d
install -p -m 755 xprofile.sh $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/xprofile.sh

%files
%doc
%dir %{_sysconfdir}/X11/xinit/xinitrc.d
%{_sysconfdir}/X11/xinit/xinitrc.d/xprofile.sh



%changelog

