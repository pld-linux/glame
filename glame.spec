Summary:	GNU/Linux Audio Mechanics
Summary(pl):	GNU/Linux Audio Mechanics - program do obróbki d¼wiêku
Name:		glame
Version:	1.0.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.sourceforge.net/glame/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-info_no_version.patch
Patch2:		%{name}-use_sys_libltdl.patch
Patch3:		%{name}-desktop.patch
URL:		http://glame.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
%{!?_without_gnome:BuildRequires: gtk+-devel >= 1.2.0}
%{!?_without_gnome:BuildRequires: gnome-libs-devel}
BuildRequires:	guile-devel >= 1.4.1
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GLAME is targeted to be the GIMP for audio processing. Its developer
want to provide a powerful, fast, stable and easily extensible sound
editor for Linux and compatible systems.

%description -l pl
GLAME ma byæ odpowiednikiem GIMP-a do obróbki d¼wiêku. Jego twórcy
chc± daæ w pe³ni funkcjonalny, szybki, stabilny i ³atwo rozszerzalny
edytor d¼wiêk dla Linuksa i kompatybilnych z nim systemów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	%{?_without_gnome:--disable-gui}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/applications

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Multimediadir=%{_datadir}/applications

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS CREDITS MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/glame
%{_datadir}/glame
%{_datadir}/applications/*
%{_infodir}/glame*
