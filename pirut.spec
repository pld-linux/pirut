Summary:	Package Installation, Removal and Update Tools
Summary(pl.UTF-8):	Narzędzia do instalowania, usuwania i uaktualniania pakietów
Name:		pirut
Version:	1.3.31
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/pirut/%{name}-%{version}.tar.gz/c6994f02627834c374f0855540850cd7/pirut-%{version}.tar.gz
# Source0-md5:	c6994f02627834c374f0855540850cd7
URL:		https://fedoraproject.org/wiki/Tools/pirut
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-consolehelper.patch
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	python
Requires(post):	desktop-file-utils >= 0.8
Requires(postun):	desktop-file-utils >= 0.8
Requires:	comps-extras
Requires:	python-dbus
Requires:	python-gnome-gconf
Requires:	python-iniparse
Requires:	python-pygtk-glade
Requires:	python-pygtk-glade
Requires:	python-pygtk-gtk >= 2.9.2
Requires:	python-pynotify
Requires:	rhpl
Requires:	usermode
Requires:	yum >= 3.2.5-2
Obsoletes:	pup
Obsoletes:	redhat-config-packages
Obsoletes:	rhn-applet
Obsoletes:	system-config-packages
Obsoletes:	up2date-gnome
BuildArch:	noarch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pirut (pronounced "pirate") provides a set of graphical tools for
managing software.

%description -l pl.UTF-8
pirut (wymawiane tak, jak angielskie słowo "pirate") to zbiór
graficznych narzędzi do zarządzania oprogramowaniem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
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
/etc/pam.d/*
/etc/security/console.apps/*
%attr(755,root,root) %{_sbindir}/pirut
%attr(755,root,root) %{_sbindir}/pup
%attr(755,root,root) %{_sbindir}/system-install-packages
%{py_sitescriptdir}/pirut
%{_datadir}/pirut
%{_desktopdir}/*.desktop
%{_desktopdir}/kde/*.desktop
%{_pixmapsdir}/*png
