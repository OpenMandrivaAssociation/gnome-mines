%define _disable_rebuild_configure 1
%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-mines
Version:	48.1
Release:	1
Summary:	GNOME Mines Sweeper game
License:	GPLv2+ and CC-BY-SA
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Apps/Mines
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	vala-devel >= 0.16.0
BuildRequires:	pkgconfig(libgnome-games-support-2)
BuildRequires:	meson
# For fix build issue:  "error: Package `librsvg-2.0' not found in specified Vala API directories or GObject-Introspection GIR directories" (penguin)
BuildRequires: librsvg-vala-devel
Obsoletes:	gnomine
# For help
Requires:	yelp

%description
The popular logic puzzle minesweeper. Find mines on a grid
using hints from squares you have already cleared.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Mines.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Mines.gschema.xml
%{_datadir}/%{name}
%{_iconsdir}/*/*/*/*
%{_mandir}/man6/%{name}.6*
%{_datadir}/metainfo/org.gnome.Mines.metainfo.xml

