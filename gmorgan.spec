Summary:	MIDI auto-accompaniment generator
Name:		gmorgan
Version:		0.79
Release:		1
License:	GPLv2+
Group:	Sound
Url:		https://gmorgan.sourceforge.net
Source0:	https://sourceforge.net/projects/%{name}/files/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
Patch0:		gmorgan-0.79-libfltk.patch
Patch1:		gmorgan-0.79-gettext.patch
Patch2:		gmorgan-0.79-install.patch
Patch3:		gmorgan-0.79-fix-chord-table-detection.patch
Patch4:		gmorgan-0.79-drop-register-keywords.patch
Patch5:		gmorgan-0.79-fix-literal-error.patch
BuildRequires:		autoconf
BuildRequires:		automake
BuildRequires:		help2man
BuildRequires:		libtool-base
BuildRequires:		make
BuildRequires:		slibtool
BuildRequires:		fltk-devel
BuildRequires:		gettext-devel
BuildRequires:		pkgconfig(alsa)
BuildRequires:		pkgconfig(cairo)
BuildRequires:		pkgconfig(dbus-1)
BuildRequires:		pkgconfig(libdecor-0)
BuildRequires:		pkgconfig(libjpeg)
BuildRequires:		pkgconfig(libpng)
BuildRequires:		pkgconfig(pixman-1)
BuildRequires:		pkgconfig(wayland-client)
BuildRequires:		pkgconfig(wayland-cursor)
BuildRequires:		pkgconfig(x11)
BuildRequires:		pkgconfig(xcursor)
BuildRequires:		pkgconfig(xfixes)
BuildRequires:		pkgconfig(xinerama)
BuildRequires:		pkgconfig(xkbcommon)
BuildRequires:		pkgconfig(xrender)

%description
GMorgan is a modern MIDI organ with full auto-accompaniment. It uses
soundfonts and the ALSA sequencer for emulate a Rhythm Station.

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%doc doc/%{name}0.75.pdf
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/openmandriva-%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_sysconfdir}/modules-load.d/%{name}.conf

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
autoreconf -vfi
%configure
%make_build


%install
%make_install

# Drop installed docs: we pick them with our %%doc macro
rm -fr %{buildroot}/%{_docdir}
#chmod 644 AUTHORS ChangeLog README 

# To load snd_seq on-demand
mkdir -p %{buildroot}%{_sysconfdir}/modules-load.d
echo "snd_seq" > %{buildroot}%{_sysconfdir}/modules-load.d/%{name}.conf

# Menu item
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/openmandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=sound_section
Name=GMorgan
Comment=MIDI Auto-Accompaniment
Categories=Audio;
EOF

%find_lang %{name}

