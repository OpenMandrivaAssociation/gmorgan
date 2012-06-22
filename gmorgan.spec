Summary:	MIDI auto-accompaniment generator
Name:		gmorgan
Version:	0.56
Release:	1
License:	GPLv2+
Group:		Sound
URL:		http://gmorgan.sourceforge.net/
Source0:	%{name}_%{version}.tar.gz

BuildRequires:	fltk-devel
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(alsa)

%description
GMorgan is a modern MIDI organ with full auto-accompaniment. GMrgand uses
soundfonts and the ALSA sequencer for emulate a Rhythm Station.

%prep
%setup -qn %{name}_%{version}

%build
%configure2_5x
%make  

%install
%makeinstall_std

rm -fr %{buildroot}/%{_docdir}
chmod 644 AUTHORS ChangeLog README 

#menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=sound_section
Name=GMorgan
Comment=MIDI Auto-Accompaniment
Categories=Audio;
EOF

%files 
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

