%define name	gmorgan
%define version	0.25
%define release 1mdk

Name: 	 	%{name}
Summary:	MIDI auto-accompaniment generator 	
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://gmorgan.sourceforge.net/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	fltk-devel libalsa-devel 

%description
GMorgan is a modern MIDI organ with full auto-accompaniment. GMrgand uses
soundfonts and the ALSA sequencer for emulate a Rhythm Station.

%prep
%setup -q
#perl -p -i -e "s|-O6|$RPM_OPT_FLAGS||g" src/Makefile

%build
%configure2_5x
%make  
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
make install PREFIX=%_prefix DESTDIR=$RPM_BUILD_ROOT
rm -fr $RPM_BUILD_ROOT/%_docdir
%find_lang %name

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="sound_section.png" needs="x11" title="GMorgan" longtitle="MIDI Auto-Accompaniment" section="Multimedia/Sound"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/%name
%{_datadir}/%name
%{_menudir}/%name

