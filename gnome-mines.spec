%define _disable_rebuild_configure 1
%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-mines
Version:	3.18.2
Release:	1
Summary:	GNOME Mines Sweeper game
License:	GPLv2+ and CC-BY-SA
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Apps/Mines
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	vala-devel >= 0.16.0
Obsoletes:	gnomine
# For help
Requires:	yelp

%description
The popular logic puzzle minesweeper. Find mines on a grid
using hints from squares you have already cleared.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.mines.gschema.xml
%{_datadir}/%{name}
%{_iconsdir}/*/*/*/*
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue Feb 17 2015 wally <wally> 3.14.0-3.mga5
+ Revision: 815340
- require yelp for showing help

* Wed Oct 15 2014 umeabot <umeabot> 3.14.0-2.mga5
+ Revision: 743505
- Second Mageia 5 Mass Rebuild

* Mon Sep 29 2014 wally <wally> 3.14.0-1.mga5
+ Revision: 731712
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 679737
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 fwang <fwang> 3.13.92-1.mga5
+ Revision: 677103
- update file list

  + ovitters <ovitters>
    - new version 3.13.92

* Mon Sep 01 2014 ovitters <ovitters> 3.13.91-1.mga5
+ Revision: 670708
- new version 3.13.91

* Sat Aug 23 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 666642
- new version 3.13.90

* Tue Jul 22 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655398
- new version 3.13.4

* Mon Jun 23 2014 ovitters <ovitters> 3.13.2-2.mga5
+ Revision: 638833
- update url

* Wed May 28 2014 ovitters <ovitters> 3.13.2-1.mga5
+ Revision: 627106
- new version 3.13.2

* Tue May 13 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622412
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614156
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 608069
- new version 3.12.0

* Mon Mar 17 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604567
- new version 3.11.92

* Tue Feb 18 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 594252
- new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.3-1.mga5
+ Revision: 583009
- new version 3.11.3

* Tue Oct 22 2013 umeabot <umeabot> 3.10.1-2.mga4
+ Revision: 541379
- Mageia 4 Mass Rebuild

* Sat Oct 12 2013 ovitters <ovitters> 3.10.1-1.mga4
+ Revision: 495801
- new version 3.10.1

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 484536
- new version 3.10.0

* Tue Sep 17 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480540
- new version 3.9.92

* Wed Aug 21 2013 fwang <fwang> 3.9.90-1.mga4
+ Revision: 468993
- new version 3.9.90

* Tue Aug 20 2013 ovitters <ovitters> 3.8.2-1.mga4
+ Revision: 468320
- new version 3.8.2

* Sun Jun 09 2013 fwang <fwang> 3.8.1-2.mga4
+ Revision: 441013
- cleanup spec

* Sun Jun 09 2013 dams <dams> 3.8.1-1.mga4
+ Revision: 440846
- imported package gnome-mines

