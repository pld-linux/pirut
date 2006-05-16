Summary:	Package Installation, Removal and Update Tools
Name:		pirut
Version:	1.0.1
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://fedoraproject.org
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	b628cc41256fa48dfb77c54085823eb6
Requires(post):	desktop-file-utils >= 0.8
Requires(postun):	desktop-file-utils >= 0.8
#Requires:	comps-extras
#Requires:	python-pygtk
Requires:	python-pygtk-glade
Requires:	yum >= 2.5.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pirut (pronounced "pirate") provides a set of graphical tools for
managing software.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/update-desktop-database %{_desktopdir}

%postun
%{_bindir}/update-desktop-database %{_desktopdir}


%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS AUTHORS
%{py_sitescriptdir}/pirut
%attr(755,root,root) %{_bindir}/pirut
%attr(755,root,root) %{_bindir}/pup
%attr(755,root,root) %{_bindir}/system-install-packages
%attr(755,root,root) %{_sbindir}/pirut
%attr(755,root,root) %{_sbindir}/pup
%attr(755,root,root) %{_sbindir}/system-install-packages
/etc/pam.d/*
/etc/security/console.apps/*
%{_desktopdir}/*.desktop
%dir %{_datadir}/pirut
%dir %{_datadir}/pirut/ui
%{_datadir}/pirut/ui/*.glade
%dir %{_datadir}/pirut/pixmaps
%{_datadir}/pirut/pixmaps/*.png
%{_pixmapsdir}/*png
