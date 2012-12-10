Summary:	MIDI auto-accompaniment generator
Name:		gmorgan
Version:	0.56
Release:	2
License:	GPLv2+
Group:		Sound
URL:		http://gmorgan.sourceforge.net/
Source0:	%{name}_%{version}.tar.gz

BuildRequires:	fltk-devel
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pixman-1)


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



%changelog
* Fri Jun 22 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.56-1
+ Revision: 806694
- new version 0.56
- cleaned up spec

* Mon Dec 06 2010 Funda Wang <fwang@mandriva.org> 0.27-2mdv2011.0
+ Revision: 611823
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Thu Apr 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.27-1mdv2010.1
+ Revision: 533141
- use a tar.gz
- remove %%post && %%postun
- update to 0.27
- drop p0, applied upstream.

* Mon Jan 18 2010 Jérôme Brenier <incubusss@mandriva.org> 0.25-4mdv2010.1
+ Revision: 493334
- rebuild for new fltk

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Aug 20 2008 Adam Williamson <awilliamson@mandriva.org> 0.25-2mdv2009.0
+ Revision: 274097
- add 01_ftbfs_amd64.diff from debian to fix x86-64 build
- rebuild for new era
- replace m4/po.m4 with system copy to fix build (per debian #456588)
- br gettext-devel
- clean spec

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - auto convert menu to XDG
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import gmorgan

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Thu Nov 10 2005 Austin Acton <austin@mandriva.org> 0.25-1mdk
- New release 0.25

* Fri Jul 9 2004 Austin Acton <austin@mandrake.org> 0.24-1mdk
- 0.24

* Tue Jun 22 2004 Austin Acton <austin@mandrake.org> 0.23-1mdk
- 0.23

* Sun Jun 6 2004 Austin Acton <austin@mandrake.org> 0.22-2mdk
- configure 2.5

* Tue Jan 27 2004 Austin Acton <austin@mandrake.org> 0.22-1mdk
- 0.22

* Mon Jan 5 2004 Austin Acton <austin@linux.ca> 0.21-1mdk
- 0.21

* Sat Dec 27 2003 Austin Acton <austin@linux.ca> 0.20-1mdk
- 0.20
- new URL
- locales

* Mon Sep 8 2003 Austin Acton <aacton@yorku.ca> 0.16-1mdk
- 0.16

* Mon Sep 1 2003 Austin Acton <aacton@yorku.ca> 0.15-1mdk
- 0.15

* Mon Aug 25 2003 Austin Acton <aacton@yorku.ca> 0.14-1mdk
- 0.14

* Thu Aug 7 2003 Austin Acton <aacton@yorku.ca> 0.10-1mdk
- 0.10
- new URL

* Wed Jul 30 2003 Austin Acton <aacton@yorku.ca> 0.07-1mdk
- 0.07

* Wed Jul 16 2003 Austin Acton <aacton@yorku.ca> 0.04-1mdk
- 0.04

* Mon Jul 14 2003 Austin Acton <aacton@yorku.ca> 0.03-1mdk
- 0.03

* Mon Jul 7 2003 Austin Acton <aacton@yorku.ca> 0.01-1mdk
- initial package
