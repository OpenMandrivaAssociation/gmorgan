Name: 	 	gmorgan
Summary:	MIDI auto-accompaniment generator 	
Version: 	0.25
Release: 	%{mkrel 4}
Source0:	%{name}-%{version}.tar.bz2
# Fix build on x86-64 (from Debian) - AdamW 2008/08
Patch0:		01_ftbfs_amd64.diff
URL:		http://gmorgan.sourceforge.net/
License:	GPLv2+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	fltk-devel
BuildRequires:	libalsa-devel
BuildRequires:	gettext-devel

%description
GMorgan is a modern MIDI organ with full auto-accompaniment. GMrgand uses
soundfonts and the ALSA sequencer for emulate a Rhythm Station.

%prep
%setup -q
%patch0 -p0 -b .x86_64
#perl -p -i -e "s|-O6|$RPM_OPT_FLAGS||g" src/Makefile

%build
rm -f m4/po.m4
cp %{_datadir}/aclocal/po.m4 m4/po.m4
autoreconf
%configure2_5x
%make  
										
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}
rm -fr %{buildroot}/%{_docdir}
%find_lang %{name}

#menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=sound_section
Name=GMorgan
Comment=MIDI Auto-Accompaniment
Categories=Audio;
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif
		
%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

