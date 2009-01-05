%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-pywbem
Version:        0.7.0
Release:        1%{?dist}
Summary:        Python WBEM Client
Patch0:		add-licence-txt.patch

Group:          Development/Languages
License:        LGPLv2
URL:            http://pywbem.sourceforge.net
Source0:        http://downloads.sourceforge.net/pywbem-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel

Requires: python >= 2.3

%description
PyWBEM is a Python library for making CIM operations over HTTP using the 
WBEM CIM-XML protocol.  WBEM is a manageability protocol, like SNMP,
standardised by the Distributed Management Task Force (DMTF) available
at http://www.dmtf.org/standards/wbem.

%prep
%setup -q -n pywbem-%{version}
%patch0 -p0

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%doc LICENSE.txt

%{python_sitelib}/*

%changelog
* Tue Jan 05 2009 Tim Potter <tpot@hp.com> - 0.7.0-1
- New upstream version
* Mon Mar 17 2008 Tim Potter <tpot@hp.com> - 0.6-1
- New upstream version
* Tue Jun 26 2007 Tim Potter <tpot@hp.com> - 0.5-1
- Initial packaging
