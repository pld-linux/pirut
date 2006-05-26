Summary:	Package Installation, Removal and Update Tools
Summary(pl):	Narz�dzia do instalowania, usuwania i uaktualniania pakiet�w
Name:		pirut
Version:	1.0.1
Release:	0.2
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	b628cc41256fa48dfb77c54085823eb6
URL:		http://fedoraproject.org/
Requires(post,postun):	desktop-file-utils >= 0.8
Patch0:		%{name}-desktop.patch
#Requires:	comps-extras
#Requires:	python-pygtk
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	python-pygtk-glade
Requires:	yum >= 2.5.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pirut (pronounced "pirate") provides a set of graphical tools for
managing software.

%description -l pl
pirut (wymawiane tak, jak angielskie s�owo "pirate") to zbi�r
graficznych narz�dzi do zarz�dzania oprogramowaniem.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%{_desktopdir}/kde/*.desktop
%dir %{_datadir}/pirut
%dir %{_datadir}/pirut/ui
%{_datadir}/pirut/ui/*.glade
%dir %{_datadir}/pirut/pixmaps
%{_datadir}/pirut/pixmaps/*.png
%{_pixmapsdir}/*png
