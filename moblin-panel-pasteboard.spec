# i wish they would stop updating translations after a release
%define checkout e1e674bb9c129e65b2171f93add2f3ac3e170d88

Name: moblin-panel-pasteboard
Summary: Pasteboard panel for Moblin
Group: Graphical desktop/Other 
Version: 0.0.3
License: LGPL 2.1
URL: http://www.moblin.org
Release: %mkrel 2
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{checkout}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: clutter-devel
BuildRequires: gtk2-devel
BuildRequires: nbtk-devel
BuildRequires: moblin-panel-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common

%description
Moblin pasteboard panel

%prep
%setup -q -n %{name}-%{checkout}

%build
NOCONFIGURE=nil ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING README NEWS AUTHORS ChangeLog
%{_libexecdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/*service
