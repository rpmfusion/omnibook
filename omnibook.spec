%define         svn 1

Name:           omnibook

Version:        2.20090714
Release:        0.5.svn288%{?dist}
Summary:        Common files for omnibook-kmod

Group:          System Environment/Kernel

License:        GPLv2
URL:            http://sourceforge.net/projects/omnibook/
%if %{svn}
# svn export -r288 https://omnibook.svn.sourceforge.net/svnroot/omnibook/omnibook/trunk omnibook-2.20090714
Source0:        omnibook-%{version}.tar.xz
%else
Source0:        http://downloads.sourceforge.net/project/omnibook/omnibook%20kernel%20module/%{version}/omnibook-%{version}.tar.gz
%endif
Source1:        omnibook.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       %{name}-kmod-common = %{version}-%{release}

%description
Linux kernel module for many HP Omnibook/Pavillon, Toshiba Satellite
(with Phoenix BIOS) and Compal laptops. It is based on the module found
in the 'omke' project.

%prep
%setup -q -n omnibook-%{version}

%build
echo nothing to build

%install
install -Dpm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/modprobe.d/omnibook.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc/*
%{_sysconfdir}/modprobe.d/omnibook.conf

%changelog
* Sun Jan 24 2010 Dominik Mierzejewski <rpm@greysector.net> 2.20090714-0.5.svn288
- better, lower-level method for autoloading

* Sat Jan 23 2010 Dominik Mierzejewski <rpm@greysector.net> 2.20090714-0.4.svn288
- autoload module

* Mon Nov 16 2009 Dominik Mierzejewski <rpm@greysector.net> 2.20090714-0.2.svn288
- rename to omnibook, provide -kmod-common
- fix build

* Wed Sep 16 2009 Dominik Mierzejewski <rpm@greysector.net> 2.20090714-0.1.svn288
- initial build for RPM Fusion
