Summary:	GLAME 0.2.0 - GNU/Linux Audio Mechanics
Name:		glame
Version:	0.5.2
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
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

%prep
%setup -q
%patch -p1

%build
#libtoolize --copy --force
#aclocal -I macros
#autoconf
%configure2_13 \
	--disable-static \
	%{?_without_gnome:--disable-gui}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install src/gui/glame.desktop $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

gzip -9nf AUTHORS BUGS CREDITS MAINTAINERS NEWS README TODO

%post
/sbin/ldconfig
%fix_info_dir

%postun
/sbin/ldconfig
%fix_info_dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/glame
%attr(755,root,root) %{_libdir}/glame/*.so
#%attr(755,root,root) %{_libdir}/glame/*.la	# is it needed?
%{_datadir}/glame
%{_applnkdir}/Multimedia/*
%{_infodir}/*
