%global srcname pysmi

%{?python_disable_dependency_generator}

Name:           python-smi
Version:        0.3.4
Release:        8%{?dist}
Summary:        A Python implementation of SNMP/SMI MIB parsing and conversion library

License:        BSD
URL:            https://github.com/etingof/pysmi
Source0:        %{pypi_source}
BuildArch:      noarch

%description
PySMI is a pure-Python implementation of SNMP SMI MIB parser. This tool is
designed to turn ASN.1 MIBs into various formats. As of this moment, JSON 
and pysnmp modules can be generated from ASN.1 MIBs.

- Understands SMIv1, SMIv2 and de-facto SMI dialects
- Turns MIBs into pysnmp classes and JSON documents
- Maintains an index of MIB objects over many MIB modules
- Automatically pulls ASN.1 MIBs from local directories, ZIP archives, HTTP
  and FTP servers

%package -n python3-smi
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-ply
%{?python_provide:%python_provide python3-smi}

%description -n python3-smi
PySMI is a pure-Python implementation of SNMP SMI MIB parser. This tool is
designed to turn ASN.1 MIBs into various formats. As of this moment, JSON 
and pysnmp modules can be generated from ASN.1 MIBs.

- Understands SMIv1, SMIv2 and de-facto SMI dialects
- Turns MIBs into pysnmp classes and JSON documents
- Maintains an index of MIB objects over many MIB modules
- Automatically pulls ASN.1 MIBs from local directories, ZIP archives, HTTP
  and FTP servers

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install
mv %{buildroot}%{_bindir}/mibcopy.py %{buildroot}%{_bindir}/mibcopy
mv %{buildroot}%{_bindir}/mibdump.py %{buildroot}%{_bindir}/mibdump

# Tests depend on python3-pysnmp and python3-pysnmp depends on python3-smi.
# This leads to a circular dependency that may cause side-effects.
#%check
#%{__python3} setup.py test

%files -n python3-smi
%doc CHANGES.rst README.md THANKS.txt TODO.txt examples/*.py
%license LICENSE.rst
%{_bindir}/mibcopy
%{_bindir}/mibdump
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{srcname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-3
- Disable tests

* Fri May 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-2
- Enable tests

* Sun May 05 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-1
- Initial package for Fedora
