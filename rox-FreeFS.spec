%define _name FreeFS
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	Monitor free space on a file system
Summary(pl):	ROX-FreeFS monitoruje ilo¶æ wolnej przestrzeni na dysku
Name:		rox-%{_name}
Version:	1.3.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tgz
Patch0:		%{name}-libxml-includes.patch
Patch1:		%{name}-paths-fix.patch
URL:		http://www.kerofin.demon.co.uk/rox/utils.html#freefs
BuildRequires:	libgtop-devel
BuildRequires:	libxml-devel
BuildRequires:	rox-CLib-devel >= 0.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define   _appsdir  %{_libdir}/ROX-apps

%description
ROX-FreeFS displays a small window showing the disk usage of a single
file system.

%description -l pl
ROX-FreeFS wy¶wietla ma³e okno pokazuj±ce wykorzystanie miejsca przez
pojedynczy system plików.

%prep
%setup -q -n %{_name}
%patch0 -p1
%patch1 -p1

%build
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,%{_platform}}

rm -f ../install
install App* choice_install gtkrc rox_run $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install %{_platform}/freefs $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}

%clean
rm -rf $RPM_BUILD_ROOT
rm -f install

%files
%defattr(644,root,root,755)
%doc Help/Versions
%attr(755,root,root) %{_appsdir}/%{_name}/*[Rr]un
%attr(755,root,root) %{_appsdir}/%{_name}/choice_install
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/gtkrc
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
