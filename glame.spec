Summary:	GLAME 0.2.0 - GNU/Linux Audio Mechanics
Name:		glame
Version:	0.2.0
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://download.sourceforge.net/pub/sourceforge/glame/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
URL:		http://glame.sourceforge.net/
Prereq:		/usr/sbin/fix-info-dir
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	XFree86-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man
%define		_infodir	/usr/share/info

%description

%prep
%setup -q
%patch -p1

%build
%configure \
	--disable-static \
	--with-gnome \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS MAINTAINERS NEWS README TODO

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/glame
%attr(755,root,root) %{_libdir}/glame/*
%{_infodir}/*
