Name: 	 	gmorgan
Summary:	MIDI auto-accompaniment generator 	
Version: 	0.27
Release: 	%mkrel 2
Source0:	%{name}-%{version}.tar.gz
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

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

