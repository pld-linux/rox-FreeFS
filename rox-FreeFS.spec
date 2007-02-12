%define _name FreeFS
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	Monitor free space on a file system
Summary(pl.UTF-8):	ROX-FreeFS monitoruje ilość wolnej przestrzeni na dysku
Name:		rox-%{_name}
Version:	2.1.3
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tar.gz
# Source0-md5:	bffcc4eea508e2bee7ad04bc6882b6c3
Source1:	%{name}.desktop
#Patch0:	%{name}-paths-fix.patch
Patch1:		%{name}-ROX-CLib2-include.patch
Patch2:		%{name}-ROX-apps-paths.patch
Patch3:		%{name}-aclocal.patch
Patch4:		%{name}-Choices-dir.patch
URL:		http://www.kerofin.demon.co.uk/rox/freefs.html
BuildRequires:	autoconf
BuildRequires:	glib2-devel >= 2.0.3
BuildRequires:	gtk+2-devel >= 2.0.1
BuildRequires:	libgtop-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	pkgconfig
BuildRequires:	rox-CLib2-devel >= 2.1.5-2
Requires:	rox >= 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_roxdir	%{_libdir}/rox

%description
ROX-FreeFS displays a small window showing the disk usage of a single
file system.

%description -l pl.UTF-8
ROX-FreeFS wyświetla małe okno pokazujące wykorzystanie miejsca przez
pojedynczy system plików.

%prep
%setup -q -n %{_name}
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cd src
%{__autoconf}
cd ..
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_roxdir}/%{_name}/{Help,%{_platform}}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install .DirIcon *.xml choice_install gtkrc rox_run $RPM_BUILD_ROOT%{_roxdir}/%{_name}
install AppRun AppletRun $RPM_BUILD_ROOT%{_roxdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Help
install %{_platform}/freefs $RPM_BUILD_ROOT%{_roxdir}/%{_name}/%{_platform}
install .DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

sed -e "s,/lib/,/%{_lib}/," %{SOURCE1} > $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/{Changes,Versions}
%attr(755,root,root) %{_roxdir}/%{_name}/*[Rr]un
%attr(755,root,root) %{_roxdir}/%{_name}/choice_install
%attr(755,root,root) %{_roxdir}/%{_name}/%{_platform}
%dir %{_roxdir}/%{_name}
%{_roxdir}/%{_name}/.DirIcon
%{_roxdir}/%{_name}/*.xml
%{_roxdir}/%{_name}/gtkrc
%{_roxdir}/%{_name}/Help
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
