Summary:	GNU/Linux Audio Mechanics
Summary(pl):	GNU/Linux Audio Mechanics - program do obr�bki d�wi�ku
Name:		glame
Version:	0.5.2
Release:	3
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Source0:	ftp://download.sourceforge.net/pub/sourceforge/glame/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
URL:		http://glame.sourceforge.net/
Prereq:		/sbin/ldconfig
BuildRequires:	guile-devel >= 1.3.4
BuildRequires:	libxml2-devel
BuildRequires:	esound-devel
%{!?_without_gnome:BuildRequires: gtk+-devel >= 1.2.0}
%{!?_without_gnome:BuildRequires: gnome-libs-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man
%define		_infodir	/usr/share/info

%description
GLAME is targeted to be the GIMP for audio processing. Its developer
want to provide a powerful, fast, stable and easily extensible sound
editor for Linux and compatible systems.

%description -l pl
GLAME ma by� odpowiednikiem GIMP-a do obr�bki d�wi�ku. Jego tw�rcy
chc� da� w pe�ni funkcjonalny, szybki, stabilny i �atwo rozszerzalny
edytor d�wi�k dla Linuksa i kompatybilnych z nim system�w.

%prep
%setup -q
%patch -p1

%build
#rm -f missing
#libtoolize --copy --force
#aclocal -I macros
#autoconf
#automake -a -c
%configure2_13 \
	--disable-static \
	%{?_without_gnome:--disable-gui}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/gui/glame.desktop $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

gzip -9nf AUTHORS BUGS CREDITS MAINTAINERS NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/glame
%{_datadir}/glame
%{_applnkdir}/Multimedia/*
%{_infodir}/glame*
