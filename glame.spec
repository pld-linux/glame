#
# Conditional build:
%bcond_without	alsa	# don't build ALSA audio plugin
%bcond_without	gnome	# build without GNOME-based GUI
#
Summary:	GNU/Linux Audio Mechanics
Summary(pl):	GNU/Linux Audio Mechanics - program do obróbki d¼wiêku
Name:		glame
Version:	2.0.1
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/glame/%{name}-%{version}.tar.gz
# Source0-md5:	b18e93e8f5d2ed9cd56c4e8088a58f18
Patch0:		%{name}-info.patch
Patch1:		%{name}-info_no_version.patch
Patch2:		%{name}-use_sys_libltdl.patch
Patch3:		%{name}-desktop.patch
URL:		http://glame.sourceforge.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 1.0.0}
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.0
#BuildRequires:	fftw-single-devel (TODO: update for fftw3-single-devel)
BuildRequires:	gettext-devel >= 0.11.5
%{?with_gnome:BuildRequires:	gtk+2-devel >= 2:2.6.0}
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.0.0}
BuildRequires:	guile-devel >= 1.4.1
BuildRequires:	ladspa-devel
BuildRequires:	lame-libs-devel
%{?with_gnome:BuildRequires:	libglade-devel}
BuildRequires:	libmad-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	texinfo
# not ready: jack, liblrdf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GLAME is targeted to be the GIMP for audio processing. Its developer
want to provide a powerful, fast, stable and easily extensible sound
editor for Linux and compatible systems.

%description -l pl
GLAME ma byæ odpowiednikiem GIMP-a do obróbki d¼wiêku. Jego twórcy
chc± daæ w pe³ni funkcjonalny, szybki, stabilny i ³atwo rozszerzalny
edytor d¼wiêk dla Linuksa i kompatybilnych z nim systemów.

%package gui
Summary:	GNOME-based GUI for GLAME
Summary(pl):	Oparty na GNOME graficzny interfejs do GLAME
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description gui
GNOME-based GUI for GLAME.

%description gui -l pl
Oparty na GNOME graficzny interfejs do GLAME.

%package audio-alsa
Summary:	ALSA audio plugin for GLAME
Summary(pl):	Wtyczka d¼wiêku ALSA dla GLAME
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description audio-alsa
Plugin for GLAME that allows playing sound through ALSA.

%description audio-alsa -l pl
Wtyczka dla GLAME pozwalaj±ca na odtwarzanie d¼wiêku przez ALSA.

%package audio-esd
Summary:	ESD audio plugin for GLAME
Summary(pl):	Wtyczka d¼wiêku ESD dla GLAME
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description audio-esd
Plugin for GLAME that allows playing sound through ESD.

%description audio-esd -l pl
Wtyczka dla GLAME pozwalaj±ca na odtwarzanie d¼wiêku przez ESD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	%{!?with_gnome:--disable-gui}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Multimediadir=%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CREDITS MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_bindir}/cglame
%attr(755,root,root) %{_bindir}/glame-convert.sh
%dir %{_libdir}/glame
%attr(755,root,root) %{_libdir}/glame/audio_io_oss.so
%attr(755,root,root) %{_libdir}/glame/debug.so
%attr(755,root,root) %{_libdir}/glame/tutorial.so
%{_libdir}/glame/audio_io_oss.la
%{_libdir}/glame/debug.la
%{_libdir}/glame/tutorial.la
# lame
%attr(755,root,root) %{_libdir}/glame/file_mp3_out.so
%{_libdir}/glame/file_mp3_out.la
# vorbis
%attr(755,root,root) %{_libdir}/glame/file_oggvorbis_out.so
%{_libdir}/glame/file_oggvorbis_out.la
%dir %{_datadir}/glame
%{_datadir}/glame/scripts
%{_infodir}/glame*.info*

%if %{with gnome}
%files gui -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glame
%{_datadir}/glame/pixmaps
%{_datadir}/glame/default-accels
%{_desktopdir}/*.desktop
%attr(755,root,root) %{_libdir}/glame/mixer.so
%attr(755,root,root) %{_libdir}/glame/normalize.so
%attr(755,root,root) %{_libdir}/glame/resample.so
%{_libdir}/glame/mixer.la
%{_libdir}/glame/normalize.la
%{_libdir}/glame/resample.la
%endif

%if %{with alsa}
%files audio-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/glame/audio_io_alsa.so
%{_libdir}/glame/audio_io_alsa.la
%endif

%files audio-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/glame/audio_io_esd.so
%{_libdir}/glame/audio_io_esd.la

#%files fft
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/glame/fft_plugins.so
#%{_libdir}/glame/fft_plugins.la
